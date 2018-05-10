# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1497441795.859729
_enable_loop = True
_template_filename = '/home/webit/app/v4rna/app/templates/v4rna/error.mako'
_template_uri = 'v4rna/error.mako'
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
        fehler = context.get('fehler', UNDEFINED)
        job = context.get('job', UNDEFINED)
        session = context.get('session', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n<div id="content" class="content">\n    <h2>Error</h2>\n    <pre>\n        <br>  \n        <h4><p style="text-indent:60px;">')
        __M_writer(unicode(fehler))
        __M_writer(u'</p></h4>\n        Please send a <a href="mailto:biobench.v4rna@gmail.com?subject=%B5ERROR%20V4RNA%D5&%20')
        __M_writer(unicode(job))
        __M_writer(u'%C2&%20')
        __M_writer(unicode(session))
        __M_writer(u'">mail</a> with the job- and the session-id.\n        If possible, please also send the input files.\n        <br>\n        job-id = ')
        __M_writer(unicode(job))
        __M_writer(u'\n        session-id = ')
        __M_writer(unicode(session))
        __M_writer(u'\n    </pre>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"35": 1, "36": 6, "37": 6, "38": 7, "39": 7, "40": 7, "41": 7, "42": 10, "43": 10, "44": 11, "45": 11, "51": 45, "27": 0}, "uri": "v4rna/error.mako", "filename": "/home/webit/app/v4rna/app/templates/v4rna/error.mako"}
__M_END_METADATA
"""
