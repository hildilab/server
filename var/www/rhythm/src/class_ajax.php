<?php

include_once("lib.php");

class ajax{

  var $ajaxId;

  var $registeredIds = array("hmmerStatus", 
			     );

  var $returnValue = '';

  function __construct(){

    $ajaxId = _GP('ajaxId');

    if(in_array($ajaxId,$this->registeredIds)){
      switch($ajaxId){
      case 'hmmerStatus':
	$this->hmmerStatus();
      }
    }
 
  }

  function hmmerStatus(){
    
    include_once("class_helixContactPrediction.php");

    $GLOBALS['sessionId'] = _GP('sessionId');
    
    if($GLOBALS['sessionId']){
      $this->returnValue = helixContactPrediction::hmmerStatus();
    }
  }

}

?> 

