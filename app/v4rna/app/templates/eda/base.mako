<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>ELECTRON DENSITY - Webserver</title>

  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <link href="/static/css/stylesheet.css" rel="stylesheet" type="text/css" />
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
	<a href="${h.url_for('/tools/eda/index')}" style="display:block;">
	  <img src="/static/img/logo.jpg" width="180" height="198" alt="Logo" border="0">
	</a>
	ELECTRON<br>
	DENSITY
      </div>
      <div class="navi">
	<a target="_self" class="active" href="${h.url_for('/tools/eda/index')}">Home</a>
	<a target="_self"  href="${h.url_for('/tools/eda/generator/index')}">Generate Electron Density Maps</a>
	<a target="_self"  href="${h.url_for('/tools/eda/converter/index')}">Convert Electron Microscopy Maps</a>
	<a target="_self"  href="${h.url_for('/tools/eda/brix_converter/index')}">Convert Brix to Map files</a>
                <a target="_self" href="${h.url_for('/tools/eda/methods_EDM')}">Methods</a>
                <div style="margin-left: 24px;">
                    <a target="_self"  href="${h.url_for('/tools/eda/methods_EDM')}">Generating the ED-Maps</a>
                    <a target="_self"  href="${h.url_for('/tools/eda/methods_Converter')}">Map-Converter</a>
                </div>
	<a target="_self"  href="${h.url_for('/tools/eda/references')}">References</a>
                <a target="_self"  href="${h.url_for('/tools/eda/faq')}">FAQ</a>
		
      </div>
      <div style="margin-top: 24px;">&nbsp;</div>
	<div class="navi">
	  <a target="_self"  href="${h.url_for('/tools/eda/links')}">Usefull Links</a>
	  <a target="_blank"  href="http://proteinformatics.de">related Projects</a>
	</div>
      </div>
    </div>
  
  
  
    ${next.body()}
    
    
    
    
    
    <div class="footer" id="footer">
      <div style="float:left; position:absolute; left:430px">
	<a href = "http://www.charite.de" target = "_blank">
	  <img src="/static/img/charite_logo.png" alt="charite logo"/>
	</a>
      </div>
      <div style="position:absolute; left:580px">
	<a href="http://www.charite.de" target="_blank">Charit&eacute; Berlin</a>
	- 
	<a href="http://proteinformatics.de" target="_blank">ProteinFormatics Group</a>
	- 
	Copyright 2011
                <br/>
                <a href="mailto:peter.hildebrand@charite.de"> 
                    we are interested in your feedback - thanks!
                </a>
                <br/>
                version 0.0 - Okt 2011
      </div>
    </div>
  </div>
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
</body>
</html>

