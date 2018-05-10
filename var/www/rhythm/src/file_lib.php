<?php
include_once ("lib.php");

if (defined('WIN')) {
    $GLOBALS['tmpDir'] = '.\\tmp\\';
    $GLOBALS['exampleDir'] = '.\\examples\\';
    $GLOBALS['dir'] = dirname(__FILE__);
    define('SEP', '\\');
} else {
    $GLOBALS['tmpDir'] = './tmp/';
    $GLOBALS['exampleDir'] = dirname(__FILE__) . '/../examples/';
    $GLOBALS['dir'] = '';
    define('SEP', '/');
}

function get_examples() {

    $examples = array();
    
    if (file_exists($GLOBALS['exampleDir'] . 'channels' . SEP)) {
	$channels = scandir($GLOBALS['exampleDir'] . 'channels' . SEP);
	foreach($channels as $c) {
	    
	    if ($c{0} != '.' && substr($c, strrpos($c, '.') + 1) == 'txt') {
		$examples[] = 'channels' . SEP . substr($c, 0, strrpos($c, '.'));
	    }
	}
    }
    
    if (file_exists($GLOBALS['exampleDir'] . 'coils' . SEP)) {
	$coils = scandir($GLOBALS['exampleDir'] . 'coils' . SEP);
	foreach($coils as $c) {
	    
	    if (substr($c, strrpos($c, '.') + 1) == 'txt') {
		$examples[] = 'coils' . SEP . substr($c, 0, strrpos($c, '.'));
	    }
	}
    }
    $examplesByChains = array();
    foreach($examples as $ex) {
	$chains = get_exampleChains($ex);
	foreach($chains as $c) $examplesByChains[] = $ex . ':' . $c;
    }
    $examples = $examplesByChains;
    return ($examples == array()) ? FALSE : $examples;
}

function get_exampleChains($ex) {

    $curatedData = read_curated($GLOBALS['exampleDir'] . $ex . '.txt');
    $chains = array();
    foreach($curatedData as $row) {
	list(, $chainId) = split(" ", trim($row['AAId']));
	$chains[] = $chainId;
    }
    return array_unique($chains);
}

function readMatrix($filename) {

    $file = fopen($filename, "r");
    $list = array();
    while (!feof($file)) {
	$line = trim(chop(fgets($file)));
	
	if ($line) $list[substr($line, 0, 1) ] = preg_split("/[\t ]+/", trim(substr($line, 2)));
    }
    return ($list);
}

function read_hmmer($file, $chain = FALSE) {

    $handle = fopen($file, "r+");
    
    if ($handle) {
	$all_domains = array();
	$i = 0;
	while ($line = fgets($handle)) {
	    $data[] = $line;
	    
	    if (!$chain || preg_match('/^Query sequence: [a-zA-Z0-9]+:' . $chain . '\|PDBID\|CHAIN\|SEQUENCE/', $line)) {
		while ($line = fgets($handle)) {
		    
		    if (preg_match('/^Query sequence: .*/', $line)) break;
		    
		    if (preg_match('/^Alignments of top-scoring domains/', $line)) {
			$line = fgets($handle);
			
			if (preg_match('/\[no hits above thresholds\]/', $line)) return array();
			while ($line && substr($line, 0, 2) != '//') {

			    //for(;trim($line) == ''; $line = fgets($handle)){}
			    
			    if (strlen($line) > 1 && $line{0} != ' ' && $line{0} != '/' && $line{1} != '/') {
				preg_match('/(.+): domain ([0-9]+) of ([0-9]+), from ([0-9]+) to ([0-9]+): score ([e0-9\.-]+), E = ([e0-9\.-]+)/', $line, $m);
				array_shift($m);
				list($dname, $di, $dn, $beg, $end, $score, $evalue) = $m;
				$line = fgets($handle);
				$profile = '';
				$consensus = '';
				$search = '';
				$start = TRUE;
				while ($line{0} == ' ') {
				    
				    if (preg_match('/^[ ]*RF/', $line)) $line = fgets($handle);
				    
				    if ($start) {
					$start = FALSE;
					$b = 22;
					$l = 47;
				    } else {
					$b = 19;
					$l = 50;
				    }
				    $line2 = fgets($handle);
				    $line3 = fgets($handle);
				    preg_match(' ([0-9]+)', substr($line3, 19) , $m, PREG_OFFSET_CAPTURE);
				    @$diff = $m[0][1] - 50;
				    
				    if ($diff < 1) {
					$l = $l + ($diff) - 3 - 1;
				    }
				    $profile.= str_replace(" ", " ", substr($line, $b, $l));
				    $consensus.= str_replace(" ", " ", substr($line2, $b, $l));
				    $search.= str_replace(" ", " ", substr($line3, $b, $l));
				    $line = fgets($handle);
				    $line = fgets($handle);
				}
				$domain['beg'] = $beg;
				$domain['end'] = $end;
				$domain['score'] = (double)$score;
				$domain['evalue'] = (double)$evalue;
				$domain['name'] = $dname;
				$domain['profile'] = str_replace(array(
				    "\n",
				    "\r"
				) , array(
				    "",
				    ""
				) , $profile);
				$domain['consensus'] = str_replace(array(
				    "\n",
				    "\r"
				) , array(
				    "",
				    ""
				) , $consensus);
				$domain['search'] = str_replace(array(
				    "\n",
				    "\r"
				) , array(
				    "",
				    ""
				) , $search);
				$all_domains[] = $domain;
			    } else {
				$line = fgets($handle);
			    }
			}
		    }
		}
	    }
	}
	fclose($handle);
    }

    //debug($all_domains);
    return ($all_domains);
}

function read_hmmtop($file, $chain = "first") {

    $k = 0;
    $map = array(
	'first' => 1,
	0 => 1,
	'' => 1
    );
    $allAsPos = array();
    $allPrediction = array();
    $prediction = "";
    $as_pos = array();
    $handle = fopen($file, "r+");
    
    if ($handle) {
	$i = 0;
	while (($line = fgets($handle))) { // && ($i < 2)) {

	    $data[] = $line;
	    
	    if (strpos($line, "OUT") == TRUE || strpos($line, " IN ") == TRUE) {
		preg_match('/[a-zA-Z0-9]+:([a-zA-Z]+)\|PDBID\|CHAIN\|SEQUENCE/', trim($line) , $m);
		$i+= 1;
		
		if (array_key_exists(1, $m)) $map[$m[1]] = $i;
		$prediction[$i] = '';
	    }
	    
	    if (strpos($line, "OUT") == TRUE) {
		$split_line = split("OUT", $line);
		
		if (preg_match_all("([0-9]+)", $split_line[1], $array)) {
		    array_shift($array[0]);
		    $as_pos[$i] = $array[0];
		}
	    } else 
	    if (strpos($line, " IN ") == TRUE) {
		$split_line = split(" IN ", $line);
		
		if (preg_match_all("([0-9]+)", $split_line[1], $array)) {
		    array_shift($array[0]);
		    $as_pos[$i] = $array[0];
		}
	    } else 
	    if (strpos($line, "pred") == TRUE) {
		$prediction[$i].= str_replace(array(
		    "pred",
		    " ",
		    "\r\n",
		    "\n",
		    "\r"
		) , "", $line);
	    }
	}
    }

    //debug($map);
    
    //debug(array($as_pos,$prediction));

    return (array(
	$as_pos[$map[$chain]],
	$prediction[$map[$chain]]
    ));
}

function read_fasta($file, $chain = "first") {

    $data = "";
    $name = '';
    $handle = fopen($file, "r+");
    
    if ($handle) {
	$i = 0;
	$map = array(
	    'first' => 1,
	    '' => 1
	);
	while ($line = fgets($handle)) {
	    
	    if (strpos(trim($line) , '>') === 0) {
		preg_match('/>[a-zA-Z0-9]+:([a-zA-Z]+)\|PDBID\|CHAIN\|SEQUENCE/', trim($line) , $m);
		$i+= 1;
		
		if (array_key_exists(1, $m)) $map[$m[1]] = $i;
	    }
	    $all_data[$i][] = $line;
	}
	
	if (array_key_exists($map[$chain], $all_data) && is_array($all_data[$map[$chain]])) {
	    $name = array_shift($all_data[$map[$chain]]);
	    $data = str_replace(array(
		"\r\n",
		"\n",
		"\r"
	    ) , "", implode("", $all_data[$map[$chain]]));
	} else {
	    $data = '';
	}
    }
    return (array(
	$name,
	$data
    ));
}

function read_curated($file) {

    $delimiter = "\t";
    $data = array();
    $handle = fopen($file, "r");
    
    if ($handle && $line = fgetcsv($handle, 1000, $delimiter)) {
	$names = $line;
	while (($line = fgetcsv($handle, 1000, $delimiter)) !== FALSE) {
	    $data[] = array_combine($names, $line);
	}
	fclose($handle);
    }
    return $data;
}

function write_fasta($file, $seq, $name = '') {

    $handle = fopen($file, "w");
    
    if ($handle) {
	fwrite($handle, '> ' . $name . "\n");
	fwrite($handle, $seq);
    }
    fclose($handle);
}

function write_pymol($file, $predictionSeq, $compPredictionSeq = FALSE, $helixPositions = FALSE) {

    
    if (is_array($helixPositions) && !is_array(reset($helixPositions))) {
	$helixPositions = array(
	    'none' => $helixPositions
	);
    }
    
    if (!is_array($predictionSeq)) $predictionSeq = array(
	'none' => $predictionSeq
    );
    $predByType = array();
    foreach($predictionSeq as $chain => $predSeq) {
	
	if ($compPredictionSeq && array_key_exists($chain, $compPredictionSeq)) {
	    $compPredSeq = $compPredictionSeq[$chain];
	} else {
	    $compPredSeq = FALSE;
	}
	$predByType[$chain] = array();
	$n = strlen($predSeq);
	for ($i = 0;$i < $n;++$i) {
	    
	    switch ($predSeq{$i}) {
		case 'H':
		    
		    if ($compPredSeq && $compPredSeq{$i} != $predSeq{$i}) {
			$predByType[$chain]['he'][] = (string)($i + 1);
		    } else {
			$predByType[$chain]['h'][] = (string)($i + 1);
		    }
		break;
		case 'M':
		    
		    if ($compPredSeq && $compPredSeq{$i} != $predSeq{$i}) {
			$predByType[$chain]['me'][] = (string)($i + 1);
		    } else {
			$predByType[$chain]['m'][] = (string)($i + 1);
		    }
		break;
		case 'W':
		    
		    if ($compPredSeq && $compPredSeq{$i} != $predSeq{$i}) {
			$predByType[$chain]['we'][] = (string)($i + 1);
		    } else {
			$predByType[$chain]['w'][] = (string)($i + 1);
		    }
		break;
	    }
	}
	foreach($predByType[$chain] as $type => $data) {
	    $predByType[$chain][$type] = "'" . $type . "' : ['" . implode("','", $data) . "']";
	}
	$predByType[$chain] = "'" . $chain . "' : {\n\t\t" . implode(",\n\t\t", $predByType[$chain]) . "\n\t\t}";
    }
    $predByType = "{\n\t" . implode(",\n\t", $predByType) . "\n\t}";

    // helix
    $aHelixPosBeginEnd = array();
    
    if ($helixPositions) {
	foreach($helixPositions as $chain => $helPos) {
	    $n = count($helPos);
	    for ($i = 0;$i < $n;$i+= 2) {
		$aHelixPosBeginEnd[$chain][] = array(
		    $helPos[$i],
		    $helPos[$i + 1]
		);
	    }
	}
    }

    foreach($aHelixPosBeginEnd as $chain => $helPos) {
	foreach($helPos as $k => $beginEnd) {
	    list($begin, $end) = $beginEnd;
	    $aHelixPosBeginEnd[$chain][$k] = "[" . $begin . "," . $end . "]";
	}
	$aHelixPosBeginEnd[$chain] = "'" . $chain . "' : [" . implode(",", $aHelixPosBeginEnd[$chain]) . "]";
    }
    $aHelixPosBeginEnd = "{\n\t" . implode(",\n\t", $aHelixPosBeginEnd) . "\n\t}";

    // template
    $pymolSkeleton = file_get_contents('.' . SEP . 'misc' . SEP . 'color_pred_res-skeleton.py');
    $handle = fopen($file, "w");
    
    if ($handle) {
	fwrite($handle, str_replace(array(
	    '###PREDRES###',
	    '###HELIXPOS###'
	) , array(
	    $predByType,
	    $aHelixPosBeginEnd
	) , $pymolSkeleton));
    }
    fclose($handle);
}

function write_results($file, $prediction, $my_line, $output_seq, $conserved) {


    //Breche den String nach 50 Zeichen um, und splitte ihn danach nach dem Zeilenumbruch in ein array
    $prediction = explode("\n", wordwrap(@$prediction, 50, "\n", 1));
    $my_line = explode("\n", wordwrap($my_line, 50, "\n", 1));
    $output_seq = explode("\n", wordwrap($output_seq, 50, "\n", 1));
    $conserved = explode("\n", wordwrap($conserved, 50, "\n", 1));
    $handle = fopen($file, "w+");
    
    if ($handle) {
	
	if ($prediction . $my_line . $output_seq . $conserved == '') {
	} else {
	    fwrite($handle, "> Output Seq. :\n");
	    for ($i = 0;$i < count($prediction);$i++) {
		fwrite($handle, "Sequence:\t" . $output_seq[$i]);
		fwrite($handle, "\n");
		fwrite($handle, "HMMTOP pred:\t" . $prediction[$i]);
		fwrite($handle, "\n");
		fwrite($handle, "Conserved:\t" . $conserved[$i]);
		fwrite($handle, "\n");
		fwrite($handle, "RHYTHM results:\t" . $my_line[$i]);

		//fwrite($handle, "\tRHYTHM results:\t".str_replace("U", " ", $my_line[$i]));
		fwrite($handle, "\n\n");
	    }
	}
    }
    fclose($handle);

    //debug(file_get_contents($file));
    
}
?>