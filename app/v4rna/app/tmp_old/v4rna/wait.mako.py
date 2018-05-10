# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1480436059.301759
_enable_loop = True
_template_filename = '/home/webit/app/v4rna/app/templates/v4rna/wait.mako'
_template_uri = 'v4rna/wait.mako'
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
        h = context.get('h', UNDEFINED)
        state = context.get('state', UNDEFINED)
        task_id = context.get('task_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n<div id="content" class="content">\n<h1>Wait or go ahead</h1>\n<input type="button" value="Reload Page" onClick="window.location.href=window.location.href" />\n<pre>\n<!--')
        __M_writer(unicode(state))
        __M_writer(u'-->\nThe calculations are still running.\nPlease wait, see the results afterwards <a href="')
        __M_writer(unicode(h.url_for('tools/v4rna/generator/old_tasks')))
        __M_writer(u'">here</a> or under *Search & Calculate* --> previous \ncalculation tasks.\n<!--Your task-id is: ')
        __M_writer(unicode(task_id))
        __M_writer(u'-->\n</pre>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"35": 1, "36": 6, "37": 6, "38": 8, "39": 8, "40": 10, "41": 10, "47": 41, "27": 0}, "uri": "v4rna/wait.mako", "filename": "/home/webit/app/v4rna/app/templates/v4rna/wait.mako"}
__M_END_METADATA
"""
