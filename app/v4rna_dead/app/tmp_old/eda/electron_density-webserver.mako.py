# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1352727920.7736399
_enable_loop = True
_template_filename = '/mnt/bigdisk/development/repos/biobench-v4rna/app/templates/eda/electron_density-webserver.mako'
_template_uri = 'eda/electron_density-webserver.mako'
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
        __M_writer(u'\n\n<form action="form" method="post" enctype="multipart/form-data">\n    <div id="content" class="content">\n<!--       <script type="text/javascript">\n\tdocument.write("<div class=\'toggleNice\' style=\'display:none;\'>");\n      </script> -->\n      <h1>ELECTRON DENSITY - Webserver: </h1>\n      <div id="teaser" align="center">\n\t<img src="/static/img/logo.jpg" width="300" height="300" alt="logo" />\n\t<!-- <img src="/static/img/logo.jpg" alt="example result" /> -->\n      </div>\n      <h2>Motivation</h2>\n      <div class="contentblock">\n\t<div class="textblock">\n\t  <p>\n\t    \n\t    Nowadays, where one structure is following another, there\n\t    needs to be time to deal with them - particular as it is easy to get\n\t    evaluated electron density maps for instance by Uppsala Electron-Density\n\t    Server, linked to the Protein Data Bank. \n\t    This webservice gives the opportunity to evaluate structures by the\n\t    electron density nearest to the raw data.\n\t    \n\t    <br>In contrast to the EDS (which alike provides\n\t    Electron Density Maps), our attention relys on density maps nearest to\n\t    the raw data (where no interpretation of programs has been\n\t    accomplished) to be possible to compare the experimental data\n\t    (structure factors) to the structure, given and often interpreted\n\t    by the crystallographers and thereby published in the Protein Data Bank.\n\t    \n\t    <br>The maps depend on the experimental data deposited in the\n\t    Protein Data Bank or loaded from the user themselves.\n\t    \n\t    <br>In addition to electron density maps there is the opportunity to evaluate\n\t    the density maps by the sfcheck-module of CCP4 and to generate a so called\n\t    total omit map. As well,  there is the possibility to convert microscopy\n\t    maps into other formats by mapman.\n\t    \n\t    \n\t    <!--It goes without saying that the reader, casual or not, should have\n\t    access to model coordinates, experimental data and electron-density maps!-->\n\t    \n\t    \n\t    <br/>\n\t  </p>\n\t  <p class="textblock"> \n\t  </p>\n\t</div>\n\t<div class="spaceblock">\n\t  Summary\n\t</div>\n      </div>\n      <script type="text/javascript">\n\tdocument.write("</div>");\n      </script>\n    </div>\n</form>')
        return ''
    finally:
        context.caller_stack._pop_frame()


