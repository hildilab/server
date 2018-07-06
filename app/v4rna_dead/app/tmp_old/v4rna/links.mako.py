# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1340726044.4665921
_enable_loop = True
_template_filename = '/home/webit/app/v4rna/app/templates/v4rna/links.mako'
_template_uri = 'v4rna/links.mako'
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
        # SOURCE LINE 1
        __M_writer(u'\n \n\n<div id="content" class="content">\n <h1>Links</h1>\n <div class="links">\n \n  <div>\n   <a target="_blank" href="http://www.rcsb.org/pdb/home/home.do">\n     <img src="/static/img/pdbLogo.png" width="120px" border="0" />\n     <b>RCSB Protein Data Bank</b> archive contains information about experimentally-determined structures of proteins, nucleic acids, and complex assemblies.\n   </a>\n  </div>\n  <div>\n   <a target="_blank" href="http://bioinf-services.charite.de/voronoia/index.php?site=home">\n     <img src="/static/img/1pw4_ohne_hoh_holes03.jpg" width="120px" border="0" />\n     <b>Voronoia</b> is a program suite to analyse and visualize the atomic packing of protein structures, based on the Voronoi-Cell method.\n   </a>\n  </div>\n  \n  \n  \n  \n  \n </div>\n <script type="text/javascript">\n   document.write("</div>");\n </script>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


