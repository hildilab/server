<?php

include_once("lib.php");
include_once("image_lib.php");
include_once("class_helixContactPrediction.php");
include_once("class_proteinLib.php");


class helixImage{

  var $img;
  var $imgHighRes = FALSE;
  var $map;
  var $resultImagemap;

  var $seq;
  var $all_domains;
  var $curatedData;

  var $outer_left_margin;
  var $outer_right_margin;
  var $outer_top_margin;
  var $outer_bottom_margin;
  var $top_margin;
  var $bottom_margin;
  var $left_margin;
  var $right_margin;
  var $padding;
  var $font_height;
  var $font_width;
  var $cyl_width;
  var $cyl_height;
  
  var $mult;

  var $mat_membrane;
  var $mat_helix;
  var $mat_water;

  var $tc;

  var $helixOrientationUsed = FALSE;

  // $oHelixContactPrediction
  // $post_seq,$pos,$pred,$all_domains,$post_mat,$optimizeFor,$optimizationLevel
  function init(&$oHelixContactPrediction){
    $this->log =& simpleLog::getInstance();

    $this->oHCP =& $oHelixContactPrediction;

    $this->seq = $this->oHCP->seq;
    $this->pType = $this->oHCP->pType;
    $this->optimizeFor = $this->oHCP->optimizeFor;
    $this->optimizationLevel = $this->oHCP->optimizationLevel;

    $this->pos = $this->oHCP->helixPos;
    $this->pred = $this->oHCP->helixPrediction;
    $this->all_domains = $this->oHCP->pfamDomains;
    $this->curatedData = $this->oHCP->curatedData;

    $this->mat_helix = $this->oHCP->mat_helix;
    $this->mat_membrane = $this->oHCP->mat_membrane;
    $this->mat_water = $this->oHCP->mat_water;

    /*
    switch($this->pType){
    case 'coil':
      $this->mat_helix=readMatrix("./mat/coil_helix.txl"); 
      $this->mat_membrane=readMatrix("./mat/coil_membran.txl");
      $this->mat_water=readMatrix("./mat/coil_water.txl");
      break;
    case 'channel':
      $this->mat_helix=readMatrix("./mat/gate_helix.txl");
      $this->mat_membrane=readMatrix("./mat/gate_membran.txl");
      $this->mat_water=readMatrix("./mat/gate_water.txl");
      break;
    }
    */
    if(defined('ARM')){
      ini_set("memory_limit","64M");
    }else{
      @ini_set("memory_limit","256M");
    }
    if((int)@ini_get("memory_limit") >= 256){
      $this->imgHighRes = TRUE;
      $mult = 8;
    }else{
      $mult = 2;
    }

    $this->initDimensions($mult);
    $this->initImg();

  }


  function initDimensions($mult=2){

    $this->outer_left_margin = 45*$mult;
    $this->outer_right_margin = 15*$mult;
    $this->outer_top_margin = 60*$mult;
    $this->outer_bottom_margin = $this->outer_top_margin;
    $this->top_margin = 10*$mult;
    $this->bottom_margin = $this->top_margin;
    $this->left_margin = 25*$mult;
    $this->right_margin = $this->left_margin;
    $this->padding = 5*$mult;
    $this->font_height = 12*$mult;
    $this->font_width = 7*$mult;
    $this->cyl_width = 30*$mult;
    $this->cyl_height = 15*$mult;

    $this->mult = $mult;

    $this->membran_helix_seq = array();
    for($i=0;$i<count($this->pos);$i+=2) {
      $this->membran_helix_seq[] = substr($this->seq, $this->pos[$i]-1, 
					  $this->pos[$i+1]-$this->pos[$i]+1);	
    }

    $this->helix_height = array_reduce(array_map("strlen",$this->membran_helix_seq),"max");
    $this->helix_count = count($this->membran_helix_seq);
    
    $this->membran_beg = $this->outer_top_margin + $this->top_margin - 7*$this->padding;
    $this->membran_end = $this->helix_height * $this->font_height + ($this->helix_height-1) * $this->padding + $this->top_margin + $this->outer_top_margin + 6*$this->padding;

    $this->img_height = $this->helix_height * $this->font_height + ($this->helix_height-1) * $this->padding + $this->top_margin + $this->bottom_margin + $this->outer_bottom_margin + $this->outer_top_margin;

    $this->img_width = $this->helix_count * ($this->left_margin + $this->right_margin + $this->font_width) + $this->outer_left_margin + $this->outer_right_margin;
    
  }


  function initImg(){

    $this->img  = imagecreatetruecolor($this->img_width, $this->img_height);
    $this->thick = 3 * ($this->mult/2);

    imagesetthickness($this->img,$this->thick);
    //imageantialias($img,TRUE);
    $this->bgc = imagecolorallocate($this->img, 255, 255, 255);
    $this->tc = imagecolorallocate($this->img, 0, 0, 0);
    $this->lc = imagecolorallocate($this->img, 128, 128, 128);
    $this->sc = imagecolorallocate($this->img, 255, 0, 0);

    $this->domainColors = array();
    $n = count($this->all_domains);
    for($i = 0; $i < $n; ++$i){
      $c = 50 + floor(($i * 200) / $n);
      $this->domainColors[$this->all_domains[$i]['name']] = 
	imagecolorallocate($this->img, ($c*$i) % 255, ($c - 50) % 255, ($c*$i + 140) % 255);
    }

    $this->curatedColors['h'] = imagecolorallocate($this->img, 255, 0, 0);
    $this->curatedColors['m'] = imagecolorallocate($this->img, 0, 255, 0);
    $this->curatedColors['w'] = imagecolorallocate($this->img, 0, 0, 255);

    $this->red = imagecolorallocate($this->img, 255,69,0);
    $this->green = imagecolorallocate($this->img, 0, 43, 184); // actually blue
    $this->blue = imagecolorallocate($this->img, 30,144,255);

    $this->text_style_mem = dirname(__FILE__) . SEP . '..' . SEP . 'fonts' . SEP . "VeraMoBd.ttf";
    $this->text_style_pos = dirname(__FILE__) . SEP . '..' . SEP . 'fonts' . SEP . "VeraMoIt.ttf";

  }





  function drawHelixArc($helixNumber,$xPos){
    $i = $helixNumber;
    $d = ($this->left_margin+$this->right_margin+$this->font_width+2);
    $x = $xPos;

    if($this->pos[2*$i]-2 >= 0 && strtolower($this->pred{$this->pos[2*$i]-2}) == 'o'){
      $this->helixOrientationUsed = TRUE;
      imageSmoothArc($this->img,$x-$d/2+$this->font_width/2+1, $this->membran_beg, $d, $d,
		     array(128,128,128),0,M_PI/2);
      imageSmoothArc($this->img,$x-$d/2+$this->font_width/2+1, $this->membran_beg, 
		     $d-2*$this->thick, $d-2*$this->thick,
		     array(255,255,255),0,M_PI/2);
      //imagearc($img,$x-$d/2+$font_width/2+1, $membran_beg, $d, $d, 270, 0, $lc);
    }
    if($this->pos[2*$i]-2 >= 0 && strtolower($this->pred{$this->pos[2*$i]-2}) == 'i'){
      $this->helixOrientationUsed = TRUE;
      imageSmoothArc($this->img,$x+$d/2+$this->font_width/2-1, $this->membran_beg, $d, $d,
		     array(128,128,128),M_PI/2,M_PI);
      imageSmoothArc($this->img,$x+$d/2+$this->font_width/2-1, $this->membran_beg, 
		     $d-2*$this->thick, $d-2*$this->thick,
		     array(255,255,255),M_PI/2,M_PI);
      //imagearc($img,$x+$d/2+$font_width/2-1, $membran_beg, $d, $d, 180, 270, $lc);
    }
    if($this->pos[2*$i]-2 >= 0 && strtolower($this->pred{$this->pos[2*$i+1]}) == 'o'){
      $this->helixOrientationUsed = TRUE;
      imageSmoothArc($this->img,$x-$d/2+$this->font_width/2+1, $this->membran_end, $d, $d,
		     array(128,128,128),M_PI+M_PI/2,2*M_PI);
      imageSmoothArc($this->img,$x-$d/2+$this->font_width/2+1, $this->membran_end, 
		     $d-2*$this->thick, $d-2*$this->thick,
		     array(255,255,255),M_PI+M_PI/2,2*M_PI);
      //imagearc($img,$x-$d/2+$font_width/2+1, $membran_end, $d, $d, 0, 90, $lc);
    }
    if($this->pos[2*$i]-2 >= 0 && strtolower($this->pred{$this->pos[2*$i+1]}) == 'i'){
      $this->helixOrientationUsed = TRUE;
      imageSmoothArc($this->img,$x+$d/2+$this->font_width/2-1, $this->membran_end, $d, $d,
		     array(128,128,128),M_PI, M_PI+M_PI/2);
      imageSmoothArc($this->img,$x+$d/2+$this->font_width/2-1, $this->membran_end, 
		     $d-2*$this->thick, $d-2*$this->thick,
		     array(255,255,255),M_PI, M_PI+M_PI/2);
      //imagearc($img,$x+$d/2+$font_width/2-1, $membran_end, $d, $d, 90, 180, $lc);
    }

  }

	
  function drawHelix($helixNumber){

    $i = $helixNumber;

    if($this->pos[2*$i]-2 >= 0 && strtolower($this->pred{$this->pos[2*$i]-2}) == 'i'){
      $out_pos = $this->pos[2*$i+1];
      $in_pos = $this->pos[2*$i];
      $hSeq = strrev($this->membran_helix_seq[$i]);
    }else{
      $out_pos = $this->pos[2*$i];
      $in_pos = $this->pos[2*$i+1];
      $hSeq = $this->membran_helix_seq[$i];
    }

    $rev = ($this->pos[2*$i]-2 >= 0 && strtolower($this->pred{$this->pos[2*$i]-2}) == 'i') ? TRUE : FALSE;
    $beg = $this->pos[2*$i]-1;
    $end = $this->pos[2*$i+1]-1;

    $y = $this->top_margin + $this->outer_top_margin;
    $x = $i * ($this->left_margin + $this->right_margin + $this->font_width) + 
      $this->left_margin + $this->outer_left_margin;
    
    $this->writeHelixString($hSeq,$i,$end,$beg,$rev,$x,$y);

    imagefttext($this->img, $this->font_height*(3/4), 0, $x - strlen($out_pos)*1.7*$this->padding, 
		$this->membran_beg+2*($this->padding)+2*$this->thick,
		$this->tc, $this->text_style_pos, $out_pos);
    //imagestring($img, 1, $x - 4*$padding, $membran_beg+$padding, $out_pos, $tc);

	
    imagefttext($this->img, $this->font_height*(3/4), 0, $x - strlen($in_pos)*1.7*$this->padding, 
		$this->membran_end-$this->padding,
		$this->tc, $this->text_style_pos, $in_pos);
    //imagestring($img, 1, $x - 4*$padding, $membran_end-2*$padding, $in_pos, $tc);

    $this->drawHelixArc($helixNumber,$x);

  }

	   
		   
  function drawImg(){
   
    imagefilledrectangle($this->img, 0, 0, $this->img_width, $this->img_height, $this->bgc);

    for($i = 0; $i < $this->helix_count; ++$i){
      $this->drawHelix($i);
    }

    if($this->helixOrientationUsed){
      imagefttext($this->img, $this->font_height, 0, 2*$this->padding, 
		  $this->membran_beg-2*($this->padding)+$this->thick,
		  $this->tc, $this->text_style_mem, 'OUT');
      //imagestring($img, 3, 2*$padding, $membran_beg-4*$padding, 'OUT', $tc);
      
      imagefttext($this->img, $this->font_height, 0, 2*$this->padding, 
		  $this->membran_end+4*($this->padding),
		  $this->tc, $this->text_style_mem, 'IN');
      //imagestring($img, 3, 2*$padding, $membran_end+1*$padding, 'IN', $tc);
      
      imagelinethick($this->img,0,$this->membran_beg,$this->img_width,
		     $this->membran_beg,$this->lc,$this->thick);
      imagelinethick($this->img,0,$this->membran_end,$this->img_width,
		     $this->membran_end,$this->lc,$this->thick);
    }

    if($this->imgHighRes) $this->imgHighRes = $this->resampleImg(1);
    $this->img = $this->resampleImg($this->mult);
  }


  function resampleImg($div){
    $img  = imagecreatetruecolor($this->img_width/$div, 
				  $this->img_height/$div);
    imagecopyresampled($img,$this->img,0,0,0,0,$this->img_width/$div,
		       $this->img_height/$div, $this->img_width, $this->img_height);

    return $img;
  }


  function predict($asNum,$matType){
    return $this->oHCP->predict($asNum, $matType);
  }

  function doScoring($hel, $mem, $wat, $cons=FALSE){
    return $this->oHCP->doScoring($hel, $mem, $wat, $cons);
  }

  function search_conserved($asNum){
    return $this->oHCP->search_conserved($asNum);
  }

  function formatConserved($dom){
    if(!$dom) return '-';

    $ret = array();
    foreach($dom as $name => $type) $ret[] = $name . '&nbsp;(' . $type . ')';
    return implode(', ', $ret);
  }

  function createMap($map_name){

    $outer_left_margin = $this->outer_left_margin/$this->mult;
    $outer_top_margin = $this->outer_top_margin/$this->mult;
    $right_margin = $this->right_margin/$this->mult;
    $left_margin = $this->left_margin/$this->mult;
    $top_margin = $this->top_margin/$this->mult;
    $padding = $this->padding/$this->mult;
    $font_height = $this->font_height/$this->mult;
    $font_width = $this->font_width/$this->mult;
    $cyl_width = $this->cyl_width/$this->mult;
    $cyl_height = $this->cyl_height/$this->mult;

    $p = proteinLib::getInstance();


    for($i = 0; $i < $this->helix_count; ++$i){

      $rev = ($this->pos[2*$i]-2 >= 0 && strtolower($this->pred{$this->pos[2*$i]-2}) == 'i') ? TRUE : FALSE;
      $beg = $this->pos[2*$i]-1;
      $end = $this->pos[2*$i+1]-1;

      $n = strlen($this->membran_helix_seq[$i]);
      $h_top_margin = $top_margin + $outer_top_margin;
      $h_left_margin = $i * ($left_margin + $right_margin + $font_width) + $left_margin + $outer_left_margin;

      for($j = 0; $j < $n; ++$j){

	$as = $rev ? ($end-$j) : ($beg+$j);
	
	$x = $h_left_margin;
	$y = $h_top_margin+($j*($font_height+$padding));

	$lox = $x-$cyl_width/2+$font_width/2;
	$loy = $y;
	$rux = $x+$font_width+$cyl_width/2-$font_width/2;
	$ruy = $y+$font_height+$font_height/2;

	$hel = $this->predict($as, 'h');
	$mem = $this->predict($as, 'm');
	$wat = $this->predict($as, 'w');

	$conserved = $this->search_conserved($as+1);
	$contact = $this->doScoring($hel, $mem, $wat, $conserved);
	$foo = array('h' => 'Helix',
		     'm' => 'Membran',
		     'w' => 'Water');
	$contact = array_key_exists($contact, $foo) ? $foo[$contact] : '';

	//$dom = $this->formatConserved($this->search_conserved($as+1));

	$cur = '';
	$dat = array();
	if(array_key_exists($as+1,$this->curatedData)){
	  $dat = $this->curatedData[$as+1];
	  $type = FALSE;
	  $elm = array();

	  foreach($dat as $k => $v) $elm[] = $k . ': ' . $v;
	  $cur = 'INFO:&nbsp;' . implode('&nbsp;|&nbsp;',$elm);
	}

	$this->resultImagemap[] = array('seqNr' => $i+1,
					'coords' => round($lox).','.round($loy).','.round($rux).','.round($ruy),
					'helixScore' => $hel,
					'membraneScore' => $mem,
					'waterScore' => $wat,
					'aaId' => $as+1,
					'aaName' => strtr(strtoupper($this->seq{$as}),$p->asDict3),
					'contact' => $contact,
					'pfamDom' => $conserved,
					'curated' => $dat,
					);
	      
      }      
    }
  }

  function ImageEllipseAA( &$img, $x, $y, $w, $h,$color,$segments=70)
  {
    $w=$w/2;
    $h=$h/2;
    $jump=2*M_PI/$segments;
    $oldx=$x+sin(-$jump)*$w;
    $oldy=$y+cos(-$jump)*$h;
    for($i=0;$i<2*(M_PI);$i+=$jump)
      {
	$newx=$x+sin($i)*$w;
	$newy=$y+cos($i)*$h;
	ImageLine($img,$newx,$newy,$oldx,$oldy,$color);
	$oldx=$newx;
	$oldy=$newy;
      }
  }


  function writeHelixString($str,$helix_nr,$end,$beg,$rev,$left_margin,$top_margin){

    //imageantialias($img,TRUE);

    $n = strlen($str);

    imageSmoothArc($this->img,$left_margin+($this->font_width/2), 
		   $top_margin-$this->font_height,
		   $this->cyl_width+$this->thick/$this->mult,$this->cyl_height+$this->thick,
		   array(128,128,128),0,2*M_PI);
    imageSmoothArc($this->img,$left_margin+($this->font_width/2), 
		   $top_margin-$this->font_height,
		   $this->cyl_width-2*$this->thick,$this->cyl_height-$this->thick,
		   array(255,255,255),0,2*M_PI);
    //   ImageEllipseAA($img,$left_margin+$font_width/2,
    // 	       $top_margin-$font_height,
    // 		 $cyl_width,$cyl_height,$lc,1000);
    //   imageellipse($img,$left_margin+$font_width/2,
    // 	       $top_margin-$font_height,
    // 	       $cyl_width,$cyl_height,$lc);

    imagelinethick($this->img,$left_margin+$this->font_width/2-$this->cyl_width/2,
		   $top_margin-$this->cyl_height/2-$this->font_height/4,
		   $left_margin+$this->font_width/2-$this->cyl_width/2,
		   $top_margin+($n*($this->font_height+$this->padding)),
		   $this->lc,$this->thick);

    imagelinethick($this->img,$left_margin+$this->font_width/2+$this->cyl_width/2,
		   $top_margin-$this->cyl_height/2-$this->font_height/4,
		   $left_margin+$this->font_width/2+$this->cyl_width/2,
		   $top_margin+($n*($this->font_height+$this->padding)),
		   $this->lc,$this->thick);

    imageSmoothArc($this->img,$left_margin+($this->font_width/2), 
		   $top_margin+($n*($this->font_height+$this->padding)),
		   $this->cyl_width+$this->thick/$this->mult,$this->cyl_height+$this->thick,
		   array(128,128,128),M_PI,2*M_PI);
    imageSmoothArc($this->img,$left_margin+($this->font_width/2), 
		   $top_margin+($n*($this->font_height+$this->padding)),
		   $this->cyl_width-2*$this->thick,$this->cyl_height-$this->thick,
		   array(255,255,255),0,2*M_PI);
    //   imagearc($img,$left_margin+$font_width/2, 
    //  	   $top_margin+($n*($font_height+$padding)) ,
    //  	   $cyl_width,$cyl_height,0,180,$lc);

    imagelinethick($this->img, $left_margin+$this->font_width/2,
		   $top_margin-$this->font_height,
		   $left_margin+$this->font_width/2,
		   $this->membran_beg,
		   $this->lc,$this->thick);

    imagelinethick($this->img, $left_margin+$this->font_width/2,
		   $top_margin+($n*($this->font_height+$this->padding))+$this->cyl_height/2+$this->thick,
		   $left_margin+$this->font_width/2,
		   $this->membran_end,
		   $this->lc,$this->thick);


    for($i = 0; $i < $n; ++$i){

      $as = $rev ? ($end-$i) : ($beg+$i);

      $dom = $this->search_conserved($as+1);
      //$style = ($dom == '') ? 4 : 5;
      //$style = ($dom == '') ? "./VeraMono.ttf" : "./VeraMoBI.ttf";

      $x = $left_margin;
      $y = $top_margin+($i*($this->font_height+$this->padding));

      //     if($dom != ''){
      //       imagefilledrectangle($img, $x-$cyl_width/2+$font_width/2, 
      // 			   $y+$font_height/2-$padding/2, 
      // 			   $x+$font_width+$cyl_width/2-$font_width/2,
      // 			   $y+$font_height+$font_height/2+$padding/2, $lc);
      //     }

      $hel = $this->predict($as, 'h');
      $mem = $this->predict($as, 'm');
      $wat = $this->predict($as, 'w');

      $conserved = $this->search_conserved($as+1);
      $contact = $this->doScoring($hel, $mem, $wat, $conserved);

      $style = dirname(__FILE__) . SEP . '..' . SEP . 'fonts' . SEP . (($contact != 'u') ? "VeraMoBd.ttf" : "VeraMono.ttf");

      switch($contact){
      case 'h':
	$col = $this->red;
	break;
      case 'm':
	$col = $this->green;
	break;
      case 'w':
	$col = $this->blue;
	break;
      default:
	$col = $this->tc;
      }

      imagefttext($this->img, $this->font_height, 0,
		  $x, $y+$this->font_height+$this->padding,
		  $col, $style, $str{$i});

      //$this->drawTextBox($this->font_height,0,$style,$contact);
      //imagestring($img, $style, $x, $y, $str{$i}, $col);

      //debug($conserved);
      $j = 0;
      foreach($conserved as $name => $type){

	$dia = $this->font_height/2;
	if($type == '+'){
	  $dia *= 0.7;
	}elseif(is_upper($type)){
	  $dia *= 1.4;
	}

	$shift = $dia * 0.8 * $j;

	imagefilledellipse($this->img,
			   ($x-$this->cyl_width/2+$this->font_width/2) - $shift,
			    $y+$this->font_height,
			    $dia,$dia,
			    $this->domainColors[$name]);

	++$j;
      }

      if(array_key_exists($as+1,$this->curatedData)){
	$dat = $this->curatedData[$as+1];
	$type = $this->oHCP->decideCurContact($dat);
	$dia = $this->font_height/2;

	if($type){
	  imagefilledellipse($this->img,
			     ($x+$this->cyl_width/2+$this->font_width/2),
			     $y+$this->font_height,
			     $dia,$dia,
			     $this->curatedColors[$type]);
	}
      }

    }

  }

  function drawTextBox($font_size, $font_angle, $font_file, $text) {
    $box = imagettfbbox($font_size, $font_angle, $font_file, $text);

    $min_x = min(array($box[0], $box[2], $box[4], $box[6]));
    $max_x = max(array($box[0], $box[2], $box[4], $box[6]));
    $min_y = min(array($box[1], $box[3], $box[5], $box[7]));
    $max_y = max(array($box[1], $box[3], $box[5], $box[7]));

    imagerectangle($this->img,$box[6],$box[7],$box[2],$box[3],$this->tc);
  }

  function format ($value) {
    if ($value < -1) return ("<i>".sprintf("%.3f",$value)."</i>");
    if ($value >  1) return ("<b>".sprintf("%.3f",$value)."</b>");
    return (sprintf("%.3f",$value)); 
  }

}

?>