# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1467656990.248102
_enable_loop = True
_template_filename = '/home/webit/app/v4rna/app/templates/v4rna/methods_RefStat.mako'
_template_uri = 'v4rna/methods_RefStat.mako'
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
        __M_writer(u'\n\n<form action="form" method="post" enctype="multipart/form-data">\n    \n        <div id="content" class="content">\n<!--             <script type="text/javascript">\n                document.write("<div class=\'toggleNice\' style=\'display:none;\'>");\n            </script> -->\n\t\n            <div>\n                <h1>Reference dataset and Statistics</h1>\n\n\n<h2>Reference dataset</h2>\nVoronoia4RNA includes a dataset of presently 1766 PDB structures. All structures are considered containing at least one RNA chain and being obtained \nwith a resolution of 3.5 Angstrom or better. Structures solved by NMR are generally also included.\n<br>To calculate reference values, the non-redundant dataset of the <a target="_blank" \nhref=\'http://rna.bgsu.edu/nrlist/lists/20120623/Nonredundant_3,5A.html\'>BGSU RNA Structural Bioinformatics Group</a> is used. This dataset contains 621 \nstructures of RNA and complexes with a resolution of at least 3.5 Angstrom.\n\n\n\n\n<h2>Statistics</h2>\n\n\n<script type="text/javascript">\nfunction popup (url) {\n fenster = window.open(url, "Popupfenster", "width=4000,height=2000,resizable=yes");\n fenster.focus();\n return false;\n}\n</script>\n\n\n\n\n<a target="_blank" onclick="return popup(href=\'static/img/pdp.png\');"\n   F1 = window.open(\'static/img/pdp.png\',\'Fenster1\',\'width=400,height=200,left=0,top=0\'); return false;"><img src="static/img/pdp.png" width="400" height="200" border="0" alt="Vorschaubild"></a>\n<a target="_blank" onclick=\'return popup(href="static/img/pdpr.png");\'\n   F1 = window.open(\'static/img/pdpr.png\',\'Fenster1\',\'width=400,height=200,left=0,top=0\'); return false;"><img src="static/img/pdpr.png" width="400" height="200" border="0" alt="Vorschaubild"></a>\n<a target="_blank" onclick=\'return popup(href="static/img/pdr2.png");\'\n   F1 = window.open(\'static/img/pdr2.png\',\'Fenster1\',\'width=400,height=200,left=0,top=0\'); return false;"><img src="static/img/pdr2.png" width="400" height="200" border="0" alt="Vorschaubild"></a>\n<font size=\'1\'>(to increase, please click on the figure)</font>\n<br>\n<a>\n    The figures depict the average packing densities of the protors (figure 1), the protors per residue (figure 2) or the interdependency between packing \ndensities, structure resolution and size (figure 3). Only the buried atoms of the structures of the reference dataset were taken into account.\n<!--    <br>Represented by the pictures and the statistics, the packing density over the whole dataset is around 0,7. Although the difference between the \nresidues (within one protor) is very marginal. -->\n</a>\n\n\n\n            <script type="text/javascript">\n                document.write("</div>");\n            </script>\n        </div>\n</form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"32": 1, "27": 0, "38": 32}, "uri": "v4rna/methods_RefStat.mako", "filename": "/home/webit/app/v4rna/app/templates/v4rna/methods_RefStat.mako"}
__M_END_METADATA
"""
