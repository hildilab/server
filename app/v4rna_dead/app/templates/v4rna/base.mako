<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>VORONOIA for RNA</title>
  <base href=${trans.app.config.base_tag_href}>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <link href="static/css/stylesheet.css" rel="stylesheet" type="text/css" />
<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-34569364-1']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>
</head>


  <style type="text/css">
  $('.selector').qtip({
   content: {
      attr: 'alt'
   }
})
</style>
<!--[if IE 5]><style type="text/css">
  a.infobox span { display:none; }
  a.infobox:hover span { display:block; }
</style><![endif]-->


<body>
  <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.6.2/jquery.min.js"></script>
  <script type="text/javascript" src="http://craigsworks.com/projects/qtip2/packages/latest/jquery.qtip.min.js"></script>

  <noscript>
    <div class="messages">
      <b>javascript is inactive</b>&nbsp;-&nbsp;this site does not rely on javascript, but the usablity is better when it's acitivated
    </div>
  </noscript>
  <div id="container">
    <div class="leftcol">
      <div class="header" align="center">
	<a href="${h.url_for('tools/v4rna/index')}" style="display:block;">
	  <img src="static/img/v4rna.jpg" width="140" height="148" alt="Logo" border="0">
	</a>
	Voronoia<br>
	for RNA
      </div>
      <div class="navi">
	<a target="_self" class="active" href="${h.url_for('tools/v4rna/index')}">Home</a>
	<a target="_self"  href="${h.url_for('tools/v4rna/generator/index')}">Search & Calculate</a>
        <a target="_self"  href="${h.url_for('tools/v4rna/methods')}">Description</a>
	  <div style="margin-left: 24px;">
	    <a target="_self"  href="${h.url_for('tools/v4rna/methods')}">Calculation, Packing density and Cavities</a>
	    <a target="_self"  href="${h.url_for('tools/v4rna/methods_RefStat')}">Dataset & Statistics</a>
	  </div>
	<a target="_self"  href="${h.url_for('tools/v4rna/tutorial')}">Manual</a>
	<a target="_self"  href="${h.url_for('tools/v4rna/references')}">References</a>
                <a target="_self"  href="${h.url_for('tools/v4rna/faq')}">FAQ</a>
		
      </div>
      <div style="margin-top: 24px;">&nbsp;</div>
	<div class="navi">
	  <a target="_blank"  href="http://proteinformatics.de">related Projects</a>
	  <a target="_self"  href="mailto:peter.hildebrand@charite.de">Contact</a>
	</div>
      </div>
    </div>
  
  
  
    ${next.body()}
    
    
    
    
    
    <div align=center class="footer" id="footer">
      <div  align=center style="float:left; position:absolute; left:430px">
	<a href = "http://www.charite.de" target = "_blank">
	  <img  align=center src="static/img/charite_logo.png" alt="charite logo"/>
	</a>
      </div>
      <div  align=center style="position:absolute; left:580px">
	<a href="http://www.charite.de" target="_blank">Charit&eacute; Berlin</a>
	- 
	<a href="http://proteinformatics.de" target="_blank">ProteinFormatics Group</a>
	- 
	Copyright 2012
                <br/>
                <a href="mailto:peter.hildebrand@charite.de"> 
                    we are interested in your feedback - thanks!
                </a>
                <br/>
                version 1.0 - Jun 2012
                <br>
                updated 2013-09-09
      </div>
    </div>
  </div>
  <!-- Piwik -->
  <script type="text/javascript">
    var pkBaseURL = (("https:" == document.location.protocol) ? "https://proteinformatics.charite.de/piwik/" : "http://proteinformatics.charite.de/piwik/");
    document.write(unescape("%3Cscript src='" + pkBaseURL + "piwik.js' type='text/javascript'%3E%3C/script%3E"));
  </script><script type="text/javascript">
    try {
      var piwikTracker = Piwik.getTracker(pkBaseURL + "piwik.php", 4);
      piwikTracker.trackPageView();
      piwikTracker.enableLinkTracking();
    } catch( err ) {}
  </script><noscript><p><img align=center 
src="http://proteinformatics.charite.de/piwik/piwik.php?idsite=4" style="border:0" alt=""/></p></noscript>
  <!-- End Piwik Tag -->
</body>
</html>

