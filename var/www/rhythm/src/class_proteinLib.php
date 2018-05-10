<?php

class proteinLib{

  var $asLetter;
  var $asNames;
  var $asNames3;
  var $asDict;
  var $asDict3;

  // Anlegen der Instanz
  //private static $instance = NULL; 

  //Konstruktor private, damit die Klasse nur aus sich selbst heraus instanziiert werden kann.
  function __construct() {
    
    $this->asLetter = array("A","C","D","E","F","G","H","I","K","L","M","N","P","Q","R","S","T","U","V","W","Y");
    
    $this->asNames = array("Alanine","Cysteine","Aspartic Acid","Glutamate","Phenylalanine","Glycine","Histidine","Isoleucine","Lysine","Leucine","Methionine","Asparagine","Proline","Glutamine","Arginine","Serine","Threonine","Selenocysteine","Valine","Tryptophan","Tyrosine");
    $this->asDict = array_combine($this->asLetter,$this->asNames);

    $this->asNames3 = array("Ala","Cys","Asp","Glu","Phe","Gly","His","Ile","Lys","Leu","Met","Asn","Pro","Gln","Arg","Ser","Thr","Sel","Val","Trp","Tyr");
    $this->asDict3 = array_combine($this->asLetter,$this->asNames3);
  }
 
  // Diese statische Methode gibt die Instanz zurueck.
//   public static function getInstance() {
 
//     if (self::$instance === NULL) {
//       self::$instance = new self;
//     }
//     return self::$instance;
//   }
//   // Klonen per 'clone()' von außen verbieten.
//   private function __clone() {}

  function &getInstance() {
    static $instance;

    if (!is_object($instance)) {
      $instance = new proteinLib;
      $instance->__construct();
    }
    return $instance;
  }

  }

?>
