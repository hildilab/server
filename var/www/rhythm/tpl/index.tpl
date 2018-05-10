<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>RHYTHM - Webserver</title>

    <HTTP-EQUIV="PRAGMA" CONTENT="NO-CACHE">

    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <link href="./css/stylesheet.css" rel="stylesheet" type="text/css" />
    {foreach from=$extraCSS item=filename}
    <link href="./css/{$filename}.css" rel="stylesheet" type="text/css" />
    {/foreach}

    {if $styleCSS}
    <style type="text/css">
      <!--
	  {foreach from=$styleCSS item=css}
	  {$css}
	  {/foreach}
	-->
    </style>
    {/if}


    <script type="text/javascript">
      {literal}
      try {
        document.execCommand("BackgroundImageCache", false, true);
      } catch(err) {}
      {/literal}

      {foreach from=$jsVARS key=name item=value}
      var {$name} = {$value};
      {/foreach}

      {literal}

      {/literal}
    </script>

    <script type="text/javascript" src="./js/prototype.js"></script>
    <script type="text/javascript" src="./js/effects.js"></script>

    {foreach from=$extraJS item=filename}
    <script type="text/javascript" src="./js/{$filename}.js"></script>
    {/foreach}

    <script type="text/javascript" src="./js/test.js"></script>

  </head>

  <body>  

    <script type="text/javascript" src="./js/wz_tooltip.js"></script>

    <noscript>
      <div class="messages">
	<b>javascript is inactive</b>&nbsp;-&nbsp;this site does not rely on javascript, but the usablity is better when it's acitivated
      </div>
    </noscript>

    {if isset($log)}{$log}{/if}

    <div id="container">
      <!--{include file='header.tpl'}-->
      {include file='sidebar.tpl'}

      <div id="content" class="content">
	<script type="text/javascript">
	  document.write("<div class='toggleNice' style='display:none;'>");
	</script>
	{include file=$pageTplFile}
	<script type="text/javascript">
	  document.write("</div>");
	</script>
      </div>


      {include file='footer.tpl'}
    </div>
    
    {literal}
    <!-- Piwik -->
    <script type="text/javascript">
    var pkBaseURL = (("https:" == document.location.protocol) ? "https://proteinformatics.charite.de/piwik/" : "http://proteinformatics.charite.de/piwik/");
    document.write(unescape("%3Cscript src='" + pkBaseURL + "piwik.js' type='text/javascript'%3E%3C/script%3E"));
    </script><script type="text/javascript">
    try {
    var piwikTracker = Piwik.getTracker(pkBaseURL + "piwik.php", 2);
    piwikTracker.trackPageView();
    piwikTracker.enableLinkTracking();
    } catch( err ) {}
    </script><noscript><p><img src="http://proteinformatics.charite.de/piwik/piwik.php?idsite=2" style="border:0" alt=""/></p></noscript>
    <!-- End Piwik Tag -->
    {/literal}
  </body>
</html>

