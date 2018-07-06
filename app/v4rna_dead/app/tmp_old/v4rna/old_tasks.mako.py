# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1467660803.777696
_enable_loop = True
_template_filename = '/home/webit/app/v4rna/app/templates/v4rna/old_tasks.mako'
_template_uri = 'v4rna/old_tasks.mako'
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
        zeit = context.get('zeit', UNDEFINED)
        h = context.get('h', UNDEFINED)
        len = context.get('len', UNDEFINED)
        task_list = context.get('task_list', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n<form action="form" method="post" enctype="multipart/form-data">\n    <div id="content" class="content">\n<!--       <script type="text/javascript">\n\tdocument.write("<div class=\'toggleNice\' style=\'display:none;\'>");\n      </script> -->\n<h1>Task List</h1>\n\n<ul>\n')
        for t in task_list:
            __M_writer(u"    <li><a href='")
            __M_writer(unicode(h.url_for('tools/v4rna/generator/task', task_id=t)))
            __M_writer(u"'>\n\t")

            i=0
                    
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['i'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
            while i != (len(task_list)):	
                if zeit[i][0]!=t:
                    __M_writer(u'\t\t\t')

                    i=i+1
                                            
                    
                    __M_locals_builtin_stored = __M_locals_builtin()
                    __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['i'] if __M_key in __M_locals_builtin_stored]))
                    __M_writer(u'\n')
                else:
                    __M_writer(u'\t\t\t')

                    context.write(zeit[i][1])
                    break
                                            
                    
                    __M_locals_builtin_stored = __M_locals_builtin()
                    __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in [] if __M_key in __M_locals_builtin_stored]))
                    __M_writer(u'\n')
            __M_writer(u'</a></li>\n')
        __M_writer(u'</ul>\n    </div>\n</form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"68": 27, "67": 24, "59": 21, "36": 1, "37": 10, "38": 11, "39": 11, "40": 11, "41": 12, "75": 69, "47": 14, "48": 15, "49": 16, "50": 17, "51": 17, "57": 19, "58": 20, "27": 0, "60": 21, "69": 29}, "uri": "v4rna/old_tasks.mako", "filename": "/home/webit/app/v4rna/app/templates/v4rna/old_tasks.mako"}
__M_END_METADATA
"""
