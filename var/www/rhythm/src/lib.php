<?php

 // php4 compat
if (!function_exists('json_encode'))
{
  function json_encode($a=false)
  {
    if (is_null($a)) return 'null';
    if ($a === false) return 'false';
    if ($a === true) return 'true';
    if (is_scalar($a))
    {
      if (is_float($a))
      {
        // Always use "." for floats.
        return floatval(str_replace(",", ".", strval($a)));
      }

      if (is_string($a))
      {
        static $jsonReplaces = array(array("\\", "/", "\n", "\t", "\r", "\b", "\f", '"'), array('\\\\', '\\/', '\\n', '\\t', '\\r', '\\b', '\\f', '\"'));
        return '"' . str_replace($jsonReplaces[0], $jsonReplaces[1], $a) . '"';
      }
      else
        return $a;
    }
    $isList = true;
    for ($i = 0, reset($a); $i < count($a); $i++, next($a))
    {
      if (key($a) !== $i)
      {
        $isList = false;
        break;
      }
    }
    $result = array();
    if ($isList)
    {
      foreach ($a as $v) $result[] = json_encode($v);
      return '[' . join(',', $result) . ']';
    }
    else
    {
      foreach ($a as $k => $v) $result[] = json_encode($k).':'.json_encode($v);
      return '{' . join(',', $result) . '}';
    }
  }
}

  // php4 compat
if (!function_exists('array_combine')){
  function array_combine($arr1, $arr2) {
    $out = array();
    
    $arr1 = array_values($arr1);
    $arr2 = array_values($arr2);
    
    foreach($arr1 as $key1 => $value1) {
      $out[(string)$value1] = $arr2[$key1];
    }
    
    return $out;
  }
 }  

  // php4 compat
if (!function_exists('scandir')){
  function scandir($dir, $no_dots=FALSE) {
    
    $files = array();
    $dh  = @opendir($dir);
    if ($dh!=FALSE) {
      while (false !== ($filename = readdir($dh))) {
	$files[] = $filename;
      }
      
      if ($no_dots) {
	while(($ix = array_search('.',$files)) > -1)
	  unset($files[$ix]);
	while(($ix = array_search('..',$files)) > -1)
	  unset($files[$ix]);
      }
      
      sort($files);
       
    }
    return $files;
  }
}

function array_smart_map($callback) {
    // Initialization
    $args = func_get_args() ;
    array_shift($args) ; // suppressing the callback
    $result = array() ;
   
    // Validating parameters
    foreach($args as $key => $arg)
        if(is_array($arg)) {
            // the first array found gives the size of mapping and the keys that will be used for the resulting array
            if(!isset($size)) {
                $keys = array_keys($arg) ;
                $size = count($arg) ;
            // the others arrays must have the same dimension
            } elseif(count($arg) != $size) {
                return FALSE ;
            }
            // all keys are suppressed
            $args[$key] = array_values($arg) ;
        }
   
    // doing the callback thing
    if(!isset($size))
        // if no arrays were found, returns the result of the callback in an array
        $result[] = call_user_func_array($callback, $args) ;
    else
        for($i=0; $i<$size; $i++) {
            $column = array() ;
            foreach($args as $arg)
                $column[] = ( is_array($arg) ? $arg[$i] : $arg ) ;
            $result[$keys[$i]] = call_user_func_array($callback, $column) ;
        }
           
    return $result ;
   
}

function gcd($num1, $num2) {
   while ($num2 != 0){
     $t = $num1 % $num2;
     $num1 = $num2;
     $num2 = $t;
   }
   return $num1;
}

function lcd($array,$x) {
  if(!is_array($array)){
    $array = array($array);
  }
  
  $mod_sum = 0;
  
  for($int=1;$int < count($array);$int++) {               
    $modulus[$int] = ($array[0]*$x) % ($array[$int]);
    $mod_sum = $mod_sum + $modulus[$int];           
  }
  
  if (!$mod_sum) {
    return($array[0]*$x);
  } else {
    lcd($array,$x+1);
  }
}

function seq($from,$to,$step=1){
  $seq = array();
  for($i=$from; $i<=$to; $i+=$step) $seq[] = $i;
  return $seq;
}

function is_upper($input) {
    return ($input == strtoupper($input));
}

function is_lower($input) {
    return ($input == strtolower($input));
}

function trimExplode($delimiter,$str){
  $array = array();
  foreach(explode($delimiter,$str) as $k => $v) $array[$k] = trim($v);
  return($array);
}

function is_even($i){
  return(!($i&1));
}

function is_uneven($i){
  return($i&1);
}

function array_concat($a,$b){
  while(list(,$v)=each($b)) {
    $a[] = $v;
  }
  return $a;
}

function is_sorted($array,$direction='ASC'){
  list(,$current)=each($array);

  if($direction==='DESC'){
    while(list(,$next)=each($array)){
      if($current < $next) return FALSE;
      $current = $next;
    }

  }else{ // ASC

    while(list(,$next)=each($array)){
      if($current > $next) return FALSE;
      $current = $next;
    }
  }

  return TRUE;
}


/**
 * Wrap string by specify chars
 *
 * @param string $strForWrap
 * @param integer $maxLength
 * @param string $breakChar
 * @param array $wrapChars
 *
 * @author Ivan Chura
 * @since 21.04.2008
 * @return string
 **/
   
function wordwrapBySpecifyChars($strForWrap, $maxLength = 80, $breakChar = "\n", $wrapChars = array(",", ";" ))
{
  $newStr = null;
  $length_of_string = strlen($strForWrap);
       
  if ($length_of_string <= $maxLength)
    {
      return $strForWrap;
    }
           
  $count_of_string = 1;   
  $wait_new_line = false;
       
  for($i=0; $i<$length_of_string; $i++)
    {
      if ( $count_of_string*$maxLength == $i || $wait_new_line)
	{
               
	  if (in_array($strForWrap{$i}, $wrapChars ) )
	    {
	      $count_of_string ++;
                    
	      $newStr .= $strForWrap{$i}.$breakChar;
	      $wait_new_line = false;
	    }
	  else
	    {
	      $newStr .= $strForWrap{$i};
	      $wait_new_line = true;
	    }
	}
      else
	{
	  $newStr .= $strForWrap{$i};  
	}
            
    }
           
  return $newStr;
}

function random_str($numchar=16) {
  $str = "abcefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  $start = mt_rand(1, (strlen($str)-$numchar));
  $string = str_shuffle($str);
  $randstr = substr($string,$start,$numchar);
  return($randstr);
}

function view_array($array_in)  {
  if (is_array($array_in))        {
    $result='<table border="1" cellpadding="1" cellspacing="0" bgcolor="white">';
    if (!count($array_in))  {$result.= '<tr><td><font face="Verdana,Arial" size="1"><b>'.htmlspecialchars("EMPTY!").'</b></font></td></tr>';}
    while (list($key,$val)=each($array_in)) {
      $result.= '<tr><td valign="top"><font face="Verdana,Arial" size="1">'.htmlspecialchars((string)$key).'</font></td><td>';
      if (is_array($array_in[$key]))  {
	$result.=view_array($array_in[$key]);
      } else
	$result.= '<font face="Verdana,Arial" size="1" color="red">'.nl2br(htmlspecialchars((string)$val)).'<br /></font>';
      $result.= '</td></tr>';
    }
    $result.= '</table>';
  } else  {
    $result  = false;
  }
  return $result;
}


function debug($var){
  if(!isset($var)){
    echo '<pre>|DEBUG|</pre>';
  }elseif(is_bool($var)){
    echo '<pre>|<b>'.($var?'TRUE':'FALSE').'</b>|</pre>'; 
  }elseif(is_array($var) || is_object($var)){
    echo view_array($var);
  }else{
    echo '<pre>|'.$var.'|</pre>';
  }  
}

function _cleanUserInput($data){
  if(is_array($data)){
    foreach($data as $k => $v){
      $data[$k] = _cleanUserInput($v);
    }
    return $data;
  }
  return strip_tags(stripslashes($data));
}

function _POST($name=FALSE){
  if(!$name){
    return _cleanUserInput($_POST);
  }elseif(array_key_exists($name,$_POST)){
    return _cleanUserInput($_POST[$name]);
  }else{
    return FALSE;
  }
}

function _GET($name=FALSE){
  if(!$name){
    return _cleanUserInput($_GET);
  }elseif(array_key_exists($name,$_GET)){
    return _cleanUserInput($_GET[$name]);
  }else{
    return FALSE;
  }
}

function _GP($name){
  $post = _POST($name);
  return $post ? $post : _GET($name);
}


function explodeArrayForURL($array){
  // only for arrays with depth 1
  $params = array();
  foreach($array as $k => $v){
    if($v) $params[] .= urlencode($k) . '='  . urlencode($v);
  }

  return htmlentities(implode('&',$params));
}


?>