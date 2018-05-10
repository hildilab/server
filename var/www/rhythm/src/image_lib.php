<?php

include_once("lib.php");

function LoadJpeg($imgname)
{
  $im = @imagecreatefromjpeg($imgname); /* Attempt to open */
  // $im = @imagecreatefromjpeg('../../media/wimmelbild/org_wimmelbild_test.jpg');
  if (!$im) { /* See if it failed */
    $im  = imagecreatetruecolor(150, 30); /* Create a black image */
    $bgc = imagecolorallocate($im, 255, 255, 255);
    $tc  = imagecolorallocate($im, 0, 0, 0);
    imagefilledrectangle($im, 0, 0, 150, 30, $bgc);
    /* Output an errmsg */
    imagestring($im, 1, 5, 5, "Error loading $imgname", $tc);
  }
  return $im;
}

function image_resize($img,$factor){
  $x = imagesx($img);
  $y = imagesy($img);
  $nx = $x*$factor;
  $ny = $y*$factor;
  $dest = imagecreatetruecolor($nx,$ny);
  //imagecopyresized($dest,$img,0,0,0,0,$nx,$ny,$x,$y);
  imagecopyresampled($dest,$img,0,0,0,0,$nx,$ny,$x,$y);
  return($dest);
}

function image_transform($img,$nx,$ny){
  $x = imagesx($img);
  $y = imagesy($img);
  $dest = imagecreatetruecolor($nx,$ny);

  //imagecopyresized($dest,$img,0,0,0,0,$nx,$ny,$x,$y);
  imagecopyresampled($dest,$img,0,0,0,0,$nx,$ny,$x,$y);
  return($dest);
}

function image_filter($img,$filter){
  $x = imagesx($img);
  $y = imagesy($img);
  imageantialias($img,TRUE);
  $img_g = imagecreatetruecolor($x,$y);
  if(SLOW_SERVER){ 
    imageantialias($img_g,FALSE); 
  }else{ 
    imageantialias($img_g,TRUE);
  }
  imagecopy($img_g,$img,0,0,0,0,$x,$y);
  call_user_func_array('imagefilter',array_merge(array($img_g),$filter));
  //  imagefilter($img_g,$filter);
  return($img_g);
}

function imageSmoothArc( &$img, $cx, $cy, $w, $h, $color, $start, $stop) {
  // Written from scratch by Ulrich Mierendorff, 06/2006
  $fillColor = imageColorExactAlpha( $img, $color[0], $color[1], $color[2], 0 );
  $w /= 2;
  $h /= 2;
  $cdx = $w * cos(M_PI/4);
  $cdy = $h * sin(M_PI/4);

  $xStart = $w * cos($start);
  $yStart = $h * sin($start);
  $xStop = $w * cos(min(M_PI,$stop));
  $yStop = $h * sin(min(M_PI,$stop));
  if ( $start < M_PI/2 ) {
    $yy = 0;
    for ( $x = 0; $x <= $xStart; $x += 1 ) {
      if ( $x < $xStop ) {
	$y1 = $x/$xStop*$yStop;
      } else {
	$y1 = $h * sqrt( 1 - pow( $x,2 ) / pow( $w,2 ) );
      }
      $y2 = $x/$xStart*$yStart;
      $d1 = $y1 - floor($y1);
      $d2 = $y2 - floor($y2);
      $y1 = floor($y1);
      $y2 = floor($y2);
      imageLine($img, $cx + $x, $cy - $y1, $cx + $x, $cy - $y2, $fillColor);
      $diffColor = imageColorExactAlpha( $img, $color[0], $color[1], $color[2], 100 - $d1*100 );
      imageSetPixel($img, $cx + $x, $cy - $y1 - 1, $diffColor);
      $diffColor = imageColorExactAlpha( $img, $color[0], $color[1], $color[2], $d2*100 );
      imageSetPixel($img, $cx + $x, $cy - $y2 + 1, $diffColor);
      for ( $yy; $yy <= $y1; $yy += 1 ) {
	if ( $yy < $yStart ) {
	  $x1 = $yy/$yStart*$xStart;
	} else {
	  $x1 = $w * sqrt( 1 - pow( $yy,2 ) / pow( $h,2 ) );
	}
	$d1 = $x1 - floor($x1);
	$x1 = floor($x1);
	$diffColor = imageColorExactAlpha( $img, $color[0], $color[1], $color[2], 100 - $d1*100 );
	imageSetPixel($img, $cx + $x1 + 1, $cy - $yy, $diffColor);
	if ($stop < M_PI/2) {
	  $x2 = $yy/$yStop*$xStop;
	  $d2 = $x2 - floor($x2);
	  $x2 = floor($x2);
	  $diffColor = imageColorExactAlpha( $img, $color[0], $color[1], $color[2], $d2*100 );
	  imageSetPixel($img, $cx + $x2, $cy - $yy, $diffColor);
	}
      }
    }
  }
  if ( $start < M_PI && $stop > M_PI/2 ) {
    $yy = 0;
    for ( $x = 0; $x >= $xStop; $x -= 1 ) {
      if ( $x > $xStart ) {
	$y1 = $x/$xStart*$yStart;
      } else {
	$y1 = $h * sqrt( 1 - pow( $x,2 ) / pow( $w,2 ) );
      }
      $y2 = $x/$xStop*$yStop;
      $d1 = $y1 - floor($y1);
      $d2 = $y2 - floor($y2);
      $y1 = floor($y1);
      $y2 = floor($y2);
      imageLine($img, $cx + $x, $cy - $y1, $cx + $x, $cy - $y2, $fillColor);
      $diffColor = imageColorExactAlpha( $img, $color[0], $color[1], $color[2], 100 - $d1*100 );
      imageSetPixel($img, $cx + $x, $cy - $y1 - 1, $diffColor);
      $diffColor = imageColorExactAlpha( $img, $color[0], $color[1], $color[2], $d2*100 );
      imageSetPixel($img, $cx + $x, $cy - $y2 + 1, $diffColor);
      for ( $yy; $yy <= $y1; $yy += 1 ) {
	if ( $yy < $yStop ) {
	  $x1 = -$yy/$yStop*$xStop;
	} else {
	  $x1 = $w * sqrt( 1 - pow( $yy,2 ) / pow( $h,2 ) );
	}
	$d1 = $x1 - floor($x1);
	$x1 = floor($x1);
	$diffColor = imageColorExactAlpha( $img, $color[0], $color[1], $color[2], 100 - $d1*100 );
	imageSetPixel($img, $cx - $x1 - 1, $cy - $yy, $diffColor);
	if ( $start > M_PI/2 ) {
	  $x2 = $yy/$yStart*$xStart;
	  $d2 = $x2 - floor($x2);
	  $x2 = floor($x2);
	  $diffColor = imageColorExactAlpha( $img, $color[0], $color[1], $color[2], $d2*100 );
	  imageSetPixel($img, $cx + $x2, $cy - $yy, $diffColor);
	}
      }
    }
  }

  $xStart = $w * cos(max(M_PI,$start));
  $yStart = $h * sin(max(M_PI,$start));
  $xStop = $w * cos($stop);
  $yStop = $h * sin($stop);
  if ( $start < 3*M_PI/2 && $stop > M_PI) {
    $yy = 0;
    for ( $x = 0; $x >= $xStart; $x -= 1 ) {
      if ( $x > $xStop) {
	$y1 = $x/$xStop*$yStop;
      } else {
	$y1 = -$h * sqrt( 1 - pow( $x,2 ) / pow( $w,2 ) );
      }
      $y2 = $x/$xStart*$yStart;
      $d1 = $y1 - floor($y1);
      $d2 = $y2 - floor($y2);
      $y1 = floor($y1);
      $y2 = floor($y2);
      imageLine($img, $cx + $x, $cy - $y1, $cx + $x, $cy - $y2, $fillColor);
      $diffColor = imageColorExactAlpha( $img, $color[0], $color[1], $color[2], $d1*100 );
      imageSetPixel($img, $cx + $x, $cy - $y1 + 1, $diffColor);
      $diffColor = imageColorExactAlpha( $img, $color[0], $color[1], $color[2], 100 - $d2*100 );
      imageSetPixel($img, $cx + $x, $cy - $y2 - 1, $diffColor);
      for ( $yy; $yy >= $y1; $yy -= 1 ) {
	if ( $yy > $yStart ) {
	  $x1 = -$yy/$yStart*$xStart;
	} else {
	  $x1 = $w * sqrt( 1 - pow( $yy,2 ) / pow( $h,2 ) );
	}
	$d1 = $x1 - floor($x1);
	$x1 = floor($x1);
	$diffColor = imageColorExactAlpha( $img, $color[0], $color[1], $color[2], 100 - $d1*100 );
	imageSetPixel($img, $cx - $x1 - 1, $cy - $yy, $diffColor);
	if ($stop < 3*M_PI/2) {
	  $x2 = $yy/$yStop*$xStop;
	  $d2 = $x2 - floor($x2);
	  $x2 = floor($x2);
	  $diffColor = imageColorExactAlpha( $img, $color[0], $color[1], $color[2], 100 - $d2*100 );
	  imageSetPixel($img, $cx + $x2 + 1, $cy - $yy, $diffColor);
	}
      }
    }

  }
  if ( $start < 2*M_PI && $stop > 3*M_PI/2 ) {
    $yy = 0;
    for ( $x = 0; $x <= $xStop; $x += 1 ) {
      if ( $x < $xStart )  {
	$y1 = $x/$xStart*$yStart;
      } else {
	$y1 = -$h * sqrt( 1 - pow( $x,2 ) / pow( $w,2 ) );
      }
      $y2 = $x/$xStop*$yStop;
      $d1 = $y1 - floor($y1);
      $d2 = $y2 - floor($y2);
      $y1 = floor($y1);
      $y2 = floor($y2);
      imageLine($img, $cx + $x, $cy - $y1, $cx + $x, $cy - $y2, $fillColor);
      $diffColor = imageColorExactAlpha( $img, $color[0], $color[1], $color[2], $d1*100 );
      imageSetPixel($img, $cx + $x, $cy - $y1 + 1, $diffColor);
      $diffColor = imageColorExactAlpha( $img, $color[0], $color[1], $color[2], 100 - $d2*100 );
      imageSetPixel($img, $cx + $x, $cy - $y2 - 1, $diffColor);
      for ( $yy; $yy >= $y1; $yy -= 1 ) {
	if ( $yy > $yStop ) {
	  $x1 = $yy/$yStop*$xStop;
	} else {
	  $x1 = $w * sqrt( 1 - pow( $yy,2 ) / pow( $h,2 ) );
	}
	$d1 = $x1 - floor($x1);
	$x1 = floor($x1);
	$diffColor = imageColorExactAlpha( $img, $color[0], $color[1], $color[2], 100 - $d1*100 );
	imageSetPixel($img, $cx + $x1 + 1, $cy - $yy, $diffColor);
	if ( $start > 3*M_PI/2 ) {
	  $x2 = $yy/$yStart*$xStart;
	  $d2 = $x2 - floor($x2);
	  $x2 = floor($x2);
	  $diffColor = imageColorExactAlpha( $img, $color[0], $color[1], $color[2], $d2*100 );
	  imageSetPixel($img, $cx + $x2 , $cy - $yy, $diffColor);
	}
      }
    }
  }
}

function imagelinethick($image, $x1, $y1, $x2, $y2, $color, $thick = 1)
{
  /* this way it works well only for orthogonal lines
   imagesetthickness($image, $thick);
   return imageline($image, $x1, $y1, $x2, $y2, $color);
  */
  if ($thick == 1) {
    return imageline($image, $x1, $y1, $x2, $y2, $color);
  }
  $t = $thick / 2 - 0.5;
  if ($x1 == $x2 || $y1 == $y2) {
    return imagefilledrectangle($image, round(min($x1, $x2) - $t), round(min($y1, $y2) - $t), round(max($x1, $x2) + $t), round(max($y1, $y2) + $t), $color);
  }
  $k = ($y2 - $y1) / ($x2 - $x1); //y = kx + q
  $a = $t / sqrt(1 + pow($k, 2));
  $points = array(
		  round($x1 - (1+$k)*$a), round($y1 + (1-$k)*$a),
		  round($x1 - (1-$k)*$a), round($y1 - (1+$k)*$a),
		  round($x2 + (1+$k)*$a), round($y2 - (1-$k)*$a),
		  round($x2 + (1-$k)*$a), round($y2 + (1+$k)*$a),
		  );
  imagefilledpolygon($image, $points, 4, $color);
  return imagepolygon($image, $points, 4, $color);
}


function imagestringdown(&$image, $font, $x, $y, $s, $col)
{
  $width = imagesx($image);
  $height = imagesy($image);

  $text_image = imagecreate($width, $height);

  $white = imagecolorallocate ($text_image, 255, 255, 255);
  $black = imagecolorallocate ($text_image, 0, 0, 0); 

  $transparent_colour = $white;
  if ($col == $white)
    $transparent_color = $black;

  imagefill($text_image, $width, $height, $transparent_colour);
  imagecolortransparent($text_image, $transparent_colour);

  imagestringup($text_image, $font, ($width - $x), ($height - $y), $s, $col);
  imagerotate($text_image, 180.0, $transparent_colour);

  imagecopy($image, $text_image, 0, 0, 0, 0, $width, $height);
}


?>