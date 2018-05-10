<?php

include_once("src/lib.php");

class site{

  var $smarty;

  var $pages = array("home", 
		     "helix",
		     "abstract",
		     "methods",
		     'references',
		     "FAQ",
		     'links',
		     );

  var $subpages = array("methods" => array('general',
					   'learning',
					   'databases',
					   'prediction',
					   ),
			);

  function init(){
    
    include_once("src/class_smartyRhythm.php");

    $this->smarty = new smartyRhythm();
    if(defined('DEBUG')) $this->smarty->debugging = true;
    $this->smarty->force_compile = true;

    $GLOBALS['extraCSS'] = array();
    $GLOBALS['styleCSS'] = array();
    $GLOBALS['extraJS'] = array();
    $GLOBALS['jsVARS'] = array();

    $subsite = '';
    $req_site = _GET('site');
    if (!in_array($req_site, $this->pages)) $req_site = $this->pages[0];
    $this->smarty->assign('site',$req_site);
    
    if($req_site == 'helix'){

      include_once('src/class_helix.php');
      $oHelixSite = new helix();
      $oHelixSite->init($this);

      if(defined('DEBUG')) $this->smarty->assign('log',$oHelixSite->log->format());

    }elseif($req_site == 'methods'){

      $subsite = _GET('sub');
      if (!in_array($subsite, $this->subpages['methods'])) $subsite = $this->subpages['methods'][0];
      $this->smarty->assign('subpageTplFile','methods_'.$subsite.'.tpl');

      if($subsite=='learning') $this->smarty->assign('propMatrices',$this->getPropMats());


    }elseif($req_site == 'references'){
      $ref = _GET('ref');

      if($ref){
	$GLOBALS['styleCSS'][] = '#' . $ref . ' { background-color: #DDCCCC; }';
	$this->smarty->assign('ref',$ref);
      }
    }

    $this->smarty->assign('subsite',$subsite);

    $GLOBALS['jsVARS']['aImagesToLoad'][] = 'img/helpbubble.png';
    $GLOBALS['jsVARS']['aImagesToLoad'][] = 'img/1.jpg';
    
    $this->smarty->assign('extraCSS',$GLOBALS['extraCSS']);
    $this->smarty->assign('styleCSS',$GLOBALS['styleCSS']);
    $this->smarty->assign('extraJS',$GLOBALS['extraJS']);
    
    // works!
    //$GLOBALS['jsVARS']['GET'] = _GET();
    //$GLOBALS['jsVARS']['POST'] = _POST();

    $jsVARS = array();
    foreach($GLOBALS['jsVARS'] as $k => $v) $jsVARS[$k] = json_encode($v);
    $this->smarty->assign('jsVARS',$jsVARS);

    $this->smarty->assign('pageTplFile',$req_site.'.tpl');
    $this->smarty->display('index.tpl');

  }


  function getPropMats(){
    include_once("src/file_lib.php");
    $propMatrices = array();

    $mChannelHelix = readMatrix("./mat/gate8_helix.mat");
    $m = floor(count(current($mChannelHelix))/2);
    $propMatrices[] = array('name' => 'Channel, Helix-Helix Contact',
			    'propMatrix' => $mChannelHelix,
			    'colNames' => seq(-$m,$m),
			    'mark' => array($m-4,$m,$m+4), //mark positions -4, 0, 4
			    );

    $mChannelMembrane = readMatrix("./mat/gate8_membran.mat");
    $m = floor(count(current($mChannelMembrane))/2);
    $propMatrices[] = array('name' => 'Channel, Helix-Membrane Contact',
			    'propMatrix' => $mChannelMembrane,
			    'colNames' => seq(-$m,$m),
			    'mark' => array($m-4,$m,$m+4), //mark positions -4, 0, 4
			    );

    $mCoilHelix= readMatrix("./mat/coil8_helix.mat");
    $m = floor(count(current($mCoilHelix))/2);
    $propMatrices[] = array('name' => 'Membrane-coil, Helix-Helix Contact',
			    'propMatrix' => $mCoilHelix,
			    'colNames' => seq(-$m,$m),
			    'mark' => array($m-3,$m,$m+4),  //mark positions -3, 0, 4
			    );

    $mCoilMembrane = readMatrix("./mat/coil8_membran.mat");
    $m = floor(count(current($mCoilMembrane))/2);
    $propMatrices[] = array('name' => 'Membrane-coil, Helix-Membrane Contact',
			    'propMatrix' => $mCoilMembrane,
			    'colNames' => seq(-$m,$m),
			    'mark' => array($m-3,$m,$m+4),  //mark positions -3, 0, 4
			    );
    
    return($propMatrices);
  }

}

?> 

