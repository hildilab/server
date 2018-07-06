# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1466175686.340241
_enable_loop = True
_template_filename = u'/home/webit/app/v4rna/app/templates/v4rna/base.mako'
_template_uri = u'v4rna/base.mako'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">\n<html xmlns="http://www.w3.org/1999/xhtml">\n<head>\n  <title>VORONOIA for RNA</title>\n  <base href=')
        __M_writer(unicode(trans.app.config.base_tag_href))
        __M_writer(u'>\n  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />\n  <link href="static/css/stylesheet.css" rel="stylesheet" type="text/css" />\n<script type="text/javascript">\n\n  var _gaq = _gaq || [];\n  _gaq.push([\'_setAccount\', \'UA-34569364-1\']);\n  _gaq.push([\'_trackPageview\']);\n\n  (function() {\n    var ga = document.createElement(\'script\'); ga.type = \'text/javascript\'; ga.async = true;\n    ga.src = (\'https:\' == document.location.protocol ? \'https://ssl\' : \'http://www\') + \'.google-analytics.com/ga.js\';\n    var s = document.getElementsByTagName(\'script\')[0]; s.parentNode.insertBefore(ga, s);\n  })();\n\n</script>\n</head>\n\n\n  <style type="text/css">\n  $(\'.selector\').qtip({\n   content: {\n      attr: \'alt\'\n   }\n})\n</style>\n<!--[if IE 5]><style type="text/css">\n  a.infobox span { display:none; }\n  a.infobox:hover span { display:block; }\n</style><![endif]-->\n\n\n<body>\n  <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.6.2/jquery.min.js"></script>\n  <script type="text/javascript" src="http://craigsworks.com/projects/qtip2/packages/latest/jquery.qtip.min.js"></script>\n\n  <noscript>\n    <div class="messages">\n      <b>javascript is inactive</b>&nbsp;-&nbsp;this site does not rely on javascript, but the usablity is better when it\'s acitivated\n    </div>\n  </noscript>\n  <div id="container">\n    <div class="leftcol">\n      <div class="header" align="center">\n\t<a href="')
        __M_writer(unicode(h.url_for('tools/v4rna/index')))
        __M_writer(u'" style="display:block;">\n\t  <img src="static/img/v4rna.jpg" width="140" height="148" alt="Logo" border="0">\n\t</a>\n\tVoronoia<br>\n\tfor RNA\n      </div>\n      <div class="navi">\n\t<a target="_self" class="active" href="')
        __M_writer(unicode(h.url_for('tools/v4rna/index')))
        __M_writer(u'">Home</a>\n\t<a target="_self"  href="')
        __M_writer(unicode(h.url_for('tools/v4rna/generator/index')))
        __M_writer(u'">Search & Calculate</a>\n        <a target="_self"  href="')
        __M_writer(unicode(h.url_for('tools/v4rna/methods')))
        __M_writer(u'">Description</a>\n\t  <div style="margin-left: 24px;">\n\t    <a target="_self"  href="')
        __M_writer(unicode(h.url_for('tools/v4rna/methods')))
        __M_writer(u'">Calculation, Packing density and Cavities</a>\n\t    <a target="_self"  href="')
        __M_writer(unicode(h.url_for('tools/v4rna/methods_RefStat')))
        __M_writer(u'">Dataset & Statistics</a>\n\t  </div>\n\t<a target="_self"  href="')
        __M_writer(unicode(h.url_for('tools/v4rna/tutorial')))
        __M_writer(u'">Manual</a>\n\t<a target="_self"  href="')
        __M_writer(unicode(h.url_for('tools/v4rna/references')))
        __M_writer(u'">References</a>\n                <a target="_self"  href="')
        __M_writer(unicode(h.url_for('tools/v4rna/faq')))
        __M_writer(u'">FAQ</a>\n\t\t\n      </div>\n      <div style="margin-top: 24px;">&nbsp;</div>\n\t<div class="navi">\n\t  <a target="_blank"  href="http://proteinformatics.de">related Projects</a>\n\t  <a target="_self"  href="mailto:peter.hildebrand@charite.de">Contact</a>\n\t</div>\n      </div>\n    </div>\n  \n  \n  \n    ')
        __M_writer(unicode(next.body()))
        __M_writer(u'\n    \n    \n    \n    \n    \n    <div align=center class="footer" id="footer">\n      <div  align=center style="float:left; position:absolute; left:430px">\n\t<a href = "http://www.charite.de" target = "_blank">\n\t  <img  align=center src="static/img/charite_logo.png" alt="charite logo"/>\n\t</a>\n      </div>\n      <div  align=center style="position:absolute; left:580px">\n\t<a href="http://www.charite.de" target="_blank">Charit&eacute; Berlin</a>\n\t- \n\t<a href="http://proteinformatics.de" target="_blank">ProteinFormatics Group</a>\n\t- \n\tCopyright 2012\n                <br/>\n                <a href="mailto:peter.hildebrand@charite.de"> \n                    we are interested in your feedback - thanks!\n                </a>\n                <br/>\n                version 1.0 - Jun 2012\n                <br>\n                updated 2013-09-09\n      </div>\n    </div>\n  </div>\n  <!-- Piwik -->\n  <script type="text/javascript">\n    var pkBaseURL = (("https:" == document.location.protocol) ? "https://proteinformatics.charite.de/piwik/" : "http://proteinformatics.charite.de/piwik/");\n    document.write(unescape("%3Cscript src=\'" + pkBaseURL + "piwik.js\' type=\'text/javascript\'%3E%3C/script%3E"));\n  </script><script type="text/javascript">\n    try {\n      var piwikTracker = Piwik.getTracker(pkBaseURL + "piwik.php", 4);\n      piwikTracker.trackPageView();\n      piwikTracker.enableLinkTracking();\n    } catch( err ) {}\n  </script><noscript><p><img align=center \nsrc="http://proteinformatics.charite.de/piwik/piwik.php?idsite=4" style="border:0" alt=""/></p></noscript>\n  <!-- End Piwik Tag -->\n</body>\n</html>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 0, "24": 1, "25": 5, "26": 5, "27": 49, "28": 49, "29": 56, "30": 56, "31": 57, "32": 57, "33": 58, "34": 58, "35": 60, "36": 60, "37": 61, "38": 61, "39": 63, "40": 63, "41": 64, "42": 64, "43": 65, "44": 65, "45": 78, "46": 78, "52": 46}, "uri": "v4rna/base.mako", "filename": "/home/webit/app/v4rna/app/templates/v4rna/base.mako"}
__M_END_METADATA
"""
