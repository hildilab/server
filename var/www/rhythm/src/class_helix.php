<?php
include_once ("lib.php");
include_once ("file_lib.php");
include_once ("class_simpleLog.php");
include_once ("class_helixImage.php");
ini_set('max_execution_time', '600');

class helix {
    
    var $oParent;
    
    var $log;
    
    var $content = '';
    
    var $messages = array();
    
    var $helix;
    
    var $matType;
    
    var $optimizeFor = 'spec';
    
    var $optimizationLevel;
    
    var $useCons;
    
    var $chainName;
    
    var $oHCP2 = NULL;
    
    var $aHCP = NULL;
    
    function init(&$oParent) {

	$this->log = & simpleLog::getInstance();
	
	if (is_object($oParent)) {
	    $this->oParent = & $oParent;
	    $this->smarty = & $this->oParent->smarty;
	} else {
	    return FALSE;
	}
	
	if (!$this->_getAndInitMode()) {

	    // show form
	    $this->log->write('showing form');
	    $this->smarty->assign('contentTplFile', 'helix_form.tpl');
	    $GLOBALS['jsVARS']['exampleSeqChannel'] = 'APAVADKADNAFMMICTALVLFMTIPGIALFYGGLIRGKNVLSMLTQVTVTFALVCILWV
VYGYSLAFGEGNNFFGNINWLMLKNIELTAVMGSIYQYIHVAFQGSFACITVGLIVGALA
ERIRFSAVLIFVVVWLTLSYIPIAHMVWGGGLLASHGALDFAGGTVVHINAAIAGLVGAY
LIGKRVGFGKEAFKPHNLPMVFTGTAILYIGWFGFNAGSAGTANEIAALAFVNTVVATAA
AILGWIFGEWALRGKPSLLGACSGAIAGLVGVTPACGYIGVGGALIIGVVAGLAGLWGVT
MLKRLLRVDDPCDVFGVHGVCGIVGCIMTGIFAASSLGGVGFAEGVTMGHQLLVQLESIA
ITIVWSGVVAFIGYKLADLTVGLRVPEEQEREGLDVNSHGENAYNADQAQQPAQADLE';
	    $GLOBALS['jsVARS']['exampleSeqCoil'] = 'ERAGPVTWVMMIACVVVFIAMQILGDQEVMLWLAWPFDPTLKFEFWRYFTHALMHFSLMH
ILFNLLWWWYLGGAVEKRLGSGKLIVITLISALLSGYVQQKFSGPWFGGLSGVVYALMGY
VWLRGERDPQSGIYLQRGLIIFALIWIVAGWFDLFGMSMANGAHIAGLAVGLAMAFVDSL
NA';
	    
	    if (defined('EXAMPLES')) {
		$examples = get_examples();
		
		if ($examples) $this->smarty->assign('examples', $examples);
	    }
	} else {
	    
	    if (isset($this->example) && $this->example) {
		list($ex,) = split(':', $this->example);
		$chains = get_exampleChains($ex);
		foreach($chains as $c) {
		    $this->aHCP[$c] = new helixContactPrediction();
		    $this->aHCP[$c]->init('EXAMPLE:' . $ex . ':' . $c, $this->matType, $this->optimizeFor, $this->optimizationLevel, TRUE, $this->useCons);
		}
		$this->oHCP2 = new helixContactPrediction();
		$this->oHCP2->init($this->seq, $this->matType, $this->optimizeFor, $this->optimizationLevel, TRUE, $this->useCons);
	    }
	    $oHCP = new helixContactPrediction();
	    $oHCP->init($this->seq, $this->matType, $this->optimizeFor, $this->optimizationLevel, $this->helix, $this->useCons);
	    
	    if (!$this->helix && $oHCP->status('helix')) {
		$this->smarty->assign('hmmtopHelix', wordwrapBySpecifyChars('Predicted helices: ' . $this->encodeHelixPos(array(
		    'pos' => $oHCP->helixPos,
		    'prediction' => $oHCP->helixPrediction
		)) , 60, '<br/>', array(
		    ','
		)));
	    }
	    $GLOBALS['jsVARS']['sessionId'] = $GLOBALS['sessionId'];
	    $params = array(
		'site' => 'helix',
		'mat' => $this->matType,
		'optLevel' => $this->optimizationLevel,
		'useCons' => $this->useCons,
		'helix' => $this->encodeHelixPos($this->helix) ,
		'sessionId' => $GLOBALS['sessionId'],
	    );
	    
	    if ($oHCP->status('helix')) {

		// show results
		$this->log->write('showing results');
		$this->smarty->assign('contentTplFile', 'helix_result.tpl');
		$this->content.= $this->_drawResults($oHCP, $this->content);
		
		if (!$oHCP->status()) {
		    $this->smarty->assign('waitTplFile', 'helix_wait.tpl');
		    $this->smarty->assign('params', explodeArrayForURL($params));
		}
		$this->smarty->assign('update', TRUE);
		$updateParams = array(
		    'site' => 'helix',
		    'example' => $this->example,
		    'sessionId' => $GLOBALS['sessionId'],
		);
		$this->smarty->assign('updateParams', explodeArrayForURL($updateParams));
	    } else {

		// show update link
		$this->log->write('showing update link');
		$this->smarty->assign('contentTplFile', 'helix_wait.tpl');
		$this->smarty->assign('params', explodeArrayForURL($params));
	    }
	    $this->smarty->assign('content', $this->content);
	}
	
	$warnings = $this->log->get(SIMPLELOG_WARNING,SIMPLELOG_USER);
	if ($warnings) $this->smarty->assign('warnings', $warnings);
	$notes = $this->log->get(SIMPLELOG_NOTE,SIMPLELOG_USER);
	if ($notes) $this->smarty->assign('notes', $notes);
    }
    
    function _getAndInitMode() {

	$doPrediction = _GP('doPrediction');
	$doUpdate = _GP('doUpdate');
	$sessionId = _GP('sessionId');
	
	if($doUpdate) $this->log->write('Prediction updated.', SIMPLELOG_NOTE, SIMPLELOG_USER);
	
	if ($sessionId) {
	    $GLOBALS['sessionId'] = $sessionId;
	} else {
	    $GLOBALS['sessionId'] = random_str();
	}
	$base = $GLOBALS['tmpDir'] . $GLOBALS['sessionId'];
	$this->resultFile = $base . '_result.dat';
	$this->pymolFile = $base . '_pymol.py';
	$this->uploadFile = $base . '_upload.txt';
	$this->sequenceFile = $base . '_sequence.fasta';
	$this->imageFile = $base . '_' . time() . '_image.jpg';
	$this->example = _GP('example');
	
	if ($sessionId) {
	    $this->log->write("Reading file.");
	    list(, $seq) = read_fasta($this->sequenceFile);
	}
	
	if ($doPrediction) {
	    
	    if (array_key_exists('userfile', $_FILES) && !$_FILES['userfile']['error']) {
		
		if (move_uploaded_file($_FILES['userfile']['tmp_name'], $this->uploadFile)) {
		    $this->log->write("File upload successful.");
		    list(, $seq) = read_fasta($this->uploadFile);
		    
		    if (!$seq) $this->log->write('Uploaded file not in FASTA format.', SIMPLELOG_WARNING, SIMPLELOG_USER);
		} else {
		    $this->log->write('file upload failed or no file-upload');
		}
	    } elseif (array_key_exists('seq', $_POST) && ($_POST['seq'] != '' || $this->example == '')) {
		$this->log->write("Take manually entered sequence.");
		$seq = trim(strtoupper(_POST('seq')));
		$seq = str_replace(array(
		    "\r\n",
		    "\n",
		    "\r"
		) , "", $seq);
		
		if (ereg("[^ACDEFGHIKLMNPQRSTVWY]", $seq)) {
		    $this->log->write("Sequence contains illegal characters. Only amino
	  acid codes are allowed. Your sequence was modified!", SIMPLELOG_WARNING, SIMPLELOG_USER);
		    $seq = ereg_replace("[^ACDEFGHIKLMNPQRSTVWY]", "", $seq);
		}
	    } else {
		$this->log->write("Show an example.");
		$availableExamples = get_examples();
		
		if (!in_array($this->example, $availableExamples)) {
		    $this->example = $availableExamples[0];
		    $this->log->write('Illegal example specified.');
		}
		$seq = 'EXAMPLE:' . $this->example;
		$this->smarty->assign('example', $this->example);
	    }
	}
	$vars = array(
	    'optLevel' => array(
		'values' => array(
		    'higher',
		    'high',
		    'medium',
		    'low'
		) ,
		'names' => array(
		    'highest',
		    'very
				      high',
		    'high',
		    'medium'
		)
	    ) ,
	    'mat' => array(
		'values' => array(
		    'channel',
		    'coil'
		) ,
		'names' => array(
		    'channel',
		    'membrane-coil'
		)
	    ) ,
	);
	$this->smarty->assign('vars', $vars);
	$this->matType = _GP('mat');
	
	if (!in_array($this->matType, $vars['mat']['values'])) {
	    $this->matType = $vars['mat']['values'][0];
	    $this->log->write('Illegal matrix specified.');
	}
	$this->smarty->assign('mat', $this->matType);
	$this->optimizationLevel = _GP('optLevel');
	
	if (!in_array($this->optimizationLevel, $vars['optLevel']['values'])) {
	    $this->optimizationLevel = $vars['optLevel']['values'][1];
	    $this->log->write('Illegal optimization level specified.');
	}
	$this->smarty->assign('optLevel', $this->optimizationLevel);
	$this->useCons = (_GP('useCons') || (!$sessionId && !$doPrediction)) ? '1' : '0';
	$this->smarty->assign('useCons', $this->useCons);
	$this->helix = $this->parseHelixPos(_GP('helix'));
	
	if ($this->helix) {
	    $this->smarty->assign('helix', $this->encodeHelixPos($this->helix));
	} else {

	    // assign old, invalid value so the user can correct it
	    $this->smarty->assign('helix', _GP('helix'));
	}
	$chainName = _GP('chainName');
	
	if (strlen($chainName) > 2) {
	    $this->chainName = substr($chainName, 0, 2);
	    $this->log->write('The
      specified chain name was too long and has been cropped to a length of
      two.', SIMPLELOG_WARNING, SIMPLELOG_USER);
	} else {
	    $this->chainName = (string)$chainName;
	}
	$this->smarty->assign('chainName', $this->chainName);
	
	if (!$doPrediction && !$sessionId) {
	    return FALSE;
	}
	
	if ($seq) {
	    $this->seq = $seq;
	    write_fasta($this->sequenceFile, $seq, 'session id: ' . $GLOBALS['sessionId']);
	} else {
	    $this->log->write('No sequence available, can not proceed.', SIMPLELOG_WARNING, SIMPLELOG_USER);
	    return FALSE;
	}
	
	if ($doPrediction && $sessionId) {
	    $this->log->write('There is already a session running, you can not submit
      new data. Please start a new session to do that.', SIMPLELOG_WARNING, SIMPLELOG_USER);
	}
	$this->smarty->assign('sessionId', $sessionId);
	return TRUE;
    }
    
    function parseHelixPos($str) {


	// no input, no error
	
	if ($str == '') return FALSE;
	$pairSep = ',';
	$posSep = '-';
	$orientSep = ':';
	$helixPositions = array();
	$helixOrientations = array();
	$error = '';
	foreach(trimExplode($pairSep, $str) as $dirPosPair) {
	    
	    if (strstr($dirPosPair, $orientSep)) {
		list($dir, $posPair) = trimExplode($orientSep, $dirPosPair);
		
		if (!($dir == 'i' || $dir == 'o')) {
		    $this->log->write('wrong character in helix orientation
	  definition', SIMPLELOG_WARNING, SIMPLELOG_USER);
		    return FALSE;
		}
		$pos = trimExplode($posSep, $posPair);
		$helixOrientations[$pos[0]] = $dir;
	    } else {
		$pos = trimExplode($posSep, $dirPosPair);
	    }
	    $helixPositions = array_concat($helixPositions, $pos);
	}

	// check if positive integers
	foreach($helixPositions as $pos) {
	    
	    if (!is_numeric($pos)) {
		$this->log->write('helix definition string contains non numeric
	values', SIMPLELOG_WARNING, SIMPLELOG_USER);
		return FALSE;
	    } elseif (!(abs(intval($pos)) == $pos)) {
		$this->log->write('helix definition string contains non integer
	values', SIMPLELOG_WARNING, SIMPLELOG_USER);
		return FALSE;
	    }
	}

	// check if length even
	
	if (is_uneven(count($helixPositions))) {
	    $this->log->write('begin or end of some helix definition missing (number
      uneven).', SIMPLELOG_WARNING, SIMPLELOG_USER);
	    return FALSE;
	}

	// check if 'sorted'
	
	if (!is_sorted($helixPositions)) {
	    $this->log->write('helix definitions are in wrong order or
      overlapping.', SIMPLELOG_WARNING, SIMPLELOG_USER);
	    return FALSE;
	}
	
	if ($helixPositions == array()) {
	    $this->log->write('No helix definitions found.', SIMPLELOG_WARNING, SIMPLELOG_USER);
	    return FALSE;
	}
	$this->log->write($helixPositions);
	
	if (is_array($helixOrientations) || (isset($this->example) && $this->example)) {
	    $orientStates = array(
		'i',
		'o'
	    );
	    $s = 0;
	    $lastHelixPosition = - 1;
	    $helixPrediction = '';
	    $n = count($helixPositions);
	    for ($i = 0;$i < $n;$i+= 2) {
		
		if (array_key_exists($helixPositions[$i], $helixOrientations)) {
		    $orient = $helixOrientations[$helixPositions[$i]];
		    $s = ($orient == 'i') ? 1 : 0;
		} else {
		    $orient = $orientStates[$s % 2];
		    ++$s;
		}
		$helixPrediction.= str_repeat($orient, $helixPositions[$i] - $lastHelixPosition - 2);
		$helixPrediction.= str_repeat('H', $helixPositions[$i + 1] - $helixPositions[$i]);
		$helixPrediction.= str_repeat(($orient == 'i') ? 'o' : 'i', 2);
		$lastHelixPosition = $helixPositions[$i + 1];
	    }

	    //$helixPrediction .= str_repeat($orientStates[$s%2],3);
	    $this->log->write($helixPrediction);
	} else {
	    $helixPrediction = FALSE;
	}
	return array(
	    'pos' => $helixPositions,
	    'prediction' => $helixPrediction,
	    'orientation' => $helixOrientations
	);
    }
    
    function encodeHelixPos($helix) {

	
	if (!is_array($helix)) return '';
	$helixPositions = $helix['pos'];
	$helixPrediction = $helix['prediction'];
	
	if (!$helixPositions) return '';
	$pairSep = ',';
	$posSep = '-';
	$orientSep = ':';
	$str = array();
	$lastOrient = 'o';
	$n = count($helixPositions);
	for ($i = 0;$i < $n;$i+= 2) {
	    $orientString = '';
	    
	    if ($helixPrediction && strlen($helixPrediction) >= $helixPositions[$i] - 2) {
		$orient = $helixPrediction{$helixPositions[$i] - 2};
		
		if ($orient == $lastOrient) $orientString = $orient . $orientSep;
		$lastOrient = $orient;
	    }
	    $str[] = $orientString . $helixPositions[$i] . $posSep . $helixPositions[$i + 1];
	}
	return implode($pairSep, $str);
    }
    
    function format($value) {

	
	if ($value < - 1) return ("<i>" . sprintf("%.3f", $value) . "</i>");
	
	if ($value > 1) return ("<b>" . sprintf("%.3f", $value) . "</b>");
	return (sprintf("%.3f", $value));
    }
    
    function _drawResults($oHCP, $content = '') {


	// TODO: cleaner coding!!!
	
	if (isset($this->example) && $this->example && $this->aHCP != NULL) {
	    $aResultImagemap = array();
	    $aImageFile = array();
	    foreach($this->aHCP as $c => $hcp) {
		$aHelixImage[$c] = new helixImage();
		$aHelixImage[$c]->init($hcp);
		$aHelixImage[$c]->drawImg();
		$aHelixImage[$c]->createMap('tt_map-' . $c);
		imagejpeg($aHelixImage[$c]->img, $this->imageFile . $c . '.jpg', 100);
		$GLOBALS['jsVARS']['aImagesToLoad'][] = $this->imageFile . $c . '.jpg';
		$aResultImagemap[$c] = $aHelixImage[$c]->resultImagemap;
		$aImageFile[$c] = strtr($this->imageFile . $c . '.jpg', '\\', '/');
	    }
	    $this->smarty->assign('aResultImagemap', $aResultImagemap);
	    $this->smarty->assign('aImageFile', $aImageFile);
	}

	// TODO: cleaner coding!!!
	
	if (isset($this->example) && $this->example && $this->oHCP2 != NULL) {
	    $oHelixImage2 = new helixImage();
	    $oHelixImage2->init($this->oHCP2);
	    $oHelixImage2->drawImg();
	    $oHelixImage2->createMap('tt_map2');
	    imagejpeg($oHelixImage2->img, $this->imageFile . '.jpg', 100);
	    $GLOBALS['jsVARS']['aImagesToLoad'][] = $this->imageFile . '.jpg';
	    $this->smarty->assign('resultImagemap2', $oHelixImage2->resultImagemap);
	    $this->smarty->assign('imageFile2', strtr($this->imageFile . '.jpg', '\\', '/'));
	}
	$oHelixImage = new helixImage();
	$oHelixImage->init($oHCP);
	$oHelixImage->drawImg();
	$oHelixImage->createMap('tt_map');
	imagejpeg($oHelixImage->img, $this->imageFile, 100);
	
	if ($oHelixImage->imgHighRes) imagejpeg($oHelixImage->imgHighRes, $this->imageFile . 'highres.jpg', 100);
	$GLOBALS['jsVARS']['aImagesToLoad'][] = $this->imageFile;
	$this->smarty->assign('resultImagemap', $oHelixImage->resultImagemap);
	$membran_sections = count($oHCP->helixPos);
	$this->smarty->assign('matType', $this->matType);
	$this->smarty->assign('optLevel', $this->optimizationLevel);
	$this->smarty->assign('countMembranSections', $membran_sections / 2);
	$this->smarty->assign('helixLocations', $this->viewHelixLocations($oHCP));
	$this->smarty->assign('helixHmmtop', $oHCP->status('helixHmmtop'));
	$this->smarty->assign('imageFile', strtr($this->imageFile, '\\', '/'));
	
	if($oHCP->status('helixHmmtop')) $this->log->write('Note of caution: the transmembrane helix sections were automatically predicted using HMMTOP.',SIMPLELOG_WARNING, SIMPLELOG_USER);
	
	if ($oHelixImage->imgHighRes) $this->smarty->assign('imageFileHighRes', strtr($this->imageFile . 'highres.jpg', '\\', '/'));
	
	if ($this->useCons && $oHCP->hmmerStatus()) {
	    
	    if ($oHCP->foundPfamDomains != array()) {
		$this->smarty->assign('pfamDomains', $oHCP->foundPfamDomains);
	    } else {
		$this->log->write("No useable Pfam domains found.", SIMPLELOG_WARNING, SIMPLELOG_USER);
	    }
	}
	
	if ($membran_sections == 0) {
	    $membran_helix_seq[] = $oHCP->seq;
	    $this->log->write("No transmembran
      helices were found. Calculation was executed by the entire
      sequence.", SIMPLELOG_WARNING, SIMPLELOG_USER);
	    return;
	}
	list($conserved, $prediction) = $this->getResultStrings($oHCP);
	write_results($this->resultFile, $oHCP->helixPrediction, $prediction, $oHCP->seq, $conserved);
	$this->smarty->assign('resultFile', strtr($this->resultFile, '\\', '/'));
	
	if ($this->chainName){
	    $prediction = array($this->chainName => $prediction);
	    $helixPos = array($this->chainName => $oHCP->helixPos);
	}else{
	    $helixPos = $oHCP->helixPos;
	}
	write_pymol($this->pymolFile, $prediction,FALSE,$helixPos);
	$this->smarty->assign('pymolFile', strtr($this->pymolFile, '\\', '/'));

	// TODO: cleaner coding!!!
	
	if (isset($this->example) && $this->example && $this->oHCP2 != NULL) {
	    list($conserved2, $prediction2) = $this->getResultStrings($this->oHCP2);
	    write_results($this->resultFile . '.dat', $this->oHCP2->helixPrediction, $prediction2, $this->oHCP2->seq, $conserved2);
	    $this->smarty->assign('resultFile2', strtr($this->resultFile . '.dat', '\\', '/'));
	    write_pymol($this->pymolFile . '.py', $prediction2);
	    $this->smarty->assign('pymolFile2', strtr($this->pymolFile . '.py', '\\', '/'));
	    $prediction3 = '-';
	    $n = strlen($conserved2);
	    for ($i = 0;$i < $n;++$i) {
		
		if (array_key_exists($i + 1, $this->oHCP2->curatedData)) {
		    $data = $this->oHCP2->curatedData[$i + 1];
		    $type = $this->oHCP2->decideCurContact($data);
		    $prediction3.= $type ? strtoupper($type) : '-';
		} else {
		    $prediction3.= '-';
		}
	    }
	    write_pymol($this->pymolFile . '.py.py', $prediction3);
	    $this->smarty->assign('pymolFile3', strtr($this->pymolFile . '.py.py', '\\', '/'));
	}
	
	if (isset($this->example) && $this->example && $this->aHCP != NULL) {
	    $aPred = array();
	    $aCurPred = array();
	    foreach($this->aHCP as $c => $hcp) {
		list($con, $pred) = $this->getResultStrings($hcp);
		$aPred[$c] = $pred;
		$curPred = '';
		$n = strlen($con);
		for ($i = 0;$i < $n;++$i) {
		    
		    if (array_key_exists($i + 1, $hcp->curatedData)) {
			$data = $hcp->curatedData[$i + 1];
			
			if ($data['I/A'] == '1') {
			    $type = $hcp->decideCurContact($data);
			    $curPred.= $type ? strtoupper($type) : '-';
			} else {
			    $curPred.= '-';
			}
		    } else {
			$curPred.= '-';
		    }
		}
		$aCurPred[$c] = $curPred;
	    }
	    write_pymol($this->pymolFile . 'allchains.py', $aPred, $aCurPred);
	    $this->smarty->assign('pymolFileAllchains', strtr($this->pymolFile . 'allchains.py', '\\', '/'));
	    write_pymol($this->pymolFile . 'curchains.py', $aCurPred, $aPred);
	    $this->smarty->assign('pymolFileCurchains', strtr($this->pymolFile . 'curchains.py', '\\', '/'));
	}
	$content.= @$html_output;
	return $content;
    }
    
    function getResultStrings($oHCP) {

	$results = array();
	$seq_counter = 1;
	$k = 1;
	$erg = '';
	$n = count($oHCP->helixPos) - 1;
	for ($i = 0;$i < $n;$i+= 2) {
	    $m = $oHCP->helixPos[$i + 1];
	    for ($j = $oHCP->helixPos[$i] - 1;$j < $m;++$j) {
		list($hel, $mem, $wat) = $oHCP->predictAll($j);
		$erg.= $oHCP->doScoring($hel, $mem, $wat);
	    }
	    $results[] = $erg;
	    $erg = "";
	}
	$my_line = $oHCP->seq;
	$k = 0;
	$n = count(@$oHCP->helixPos) - 1;
	for ($l = 0;$l < $n;$l+= 2) {
	    $my_line = substr_replace($my_line, $results[$k], $oHCP->helixPos[$l] - 1, $oHCP->helixPos[$l + 1] - $oHCP->helixPos[$l] + 1);
	    $k++;
	}
	$conserved = $oHCP->seq;
	$n = strlen($conserved);
	for ($i = 0;$i < $n;$i+= 1) {
	    $conserved{$i} = $oHCP->consLevel($oHCP->search_conserved($i + 1));
	}
	$my_line = ereg_replace("[A-Z]", "-", $my_line);
	$my_line = strtoupper($my_line);
	return array(
	    $conserved,
	    $my_line
	);
    }
    
    function viewHelixLocations($oHCP) {

	$array_counter = 0;
	$seq_counter = 1;
	$max_stellen = ceil(log10(strlen($oHCP->seq)));
	$content = '<pre><font size="-2">' . ($max_stellen > 0 ? str_repeat("&nbsp;", $max_stellen - 1) : '') . "1&nbsp;&nbsp;";
	for ($i = 0, $link = FALSE;$i < strlen($oHCP->seq);$i++) {
	    
	    if ($i == @$oHCP->helixPos[$array_counter - 1] - 1 && $array_counter % 2 != 0) {
		$content.= "<a href=\"#seq$seq_counter\"><font color=blue>";
		$seq_counter++;
		$array_counter++;
		$link = TRUE;
	    } else 
	    if ($i == @$oHCP->helixPos[$array_counter - 1]) {
		$content.= "</font>" . ($link ? "</a>" : "");
		$array_counter++;
		$link = FALSE;
	    }
	    
	    if ($i % 40 == 0 && $i != 0) {
		
		if ($link) {
		    $content.= "</font></a>";
		}
		$stellen = ceil(log10($i + 1));
		$content.= '<font
	size="-2">' . "&nbsp;&nbsp;" . str_repeat("&nbsp;", $max_stellen - $stellen) . $i . '</font>';
		$content.= "<br/>";
		
		if ($i < strlen($oHCP->seq)) {
		    $stellen = ceil(log10($i + 2));
		    $content.= '<font
	  size="-2">' . str_repeat("&nbsp;", $max_stellen - $stellen) . ($i + 1) . "&nbsp;&nbsp;" . '</font>';
		}
		
		if ($link) {
		    $content.= "<a href=\"#seq" . ($seq_counter - 1) . "\"><font color=blue>";
		}
	    }
	    $content.= $oHCP->seq{$i};
	}
	$content.= "</pre>";
	return $content;
    }
}
?>
