<?php
include_once ("lib.php");
include_once ("file_lib.php");
include_once ("image_lib.php");
include_once ("class_simpleLog.php");

class helixContactPrediction {
    
    var $seq;
    
    var $pType;
    
    var $optimizeFor;
    
    var $optimizationLevel;
    
    var $helixPos;
    
    var $helixSeq;
    
    var $helixPrediction;
    
    var $pfamDomains = array();
    
    var $foundPfamDomains = array();
    
    var $curatedData = array();
    
    var $map;
    
    var $seqFile;
    
    var $status;
    
    var $optLevelDef = array();
    
    var $optLevelDefAll = array(
	'channel' => array(
	    'h' => array(
		'higher' => '0.9',
		'high' => '0.85',
		'medium' => '0.8',
		'low' => '0.75'
	    ) ,
	    'm' => array(
		'higher' => '0.9',
		'high' => '0.85',
		'medium' => '0.8',
		'low' => '0.75'
	    ) ,
	    'w' => array(
		'higher' => '0.9',
		'high' => '0.85',
		'medium' => '0.8',
		'low' => '0.75'
	    ) ,
	) ,
	'coil' => array(
	    'h' => array(
		'higher' => '0.9',
		'high' => '0.85',
		'medium' => '0.8',
		'low' => '0.75'
	    ) ,
	    'm' => array(
		'higher' => '0.9',
		'high' => '0.85',
		'medium' => '0.8',
		'low' => '0.75'
	    ) ,
	    'w' => array(
		'higher' => '0.9',
		'high' => '0.85',
		'medium' => '0.8',
		'low' => '0.75'
	    ) ,
	)
    );
    
    var $consBonus = array();
    
    var $consBonusAll = array(
	'channel' => array(
	    'higher' => 0.8,
	    'high' => 0.6,
	    'medium' => 0.3,
	    'low' => 0.0
	) ,
	'coil' => array(
	    'higher' => 0.1,
	    'high' => 0.2,
	    'medium' => 0.5,
	    'low' => 0.5
	) ,
    );

    // helix can contain the helixPos or a boolean for example input
    
    function init($input, $pType, $optimizeFor, $optimizationLevel, $helix = FALSE, $useCons = TRUE) {

	$this->log = & simpleLog::getInstance();
	$this->pType = $pType;
	$this->optimizeFor = $optimizeFor;
	$this->optimizationLevel = $optimizationLevel;
	$hmmtopFile = FALSE;
	$hmmerFile = FALSE;
	$chain = FALSE;
	
	if (substr($input, 0, 5) == 'FILE:') {
	    $this->seqFile = substr($input, 5);
	    list(, $this->seq) = read_fasta($this->seqFile);
	} elseif (substr($input, 0, 4) == 'PDB:') {
	} elseif (substr($input, 0, 8) == 'EXAMPLE:') {
	    $chainId = FALSE;
	    list($example, $chainId) = split(':', substr($input, 8));
	    $this->seqFile = $GLOBALS['exampleDir'] . $example . '.fasta';
	    $hmmerFile = $GLOBALS['exampleDir'] . $example . '.hmmer';
	    $hmmtopFile = $GLOBALS['exampleDir'] . $example . '.hmmtop';
	    $curatedData = read_curated($GLOBALS['exampleDir'] . $example . '.txt');
	    
	    if (!$chainId) list(, $chainId) = split(" ", trim($curatedData[0]['AAId']));
	    list(, $this->seq) = read_fasta($this->seqFile, $chainId);
	    $chain = $chainId;
	    $this->log->write($chainId);
	    $currentChainId = $chainId;
	    while ((list(, $row) = each($curatedData))) { // && $chainId == $currentChainId

		list($asId, $chainId) = split(" ", trim($row['AAId']));
		
		if ($chainId == $currentChainId) $this->curatedData[$asId] = $row;
	    }
	    
	    if ($helix) {
		$helix = array();
		$helixNr = array();
		$helixPos = array();
		foreach($this->curatedData as $asId => $dat) {
		    
		    if ($dat['I/A'] == '1'

		    //|| $dat['I/A'] == '0'
		    ) $helixNr[$dat['H-Nr']][] = $asId;
		}
		$i = 0;
		foreach($helixNr as $as) {

		    //debug($as);
		    $helixPos[] = min($as);
		    $helixPos[] = max($as);
		    $helixSeq[$i] = '';
		    foreach($as as $pos) {
			$helixSeq[$i].= $this->curatedData[$pos]['AA'];
		    }
		    ++$i;
		}
		$helix['pos'] = $helixPos;
	    }
	} else {
	    $this->seq = $input;
	    $this->writeSeq();
	}
	$this->initMat();
	
	if ($useCons) $this->getPfamDomains($hmmerFile, $chain);
	$this->status['helix'] = FALSE;
	
	if ($helix) {
	    
	    if (max($helix['pos']) < strlen($this->seq)) {
		$this->helixPos = $helix['pos'];
		$this->helixPrediction = array_key_exists('prediction', $helix) ? $helix['prediction'] : str_repeat('-', strlen($this->seq));
		$this->helixSeq = $this->helixPosToSeq($this->helixPos);
		$this->status['helix'] = TRUE;
	    } else {
		$this->log->write('The given helix definitions don\'t match sequence length, trying to predict helices instead.', TRUE);
	    }
	}
	
	if (!$this->status['helix']) {
	    $this->getHelices($hmmtopFile, $chain);
	}
	$this->getHelixBegEndPos();

	//debug(array($this->seq));
	
	//$this->log->write($this->pfamDomains);

	$this->log->write($this->helixPos);

	//$this->log->write($hmmerFile);
	
	//$this->log->write(wordwrap($this->seq, 50, "\n", 1));

	
	//$this->log->write($chain);

	
	//$this->log->write(strlen($this->seq));

	$this->log->write($this->seq);
	$this->log->write($this->helixPrediction);

	//debug($this->helixSeq);
	
    }
    
    function status($name = FALSE) {

	if ($name) {
	    return array_key_exists($name, $this->status) ? $this->status[$name] : FALSE;
	} else {
	    
	    if (is_array($this->status)) {
		foreach($this->status as $c) if (!$c) return FALSE;
	    } else {
		return FALSE;
	    }
	    return TRUE;
	}
    }
    
    function writeSeq() {

	if (!$GLOBALS['sessionId']) {
	    $this->status['seqFile'] = FALSE;
	    return FALSE;
	}
	$this->seqFile = $GLOBALS['tmpDir'] . $GLOBALS['sessionId'] . '_seq.fasta';
	write_fasta($this->seqFile, $this->seq, 'session id: ' . $GLOBALS['sessionId']);
    }
    
    function decideCurContact($dat) {

	
	if ($dat['Hel'] > $dat['Memb'] && $dat['Hel'] > $dat['H2O']) {
	    return 'h';
	} elseif ($dat['Memb'] > $dat['Hel'] && $dat['Memb'] > $dat['H2O']) {
	    return 'm';
	} elseif ($dat['H2O'] > $dat['Hel'] && $dat['H2O'] > $dat['H2O']) {
	    return 'w';
	}
	return FALSE;
    }
    
    function getPfamDomains($hmmerFile = FALSE, $chain = FALSE) {

	$this->status['pfam'] = FALSE;
	
	if (!$GLOBALS['sessionId']) return FALSE;
	
	if (!$hmmerFile) $hmmerFile = $GLOBALS['tmpDir'] . $GLOBALS['sessionId'] . '_hmmer.out';
	$seqFile = $this->seqFile;
	
	if ($this->hmmerStatus($hmmerFile)) {
	    $pfamDomains = read_hmmer($hmmerFile, $chain);
	    foreach($pfamDomains as $v) {
		
		if ($v['evalue'] < 0.1 && $v['score'] > 20) $this->pfamDomains[] = $v;
	    }

	    //debug($this->pfamDomains);
	    $this->status['pfam'] = TRUE;
	} elseif (is_file($hmmerFile)) {
	    $this->log->write('hmmer running and locking file/writing data?');
	} else {
	    $this->hmmer($this->seqFile, $hmmerFile);
	}
    }

    // must be callable from outside this class
    
    function hmmerStatus($hmmerFile = FALSE) {

	
	if (!$hmmerFile) $hmmerFile = $GLOBALS['tmpDir'] . $GLOBALS['sessionId'] . '_hmmer.out';
	return (is_file($hmmerFile) && is_readable($hmmerFile) && is_writeable($hmmerFile) && @filesize($hmmerFile) > 0);
    }
    
    function getHelices($hmmtopFile = FALSE, $chain = FALSE) {

	$this->status['helix'] = FALSE;
	$this->status['helixHmmtop'] = FALSE;
	
	if (!$GLOBALS['sessionId']) return FALSE;
	
	if (!$hmmtopFile) $hmmtopFile = $GLOBALS['tmpDir'] . $GLOBALS['sessionId'] . '_hmmtop.out';
	$seqFile = $this->seqFile;
	$maxWait = 2;
	for ($i = 0;($i <= $maxWait);++$i, sleep(1)) {
	    
	    if (is_readable($hmmtopFile)) {
		list($this->helixPos, $this->helixPrediction) = read_hmmtop($hmmtopFile, $chain);
		
		if (!$this->helixPos) {
		    $this->log->write('Hmmtop found no helices. Defining the entire sequence as one helix.', TRUE);
		    $this->helixPos = array(
			1,
			strlen($this->seq)
		    );
		    $this->helixPrediction = str_repeat('-', strlen($this->seq));
		} else {
		    $this->status['helixHmmtop'] = TRUE;
		}
		$this->status['helix'] = TRUE;
		break;
	    } elseif (is_file($hmmtopFile)) {
		$this->log->write('hmmtop running and locking file/writing data?');
	    } else {
		$this->hmmtop($this->seqFile, $hmmtopFile);
	    }
	}
	$this->helixSeq = $this->helixPosToSeq($this->helixPos);
    }
    
    function getHelixBegEndPos() {

	
	if (!$this->helixPos) return;
	$n = strlen($this->seq);
	$this->helixBegEndPos = array();
	for ($i = 0;$i < $n;++$i) {
	    $hBeg = 0;
	    $hEnd = $n;
	    $m = count($this->helixPos) - 1;
	    for ($j = 0;$j < $m;$j+= 2) {
		
		if ($i >= $this->helixPos[$j] - 1 && $i <= $this->helixPos[$j + 1] - 1) {
		    $hBeg = $this->helixPos[$j] - 1;
		    $hEnd = $this->helixPos[$j + 1] - 1;
		    break;
		}
	    }
	    $this->helixBegEndPos[$i] = array(
		$hBeg,
		$hEnd
	    );
	}
    }
    
    function helixPosToSeq($helixPos) {

	$helixSeq = array();
	$n = count($helixPos) - 1;
	for ($i = 0;$i < $n;$i+= 2) {
	    $helixSeq[] = substr($this->seq, $helixPos[$i] - 1, $helixPos[$i + 1] - $helixPos[$i] + 1);
	}
	return $helixSeq;
    }
    
    function _selectMat($matType) {

	
	switch ($matType) {
	    case 'h':
		return $this->mat_helix;
	    break;
	    case 'm':
		return $this->mat_membrane;
	    break;
	    case 'w':
		return $this->mat_water;
	    break;
	}
    }
    
    function initMat() {

	
	switch ($this->pType) {
	    case 'coil':
		$this->mat_helix = readMatrix("./mat/coil4_helix.mat");
		$this->mat_membrane = readMatrix("./mat/coil4_membran.mat");
		$this->mat_water = readMatrix("./mat/coil4_water.mat");
	    break;
	    case 'channel':
		$this->mat_helix = readMatrix("./mat/gate4_helix.mat");
		$this->mat_membrane = readMatrix("./mat/gate4_membran.mat");
		$this->mat_water = readMatrix("./mat/gate4_water.mat");
	    break;
	}
	
	if ($this->pType == 'channel') $pType = 'channel';
	elseif ($this->pType == 'coil') $pType = 'coil';
	$this->optLevelDef = $this->optLevelDefAll[$pType];
	$this->consBonus = $this->consBonusAll[$pType];
	
	if ($this->optimizeFor == 'sens') $optFor = 'sen';
	elseif ($this->optimizeFor == 'spec') $optFor = 'spec';
	$optimalLevelDat = array();
	$this->optimalLevelDat = array();
	$r = $optFor == 'spec' ? 2 : 1;
	foreach(array(
	    'm' => 'mem',
	    'h' => 'hel',
	    'w' => 'wat'
	) as $key => $type) {
	    $optimalLevelDat[$key] = readMatrix('./mat/' . $pType . '_' . $optFor . '_' . $type . '.dat');
	    foreach($optimalLevelDat[$key] as $row) {
		$this->optimalLevelDat[$key][(string)(round($row[$r], 2)) ] = $row[0];
	    }
	}

	//debug($this->optimalLevelDat);
	
    }
    
    function predictAll($i) {

	return array(
	    $this->predict($i, 'h') ,
	    $this->predict($i, 'm') ,
	    $this->predict($i, 'w')
	);
    }
    
    function predict($i, $matType) {

	list($hBeg, $hEnd) = $this->helixBegEndPos[$i];
	$mat = $this->_selectMat($matType);
	$pm = (count($mat["A"]) - 1) / 2;
	$n = strlen($this->seq);
	$pep = "";
	for ($pos = $i - $pm;$pos <= $i + $pm;$pos++) {
	    
	    if ($pos < 0 || $pos >= $n || $pos < $hBeg || $pos > $hEnd) {
		$pep.= "O";
	    } else {
		$pep.= $this->seq[$pos];
	    }
	}
	$score = 0;
	for ($k = 0;$k < strlen($pep);$k++) {
	    
	    if ($pep[$k] != "O") {
		$score+= $mat[$pep[$k]][$k];
	    }
	}
	return ($score);
    }

    // TODO: doClassification would be a better name
    
    function doScoring($hel, $mem, $wat, $cons = FALSE) {


	// you can use $this->pType which is either coil or channel
	
	// $this->optimizationLevel is in: high, medium or low

	
	// $this->optimizeFor is in: sens, spec

	
	if ($hel >= $this->optimalLevelDat['h'][$this->optLevelDef['h'][$this->optimizationLevel]]) {
	    $erg = "h";
	} elseif ($mem >= $this->optimalLevelDat['m'][$this->optLevelDef['m'][$this->optimizationLevel]]) {
	    $erg = "m";

	    //}elseif ($wat >= $this->optimalLevelDat['w'][$this->optLevelDef['w'][$this->optimizationLevel]]) {
	    
	    //$erg = "w";

	    
	} elseif ($cons !== FALSE && $this->consLevel($cons) == 3 && $hel + $this->consBonus[$this->optimizationLevel] >= $this->optimalLevelDat['h'][$this->optLevelDef['h'][$this->optimizationLevel]]) {
	    $erg = "h";
	} else {
	    $erg = "u";
	}
	return $erg;
    }

    // $hmmtopfile - output
    
    // $uploadfile - input

    
    function hmmtop($uploadfile, $hmmtopfile) {


	// need to go to a directory where a hmmtop-'arch' file is
	
	if (defined('OSX')) {
	    $s = "cd " . dirname(__FILE__) . "/../bin/hmmtop/; ./hmmtop -if=../../$uploadfile -of=../../$hmmtopfile -pl";
	} elseif (defined('WIN')) {
	    $s = "start /D \"" . dirname(__FILE__) . "\\..\\bin\\hmmtop\" /B hmmtop2.exe -if=..\\..\\$uploadfile -of=..\\..\\$hmmtopfile -pl";
	} elseif (defined('LINUX')) {
	    
	    if (defined('ARM')) {
		$s = "cd " . dirname(__FILE__) . "/../bin/hmmtop/; ./hmmtop_arm -if=../../$uploadfile -of=../../$hmmtopfile -pl";
	    }else{
		$s = "cd " . dirname(__FILE__) . "/../bin/hmmtop/; ./hmmtop_linux -if=../../$uploadfile -of=../../$hmmtopfile -pl";
	    }
	}
	
	$this->log->write($s);
	$out;
	exec($s,$out);
	$this->log->write($out);
    }
    
    
    function hmmer($uploadfile, $hmmerfile, $hmm = "Pfam_ls") {


	//	 exec("./src/hmmtop/hmmtop -if=$uploadfile -of=$hmmtopfile -pl");
	
	if (defined('OSX')) {
	    $s = "(" . dirname(__FILE__) . "/../bin/hmmer/hmmpfam" . " res/" . $hmm . " " . dirname(__FILE__) . "/../" . $uploadfile . " > " . dirname(__FILE__) . "/../" . $hmmerfile . ") >/dev/null &" . "";

	    //debug($s);
	    exec($s);
	} elseif (defined('WIN')) {
	    exec("start /D \"" . dirname(__FILE__) . "\\..\\bin\\hmmer\" /B hmmpfam.exe" . " ..\\..\\res\\" . $hmm . " ..\\..\\" . $uploadfile . " > .\\" . $hmmerfile);
	} elseif (defined('LINUX')) {
	    exec("(./bin/hmmer/hmmpfam_linux" . " res/" . $hmm .

	    //	      " ../.".$uploadfile.
	    " " . $uploadfile . " > " . $hmmerfile . ") >/dev/null &" . "");
	}
    }
    
    function consLevel($cons) {

	
	if (!$cons) return 0;
	$l = 0;
	foreach($cons as $name => $type) {
	    
	    if ($type == '+') {
		$l = $l > 1 ? $l : 1;
	    } elseif (is_upper($type)) {
		return 3;
	    } elseif (is_lower($type)) {
		$l = $l > 2 ? $l : 2;
	    }
	}
	return $l;
    }
    
    function search_conserved($pos) {

	$result = array();
	foreach($this->pfamDomains as $domain) {
	    
	    if ($pos >= $domain['beg'] && $pos <= $domain['end']

	    //&& $domain['evalue'] < 0.1
	    
	    //&& $domain['score'] > 20

	    ) {

		// adjust for gaps
		$posD = $pos - $domain['beg'];
		$j = 0;
		$k = 0;
		while ($j < $posD || $domain['search'] {
		    $k
		} == '-') {
		    
		    if ($domain['search'] {
			$k
		    } != '-') ++$j;
		    ++$k;
		}

		// data integrity check
		
		if (FALSE && strtoupper($domain['search'] {
		    $k
		}) != strtoupper($this->seq{$pos - 1})) debug(array(
		    'pfam data integrity problem',
		    $domain,
		    'pos: ' . ($pos - 1) ,
		    'k: ' . ($k) ,
		    'seq: ' . $this->seq{$pos},
		    'search: ' . $domain['search'] {
			$k
		    }
		    ,
		));
		$x = $domain['consensus'] {
		    $k
		};
		
		if ($x != ' ' && $x != '+' && is_upper($x)) {

		    //echo $domain['evalue']." - ".($domain['evalue'] < 1)."<br/>";
		    $result[$domain['name']] = $x;
		    
		    if (!in_array($domain['name'], $this->foundPfamDomains)) $this->foundPfamDomains[] = $domain['name'];
		}
	    }
	}
	return $result;
    }
}
?>