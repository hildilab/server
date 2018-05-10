<?php

// severity
define('SIMPLELOG_WARNING', 'SIMPLELOG_WARNING');
define('SIMPLELOG_NOTE', 'SIMPLELOG_NOTE');

// visibility
define('SIMPLELOG_USER', 'SIMPLELOG_USER');
define('SIMPLELOG_ADMIN', 'SIMPLELOG_ADMIN');

class simpleLog {

    /*
    // Anlegen der Instanz
    private static $instance = NULL;
    */
    
    var $log = array();
    
    var $messages = array();

    //Konstruktor private, damit die Klasse nur aus sich selbst heraus instanziiert werden kann.
    private 
    function __construct() {

    }

    /*
    // Diese statische Methode gibt die Instanz zurueck.
    public static function getInstance() {
    
    if (self::$instance === NULL) {
    self::$instance = new self;
    }
    return self::$instance;
    }
    */

    // php4 version
    
    function &getInstance() {

	static $instance;
	
	if (!is_object($instance)) {
	    $instance = new simpleLog;
	}
	return $instance;
    }

    /*
    // Klonen per 'clone()' von außen verbieten.
    private function __clone() {}
    */
    
    function write($message, $severity = SIMPLELOG_WARNING, $visibility = SIMPLELOG_ADMIN) {

	$this->log[] = array(
	    'message' => $message,
	    'severity' => $severity,
	    'visibility' => $visibility,
	);
    }
    
    function format() {

	return ('<h3 id="logToggle" class="toggleNext">Log/Debuging:</h3>' . '<div>' . view_array($this->log) . '<hr/></div>');
    }
    
    function view() {

	echo $this->format();
    }

    /*
    * function get
    * @param $severity
    * @param $visibility
    */
    
    function get($severity, $visibility) {

	$filteredLog = array();
	foreach($this->log as $entry) {
	    
	    if ($entry['severity'] == $severity && $entry['visibility'] == $visibility) {
		$filteredLog[] = $entry['message'];
	    }
	}
	return count($filteredLog) ? $filteredLog : FALSE;
    }
}
?>
