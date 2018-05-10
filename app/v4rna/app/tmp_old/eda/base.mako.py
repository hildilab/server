# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1352727920.8116629
_enable_loop = True
_template_filename = u'/mnt/bigdisk/development/repos/biobench-v4rna/app/templates/eda/base.mako'
_template_uri = u'eda/base.mako'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">\n<html xmlns="http://www.w3.org/1999/xhtml">\n<head>\n  <title>ELECTRON DENSITY - Webserver</title>\n\n  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />\n  <link href="/static/css/stylesheet.css" rel="stylesheet" type="text/css" />\n</head>\n\n\n  <style type="text/css">\n  $(\'.selector\').qtip({\n   content: {\n      attr: \'alt\'\n   }\n})\n</style>\n<!--[if IE 5]><style type="text/css">\n  a.infobox span { display:none; }\n  a.infobox:hover span { display:block; }\n</style><![endif]-->\n\n\n<body>\n  <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.6.2/jquery.min.js"></script>\n  <script type="text/javascript" src="http://craigsworks.com/projects/qtip2/packages/latest/jquery.qtip.min.js"></script>\n\n  <noscript>\n    <div class="messages">\n      <b>javascript is inactive</b>&nbsp;-&nbsp;this site does not rely on javascript, but the usablity is better when it\'s acitivated\n    </div>\n  </noscript>\n  <div id="container">\n    <div class="leftcol">\n      <div class="header" align="center">\n\t<a href="')
        # SOURCE LINE 36
        __M_writer(unicode(h.url_for('/tools/eda/index')))
        __M_writer(u'" style="display:block;">\n\t  <img src="/static/img/logo.jpg" width="180" height="198" alt="Logo" border="0">\n\t</a>\n\tELECTRON<br>\n\tDENSITY\n      </div>\n      <div class="navi">\n\t<a target="_self" class="active" href="')
        # SOURCE LINE 43
        __M_writer(unicode(h.url_for('/tools/eda/index')))
        __M_writer(u'">Home</a>\n\t<a target="_self"  href="')
        # SOURCE LINE 44
        __M_writer(unicode(h.url_for('/tools/eda/generator/index')))
        __M_writer(u'">Generate Electron Density Maps</a>\n\t<a target="_self"  href="')
        # SOURCE LINE 45
        __M_writer(unicode(h.url_for('/tools/eda/converter/index')))
        __M_writer(u'">Convert Electron Microscopy Maps</a>\n\t<a target="_self"  href="')
        # SOURCE LINE 46
        __M_writer(unicode(h.url_for('/tools/eda/brix_converter/index')))
        __M_writer(u'">Convert Brix to Map files</a>\n                <a target="_self" href="')
        # SOURCE LINE 47
        __M_writer(unicode(h.url_for('/tools/eda/methods_EDM')))
        __M_writer(u'">Methods</a>\n                <div style="margin-left: 24px;">\n                    <a target="_self"  href="')
        # SOURCE LINE 49
        __M_writer(unicode(h.url_for('/tools/eda/methods_EDM')))
        __M_writer(u'">Generating the ED-Maps</a>\n                    <a target="_self"  href="')
        # SOURCE LINE 50
        __M_writer(unicode(h.url_for('/tools/eda/methods_Converter')))
        __M_writer(u'">Map-Converter</a>\n                </div>\n\t<a target="_self"  href="')
        # SOURCE LINE 52
        __M_writer(unicode(h.url_for('/tools/eda/references')))
        __M_writer(u'">References</a>\n                <a target="_self"  href="')
        # SOURCE LINE 53
        __M_writer(unicode(h.url_for('/tools/eda/faq')))
        __M_writer(u'">FAQ</a>\n\t\t\n      </div>\n      <div style="margin-top: 24px;">&nbsp;</div>\n\t<div class="navi">\n\t  <a target="_self"  href="')
        # SOURCE LINE 58
        __M_writer(unicode(h.url_for('/tools/eda/links')))
        __M_writer(u'">Usefull Links</a>\n\t  <a target="_blank"  href="http://proteinformatics.de">related Projects</a>\n\t</div>\n      </div>\n    </div>\n  \n  \n  \n    ')
        # SOURCE LINE 66
        __M_writer(unicode(next.body()))
        __M_writer(u'\n    \n    \n    \n    \n    \n    <div class="footer" id="footer">\n      <div style="float:left; position:absolute; left:430px">\n\t<a href = "http://www.charite.de" target = "_blank">\n\t  <img src="/static/img/charite_logo.png" alt="charite logo"/>\n\t</a>\n      </div>\n      <div style="position:absolute; left:580px">\n\t<a href="http://www.charite.de" target="_blank">Charit&eacute; Berlin</a>\n\t- \n\t<a href="http://proteinformatics.de" target="_blank">ProteinFormatics Group</a>\n\t- \n\tCopyright 2011\n                <br/>\n                <a href="mailto:peter.hildebrand@charite.de"> \n                    we are interested in your feedback - thanks!\n                </a>\n                <br/>\n                version 0.0 - Okt 2011\n      </div>\n    </div>\n  </div>\n  <!-- Piwik -->\n  <script type="text/javascript">\n    var pkBaseURL = (("https:" == document.location.protocol) ? "https://proteinformatics.charite.de/piwik/" : "http://proteinformatics.charite.de/piwik/");\n    document.write(unescape("%3Cscript src=\'" + pkBaseURL + "piwik.js\' type=\'text/javascript\'%3E%3C/script%3E"));\n  </script><script type="text/javascript">\n    try {\n      var piwikTracker = Piwik.getTracker(pkBaseURL + "piwik.php", 2);\n      piwikTracker.trackPageView();\n      piwikTracker.enableLinkTracking();\n    } catch( err ) {}\n  </script><noscript><p><img src="http://proteinformatics.charite.de/piwik/piwik.php?idsite=2" style="border:0" alt=""/></p></noscript>\n  <!-- End Piwik Tag -->\n</body>\n</html>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


