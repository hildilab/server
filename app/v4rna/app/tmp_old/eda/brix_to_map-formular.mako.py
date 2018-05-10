# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1352737007.264766
_enable_loop = True
_template_filename = '/mnt/bigdisk/development/repos/biobench-v4rna/app/templates/eda/brix_to_map-formular.mako'
_template_uri = 'eda/brix_to_map-formular.mako'
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
        __M_writer(u'\n\n<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.6.2/jquery.min.js"></script>\n<script language="javascript">\n    $(document).ready(function() {\n        $(".clear_btn").click( function(e){\n            clear_form_elements( $(this).parent() );\n        });\n    });\n    function clear_form_elements( $ele ) {\n        $ele.find(\':input\').each(function() {\n            switch(this.type) {\n                case \'file\':\n                case \'text\':\n                case \'textarea\':\n                    $(this).val(\'\');\n                    break;\n                case \'checkbox\':\n                case \'radio\':\n                    this.checked = false;\n            }\n        });\n    }\n</script>\n        <div id="content" class="content">\n<!--            <script type="text/javascript">\n                document.write("<div class=\'toggleNice\' style=\'display:none;\'>");\n            </script> -->\n            <h1>Brix to MAP Converter</h1>\n            <div class="subcontent">\n                <div>\n                    <form action="form" method="post" enctype="multipart/form-data">\n                        <fieldset id="example_1">\n                            <legend>Load the file independent:</legend>\n                            <p style="text-indent:1.0em;">Please choose a brix-file:<br>\n                                <input name="data" type="file" value="pdb_datei" size="50" maxlength="100000" accept="text/*" />\n                                <form:error name="data" />\n                            </p>\n                            <input class="clear_btn" type="button" value="Clear" />\n                        </fieldset>\n                        <br>\n                        <p><input type="submit" name="submit" value="submit" /> <input type="reset" value="reset all" /></p>\n                    </form>\n                </div>\n            </div>\n        </div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


