# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1466175686.269047
_enable_loop = True
_template_filename = '/home/webit/app/v4rna/app/templates/v4rna/voronoia4rna.mako'
_template_uri = 'v4rna/voronoia4rna.mako'
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
        __M_writer(u'\n\n<form action="form" method="post" enctype="multipart/form-data">\n    <div id="content" class="content">\n<!--       <script type="text/javascript">\n\tdocument.write("<div class=\'toggleNice\' style=\'display:none;\'>");\n      </script> -->\n      <h1>VORONOIA 4 RNA </h1>\n      <div id="teaser" align="center">\n\t<img src="static/img/logo_v4rna.png" width="30%" height="30%" alt="logo" />\n\t<!--<img src="/static/img/logo.jpg" width="100" height="100" alt="logo" /> -->\n\t<!-- <img src="/static/img/logo.jpg" alt="example result" /> -->\n      </div>\n      <h2>Motivation</h2>\n\n\t<div class="middleblock">\n\t  <p>\n\t    \n\t  <h3>A method to calculate atomic packing and packing defects</h3>\nVoronoia4RNA is a database storing data on atomic packing densities of RNA structures and complexes. Compared to other methods, that solely estimate van \nder Waals interactions i.e. by gain of solvent excluded surfaces, Voronoia4RNA allocates the free space between neighbouring atoms. It explicitly takes \npacking defects into consideration and is therefore an appropriate method to calculate van der Waals interactions and to estimate the underlying forces.\n<br>\n<h3>On site visualization</h3>\nPacking densities and water sized cavities can be visualized by the Jmol based viewer Provi. Visualisation allows to quickly evaluate these cavities that \noften refer to internal waters not resolved in the crystal structure. Regions with large packing defects i.e. in ribosomes or riboswitches also refer to \nlocal flexibilities. Packing densities are also considered as a tool to assess the quality of a structure, as this measure correlates with X-ray \nstructure resolution. In some cases, Voronoia4RNA may also be used to detect potential binding sites for ligands or coenzymes. \n<br>\n<h3>What you can do ...</h3>\nYou may browse a pre-calculated set of RNA structures, visualize or download sub-datasets or individual entries, submit your own protein or RNA structure \nfor calculation and compare it to reference values calculated from a set of non-redundant RNA structures by means of a given z-Score.\n\n\t    <br/>\n\t  </p>\n\n\n      </div>\n      <script type="text/javascript">\n\tdocument.write("</div>");\n      </script>\n    </div>\n</form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"32": 1, "27": 0, "38": 32}, "uri": "v4rna/voronoia4rna.mako", "filename": "/home/webit/app/v4rna/app/templates/v4rna/voronoia4rna.mako"}
__M_END_METADATA
"""
