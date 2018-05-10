<?php

  // enables debugging globally
  //define('DEBUG','DEBUG');

// offers precomputed examples containing curated information
  //define('EXAMPLES','EXAMPLES');


if(defined('DEBUG')){
  ini_set('display_errors','On');
  error_reporting(E_ALL);
 }
  
 
if( strtoupper(substr(PHP_OS, 0,3)) == 'WIN'){
  define("WIN",1);
}elseif( strtoupper(substr(PHP_OS, 0,6)) == 'DARWIN'){
  define("OSX",1);
}else{
  define("LINUX",1);
}

if( defined('LINUX') || defined('OSX') ){
  $uname_m;
  exec("uname -m", $uname_m);
  if( strtoupper(substr($uname_m[0], 0, 3)) == 'ARM' ){
    define('ARM',1);
  }elseif( substr($uname_m[0], -3) == '_64' ){
    define('64BIT',1);
  }else{
    define('32BIT',1);
  }
}

date_default_timezone_set('UTC');

set_include_path(dirname(__FILE__) . PATH_SEPARATOR . get_include_path());
set_include_path(dirname(__FILE__) . '/src' .PATH_SEPARATOR . get_include_path());

include_once("src/lib.php");

// dispatcher: ajax or normal mode
if(_GET('ajaxId')){
  include_once("src/class_ajax.php");
  $oAjax = new ajax;
  echo $oAjax->returnValue;
 }else{
  include_once("src/class_site.php");
  $oSite = new site;
  $oSite->init();
 }

?>

