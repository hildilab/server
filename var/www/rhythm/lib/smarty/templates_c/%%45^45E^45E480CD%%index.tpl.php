<?php /* Smarty version 2.6.20, created on 2018-05-07 09:00:16
         compiled from index.tpl */ ?>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>RHYTHM - Webserver</title>

    <HTTP-EQUIV="PRAGMA" CONTENT="NO-CACHE">

    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <link href="./css/stylesheet.css" rel="stylesheet" type="text/css" />
    <?php $_from = $this->_tpl_vars['extraCSS']; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array'); }if (count($_from)):
    foreach ($_from as $this->_tpl_vars['filename']):
?>
    <link href="./css/<?php echo $this->_tpl_vars['filename']; ?>
.css" rel="stylesheet" type="text/css" />
    <?php endforeach; endif; unset($_from); ?>

    <?php if ($this->_tpl_vars['styleCSS']): ?>
    <style type="text/css">
      <!--
	  <?php $_from = $this->_tpl_vars['styleCSS']; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array'); }if (count($_from)):
    foreach ($_from as $this->_tpl_vars['css']):
?>
	  <?php echo $this->_tpl_vars['css']; ?>

	  <?php endforeach; endif; unset($_from); ?>
	-->
    </style>
    <?php endif; ?>


    <script type="text/javascript">
      <?php echo '
      try {
        document.execCommand("BackgroundImageCache", false, true);
      } catch(err) {}
      '; ?>


      <?php $_from = $this->_tpl_vars['jsVARS']; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array'); }if (count($_from)):
    foreach ($_from as $this->_tpl_vars['name'] => $this->_tpl_vars['value']):
?>
      var <?php echo $this->_tpl_vars['name']; ?>
 = <?php echo $this->_tpl_vars['value']; ?>
;
      <?php endforeach; endif; unset($_from); ?>

      <?php echo '

      '; ?>

    </script>

    <script type="text/javascript" src="./js/prototype.js"></script>
    <script type="text/javascript" src="./js/effects.js"></script>

    <?php $_from = $this->_tpl_vars['extraJS']; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array'); }if (count($_from)):
    foreach ($_from as $this->_tpl_vars['filename']):
?>
    <script type="text/javascript" src="./js/<?php echo $this->_tpl_vars['filename']; ?>
.js"></script>
    <?php endforeach; endif; unset($_from); ?>

    <script type="text/javascript" src="./js/test.js"></script>

  </head>

  <body>  

    <script type="text/javascript" src="./js/wz_tooltip.js"></script>

    <noscript>
      <div class="messages">
	<b>javascript is inactive</b>&nbsp;-&nbsp;this site does not rely on javascript, but the usablity is better when it's acitivated
      </div>
    </noscript>

    <?php if (isset ( $this->_tpl_vars['log'] )): ?><?php echo $this->_tpl_vars['log']; ?>
<?php endif; ?>

    <div id="container">
      <!--<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => 'header.tpl', 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>-->
      <?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => 'sidebar.tpl', 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>

      <div id="content" class="content">
	<script type="text/javascript">
	  document.write("<div class='toggleNice' style='display:none;'>");
	</script>
	<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => $this->_tpl_vars['pageTplFile'], 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>
	<script type="text/javascript">
	  document.write("</div>");
	</script>
      </div>


      <?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => 'footer.tpl', 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>
    </div>
    
    <?php echo '
    <!-- Piwik -->
    <script type="text/javascript">
    var pkBaseURL = (("https:" == document.location.protocol) ? "https://proteinformatics.charite.de/piwik/" : "http://proteinformatics.charite.de/piwik/");
    document.write(unescape("%3Cscript src=\'" + pkBaseURL + "piwik.js\' type=\'text/javascript\'%3E%3C/script%3E"));
    </script><script type="text/javascript">
    try {
    var piwikTracker = Piwik.getTracker(pkBaseURL + "piwik.php", 2);
    piwikTracker.trackPageView();
    piwikTracker.enableLinkTracking();
    } catch( err ) {}
    </script><noscript><p><img src="http://proteinformatics.charite.de/piwik/piwik.php?idsite=2" style="border:0" alt=""/></p></noscript>
    <!-- End Piwik Tag -->
    '; ?>

  </body>
</html>
