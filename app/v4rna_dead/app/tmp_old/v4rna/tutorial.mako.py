# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1478805585.527847
_enable_loop = True
_template_filename = '/home/webit/app/v4rna/app/templates/v4rna/tutorial.mako'
_template_uri = 'v4rna/tutorial.mako'
_source_encoding = 'ascii'
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'base.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n\n<form action="form" method="post" enctype="multipart/form-data">\n    \n        <div id="content" class="content">\n<!--             <script type="text/javascript">\n                document.write("<div class=\'toggleNice\' style=\'display:none;\'>");\n            </script> -->\n\t\n            <div>\n                <h1>Viewer Tutorial</h1>\n<script type="text/javascript">\nfunction popup (url) {\n fenster = window.open(url, "Popupfenster", "width=4000,height=2000,resizable=yes");\n fenster.focus();\n return false;\n}\n</script>\n<table>\n    <tr>\n\t<td>\n\t    <a target="_blank" onclick="return popup(href=\'static/img/screenshot.png\');" F1 = window.open(\'static/img/screenshot.png\',\'Fenster1\',\'width=100%\'); return \nfalse;"><img src="static/img/screenshot.png" width="100%" border="0" alt="Vorschaubild"></a>\n\t    <br> click to increase the picture\n\t</td>\n\t<td>\n\t    <a>On startup Provi shows the desired structure in the "ribbon and aromatic" style, coloured according to the packing densities. Internal cavities are represented as simple balls. </a>\n\t    <br>\n\t    <a>In three widgets the visualization styles for general settings, cavities and packing densities can be altered. </a><br><br>\n\t</td>\n    </tr>\n    <tr>\n\t<td>\n\t    <a target="_blank" onclick="return popup(href=\'static/img/general.png\');" F1 = window.open(\'static/img/general.png\',\'Fenster1\',\'width=50%\'); return false;"><img \nsrc="static/img/general.png" width="50%" border="0" alt="Vorschaubild"><br><br>\n\t</td>\n\t<td>\n\t    <a>In the first widget you can find the general controls: style, selections and center options</a>\n\t</td>\n    </tr>\n    <tr>\n\t<td>\n\t    <a target="_blank" onclick="return popup(href=\'static/img/cavity.png\');" F1 = window.open(\'static/img/cavity.png\',\'Fenster1\',\'width=50%\'); return false;"><img \nsrc="static/img/cavity.png" width="50%" border="0" alt="Vorschaubild"><br><br>\n\t</td>\n\t<td>\n\t    <a>The second widget holds the controls for the visualization of the cavities. there are two different ways to represent the cavities.As simple balls (blue checkbox), which is the most \nproper way to look at all cavities of a structure. </a>\n\t    <br><br>\n\t</td>\n    </tr>\n    <tr>\n\t<td>\n\t    <a target="_blank" onclick="return popup(href=\'static/img/cavityeinzeln.png\');" F1 = window.open(\'static/img/cavityeinzeln.png\',\'Fenster1\',\'width=100%\'); return \nfalse;"><img src="static/img/cavityeinzeln.png" width="100%" border="0" alt="Vorschaubild"><br><br>\n\t</td>\n\t<td>\n\t    <a>To inspect a specific cavity are more detailed view is provided where the exact shape is shown (red checkbox). The green checkbox selects the atoms that are neighbouring the cavity. </a>\n\t    <br><br>\n\t</td>\n    </tr>\n    <tr>\n\t<td>\n\t    <a target="_blank" onclick="return popup(href=\'static/img/Pcking.png\');" F1 = window.open(\'static/img/Pcking.png\',\'Fenster1\',\'width=50%\'); return false;"><img \nsrc="static/img/Pcking.png" width="50%" border="0" alt="Vorschaubild"><br><br>\n\t</td>\n\t<td>\n\t    <a>In the third widget the different visualization modes for the packing densities are located. You can choose whether the packing range occurring in the file or a user-defined range is used \nand what colour scheme is used.</a>\n\t    <br><br>\n\t</td>\n    </tr>\n    <tr>\n\t<td>\n\t    <a target="_blank" onclick="return popup(href=\'static/img/cpk.png\');" F1 = window.open(\'static/img/cpk.png\',\'Fenster1\',\'width=100%\'); return false;"><img \nsrc="static/img/cpk.png" width="100%" border="0" alt="Vorschaubild"><br><br>\n\t</td>\n\t<td>\n\t    <a>To get an atom wise representation of the packing density a detailed representation style like cpk should be selected.</a>\n\t</td>\n    </tr>\n</table>\n            <script type="text/javascript">\n                document.write("</div>");\n            </script>\n        </div>\n</form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"32": 1, "27": 0, "38": 32}, "uri": "v4rna/tutorial.mako", "filename": "/home/webit/app/v4rna/app/templates/v4rna/tutorial.mako"}
__M_END_METADATA
"""
