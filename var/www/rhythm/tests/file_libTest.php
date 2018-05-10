<?php

require_once('PHPUnit/Framework.php');
 
class file_libTest extends PHPUnit_Framework_TestCase {
 
        function testMe() {
                $params = 1;
                $this->assertEquals(1, $params);
        }
 
        function testMeToo() {
                $params = 1;
                $this->assertEquals(2,$params);
        }
}
 
?>