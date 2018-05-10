<?php

set_include_path(dirname(__FILE__) . '/../lib/smarty/libs/' . PATH_SEPARATOR . get_include_path());

// NOTE: Smarty has a capital 'S'
require_once('Smarty.class.php');

class smartyRhythm extends Smarty {
  
  var $ref = array(
		   'punta07' => 1,
		   'hildebrand06' => 2,
		      'hildebrand08' => 3,
		      'hmmtop' => 4,
		   'pfam' => 5,
		      'hmmer' => 6,
		      'hildebrand05' => 7,
		      );

  function smartyRhythm(){

    // Class Constructor.
    // These automatically get set with each new instance.
    
    $this->Smarty();
    
    $this->template_dir = dirname(__FILE__) . '/../tpl/';
    $this->compile_dir  = dirname(__FILE__) . '/../lib/smarty/templates_c/';
    $this->config_dir   = dirname(__FILE__) . '/../lib/smarty/configs/';
    $this->cache_dir    = dirname(__FILE__) . '/../lib/smarty/cache/';
    
    $this->caching = false;

    $this->register_block('addslashesRemoveNl', array($this,'addslashesRemoveNl'));
    $this->register_modifier('getScoreClass', array($this,'getScoreClass'));
    $this->register_modifier('ref', array($this,'ref'));
  }

  function addslashesRemoveNl ($params, $content, &$smarty, &$repeat)
  {
    if (isset($content)){
      $nl = array("\r\n", "\n", "\r");
      return(str_replace($nl,'',addslashes($content)));
    }
  }

  function getScoreClass ($score)
  {
    if (isset($score)){
      if($score > 0.8) return('veryHigh');
      if($score > 0.4) return('higher');
      if($score > 0.0) return('high');
      if($score > -0.4) return('low');
      if($score > -0.9) return('lower');
      return('veryLow');
    }
  }
  
 function ref ($ref)
  {
    if (isset($ref)){
      @list($id,$name) = trimExplode("#",$ref);
      if(!$name){
	if(array_key_exists($id,$this->ref)){
	  $name = $this->ref[$id];
	}else{
	  $name = '*';
	}
      }

      return('<a class="ref" href="index.php?site=references&ref=' . $id . '#' . $id . '">' . $name . '</a>');
    }
  }

}

?>