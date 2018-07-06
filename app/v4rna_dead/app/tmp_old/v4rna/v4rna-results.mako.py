# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1480436612.712749
_enable_loop = True
_template_filename = '/home/webit/app/v4rna/app/templates/v4rna/v4rna-results.mako'
_template_uri = 'v4rna/v4rna-results.mako'
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
        environurl = context.get('environurl', UNDEFINED)
        task_id = context.get('task_id', UNDEFINED)
        proviurl = context.get('proviurl', UNDEFINED)
        provipath = context.get('provipath', UNDEFINED)
        file_status = context.get('file_status', UNDEFINED)
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.6.2/jquery.min.js"></script>\n<script language="javascript">\n$(document).ready(function(){\n    $("table").hide()\n    $("a#slideFade").toggle(function(){\n        $("table").animate({ height: \'show\', opacity: \'show\' }, \'fast\');\n    },function(){\n        $("table").animate({ height: \'hide\', opacity: \'hide\' }, \'fast\');\n    })\n});\n</script>  \n        <div id="content" class="content">\n<!--            <script type="text/javascript">\n                document.write("<div class=\'toggleNice\' style=\'display:none;\'>");\n            </script> -->\n            <h1>Voronoia for RNA Calculation - Results</h1>\n            <div class="subcontent">\n                <div>\n                    <form action="form" method="post" enctype="multipart/form-data">\n                        <fieldset id="example_1"><legend>Download the files:</legend>\n                            <p>\n')
        if (file_status['volfile']):
            __M_writer(u'                                    The vol file:<br>\n                                    <a name="volfile"  style=\'padding-left: 15px\' href="')
            __M_writer(unicode(h.url_for('tools/v4rna/generator/download', filename='volfile', task_id=task_id)))
            __M_writer(u'">vol-file</a><br>\n')
        __M_writer(u'                            </p>\n                            <p>\n')
        if (file_status['exvol']):
            __M_writer(u'                                    The vol file:<br>\n                                    <a name="exvol"  style=\'padding-left: 15px\' href="')
            __M_writer(unicode(h.url_for('tools/v4rna/generator/download', filename='exvol', task_id=task_id)))
            __M_writer(u'">extended vol-file</a><br>\n')
        __M_writer(u'                            </p>\n                            <p>\n')
        if (file_status['provi']):
            __M_writer(u'                                    Visualization:<br>\n                                    <a name="provi" target="_blank" href="')
            __M_writer(unicode(proviurl+'/static/html/voro.html?example_json_url='+environurl+'/staticjob/'+provipath))
            __M_writer(u'">Visualization</a><br>\n')
        __M_writer(u'                            </p>\n\n                            <p>\n')
        if (file_status['info']):
            __M_writer(u'                                    The info file:<br>\n                                    <a name="info"  style=\'padding-left: 15px\' href="')
            __M_writer(unicode(h.url_for('tools/v4rna/generator/download', filename='info', task_id=task_id)))
            __M_writer(u'">info-file</a><br>\n')
        __M_writer(u'                            </p>\n                            <p>\n')
        if (file_status['stdout']):
            __M_writer(u'                                    The error file:<br>\n                                    <a name="stdout"  style=\'padding-left: 15px\' href="')
            __M_writer(unicode(h.url_for('tools/v4rna/generator/download', filename='stdout', task_id=task_id)))
            __M_writer(u'">error-file</a><br>\n')
        __M_writer(u'                            </p>\n                            <p>\n')
        if (file_status['stderr']):
            __M_writer(u'                                    The error file:<br>\n                                    <a name="stderr"  style=\'padding-left: 15px\' href="')
            __M_writer(unicode(h.url_for('tools/v4rna/generator/download', filename='stderr', task_id=task_id)))
            __M_writer(u'">error-file</a><br>\n')
        __M_writer(u'                            </p>\n                        <br>\n           <!--             All files compressed into zip format:\n                        <p><a name="allzip"  style=\'padding-left: 300px\' href="')
        __M_writer(unicode(h.url_for('tools/v4rna/generator/download', filename='allzip', task_id=task_id)))
        __M_writer(u'">download all</a></p>\n                        -->\n                        </fieldset>\n                    </form>\n                </div>\n            </div>\n            <script type="text/javascript">\n                document.write("</div>");\n            </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"27": 0, "38": 1, "39": 23, "40": 24, "41": 25, "42": 25, "43": 27, "44": 29, "45": 30, "46": 31, "47": 31, "48": 33, "49": 35, "50": 36, "51": 37, "52": 37, "53": 39, "54": 42, "55": 43, "56": 44, "57": 44, "58": 46, "59": 48, "60": 49, "61": 50, "62": 50, "63": 52, "64": 54, "65": 55, "66": 56, "67": 56, "68": 58, "69": 61, "70": 61, "76": 70}, "uri": "v4rna/v4rna-results.mako", "filename": "/home/webit/app/v4rna/app/templates/v4rna/v4rna-results.mako"}
__M_END_METADATA
"""
