# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1353686150.6452689
_enable_loop = True
_template_filename = '/mnt/bigdisk/development/repos/biobench-v4rna/app/templates/eda/electron_density-formular.mako'
_template_uri = 'eda/electron_density-formular.mako'
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
        __M_writer(u'\n\n\n<script language="javascript">\n    $(document).ready(function() {\n        $(".clear_btn").click( function(e){\n            clear_form_elements( $(this).parent() );\n        });\n    });\n    function clear_form_elements( $ele ) {\n        $ele.find(\':input\').each(function() {\n            switch(this.type) {\n                case \'file\':\n                case \'text\':\n                case \'textarea\':\n                    $(this).val(\'\');\n                    break;\n                case \'checkbox\':\n                case \'radio\':\n                    this.checked = false;\n            }\n        });\n    }\n</script>\n\n<div id="content" class="content">\n<!--            <script type="text/javascript">\n                document.write("<div class=\'toggleNice\' style=\'display:none;\'>");\n            </script> -->\n    <h1>Electron Density Calculation</h1>\n    <div class="subcontent">\n        <div>\n            <form action="form" method="post" enctype="multipart/form-data">\n                <h3>Required:</h3>\n                <fieldset id="example_1">\n                    <legend>Load the files independent:</legend>\n                    <p style="text-indent:1.0em;">Please choose a sf.cif-file or a mtz-file:\n                        <input name="data_cif" type="file" value="cif_datei" size="20" maxlength="100000" accept="text/*" />\n                        <form:error name="data_cif" />\n                        <input class="clear_btn" type="button" value="Clear" />\n                    </p>\n                    <p style="text-indent:1.0em;">Please choose a pdb-file: \n                        <input name="data_pdb" type="file" value="pdb_datei" size="20" maxlength="100000" accept="text/*" />\n                        <form:error name="data_pdb" />\n                        <input class="clear_btn" type="button" value="Clear" />\n                    </p>\n                </fieldset>\n                <h4>OR</h4>\n                <fieldset id="example_2">\n                    <legend>Get the files from the PDB:</legend>\n                    <p style="text-indent:1.0em;">Enter PDB-Entry <img src="/static/img/helpbubble.png" alt="logo" title="e.g.: 3DQB"></img>\n                        <input name="data_idpdb" type="text" value="from_pdb" size="10" maxlength="10" />\n                        <form:error name="data_idpdb" />\n                    </p>\n                </fieldset>\n                <form:error name="blub" />\n                <br>\n                <p><input type="submit" name="submit" value="submit" /> <input type="reset" value="reset all" /></p>\n                <br>\n                <br>\n                <h3>Optional:</h3>\n                <fieldset id="example_5">\n                    <legend>Validation:</legend>\n                        <input type="checkbox" id="sfcheck" name="sfcheck" value="sfcheck" checked="checked"><label for="sfcheck" >sfcheck </label><img src="/static/img/helpbubble.png" alt="logo" title="A program for assessing the agreement between the atomic model and X-ray data"></img>\n                        <form:error name="sfcheck" />\n                        <input type="checkbox" id="omit" name="omit" value="omit" checked="checked"><label for="omit" >omit map by sfcheck (time intensive: >10 min)</label><img src="/static/img/helpbubble.png" alt="logo" title="An omit map is a way to reduce the model bias in the electron density calculated with model phases."></img>\n                        <form:error name="omit" />\n                </fieldset>\n                <fieldset id="example_3">\n                    <legend>Outputmaps:</legend>\n                    <form:error name="maptype" />\n                    <input type="hidden" name="topic" value="maptypes" />\n                        <table border="0">\n                            <tr>\n                                <td>2fo-fc Map: <img src="/static/img/helpbubble.png" alt="logo" title="A sigmaa weighted map to guide the construction of a new model"></img></td>\n                                <td><input type="checkbox" id="maptype_2fofc_as" name="subtopics" value="tfofc_as" checked="checked"><label for="maptype_2fofc_as"> around asymmetric unit</label></td>\n                                <td><input type="checkbox" id="maptype_2fofc_al" name="subtopics" value="tfofc_al" checked="checked"><label for="maptype_2fofc_al"> around all atoms in PDB</label></td>\n                            </tr>\n                            <tr>\n                                <td>fo-fc Map: <img src="/static/img/helpbubble.png" alt="logo" title="Difference map to identify errors in a model"></img></td>\n                                <td><input type="checkbox" id="maptype_fofc_as" name="subtopics" value="fofc_as" checked="checked"><label for="maptype_fofc_as"> around asymmetric unit</label></td>\n                                <td><input type="checkbox" id="maptype_fofc_al" name="subtopics" value="fofc_al" checked="checked"><label for="maptype_fofc_al"> around all atoms in PDB</label></td>\n                            </tr>\n                        </table>\n                        <form:error name="subtopics" />\n                </fieldset>\n                <fieldset id="example_4">\n                    <legend>Extension of the maps:</legend>\n                        <input type="radio" id="mapext_map" name="mapext" value="dotmap"><label for="mapext_map"> save as .map (e.g. for <a href="http://biop.ox.ac.uk/coot/" target="_blank">COOT</a>)</label><br>\n                        <input type="radio" id="mapext_ccp4" name="mapext" value="dotccp4"><label for="mapext_ccp4"> save as .ccp4 (e.g. for <a href="http://www.pymol.org/" target="_blank">PYMOL</a>)</label><br>\n                        <form:error name="mapext" />\n                </fieldset>\n                <p><input type="submit" name="submit" value="submit" /> <input type="reset" value="reset all" /></p>\n            </form>\n        </div>\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


