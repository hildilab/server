# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1466175804.131423
_enable_loop = True
_template_filename = '/home/webit/app/v4rna/app/templates/v4rna/v4rna-formular.mako'
_template_uri = 'v4rna/v4rna-formular.mako'
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
        zscorelist = context.get('zscorelist', UNDEFINED)
        dataset_list = context.get('dataset_list', UNDEFINED)
        h = context.get('h', UNDEFINED)
        zipped = context.get('zipped', UNDEFINED)
        len = context.get('len', UNDEFINED)
        headerlist = context.get('headerlist', UNDEFINED)
        anzahl = context.get('anzahl', UNDEFINED)
        proviurl = context.get('proviurl', UNDEFINED)
        liste = context.get('liste', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n<script language="javascript">\n$(document).ready(function(){\n    $("table6").hide()\n    $("a#slideFade6").toggle(function(){\n\t$("table6").animate({ height: \'show\', opacity: \'show\' }, \'fast\');\n    },function(){\n\t$("table6").animate({ height: \'hide\', opacity: \'hide\' }, \'fast\');\n    });\n    $("table1").hide()\n    $("a#slideFade1").toggle(function(){\n\t$("table1").animate({ height: \'show\', opacity: \'show\' }, \'fast\');\n    },function(){\n\t$("table1").animate({ height: \'hide\', opacity: \'hide\' }, \'fast\');\n    });\n});\n\n</script>\n\n<script language="javascript">\n    $(document).ready(function() {\n        $(".clear_btn").click( function(e){\n            clear_form_elements( $(this).parent() );\n        });\n    });\n    function clear_form_elements( $ele ) {\n        $ele.find(\':input\').each(function() {\n            switch(this.type) {\n                case \'file\':\n                case \'text\':\n                case \'textarea\':\n                    $(this).val(\'\');\n                    break;\n                case \'checkbox\':\n                case \'radio\':\n                    this.checked = false;\n            }\n        });\n    }\n</script>\n\n<div id="content" class="content">\n<!--            <script type="text/javascript">\n                document.write("<div class=\'toggleNice\' style=\'display:none;\'>");\n            </script> -->\n    <h1>Voronoia for RNA: Search & Calculation</h1>\n    <div class="subcontent">\n        <div>\n            <form action="tools/v4rna/generator/form" method="post" enctype="multipart/form-data">\n                <br>\n                <fieldset id="example_2">\n                    <legend>Get packing density from precalculated molecule file:</legend>\n                    <p style="text-indent:1.0em;">Enter PDB-Entry or search words from the PDB-Header <img src="static/img/helpbubble.png" alt="logo" title="e.g.: riboswitch, 3UCU ..."></img>\n                        <input name="data_idpdb" type="text" size="45" maxlength="100" />\n                        <form:error name="data_idpdb" />\n                    </p>\n<!--\t\t    <input type="checkbox" id="zipped" name="zipped" value="zipped" ><label for="zipped">Download all results zipped (many results occure long time to zip).</label>\n-->\t\t\n\t\t    \n                    <p><input type="submit" name="submit" value="submit" />\n\n\t\t    <a href="#" id="slideFade1">show/hide whole dataset</a><br>\n\t\t    <table1 border="0">\n\t\t    <a>\n')
        for element in dataset_list:
            __M_writer(u'\t\t\t    <a name="pdbfile" href="')
            __M_writer(unicode(h.url_for('tools/v4rna/generator/form', data_idpdb=element, data_pdb='', submit='submit')))
            __M_writer(u'">\n\t\t\t\t')

            context.write(element)
                                            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in [] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n\t\t\t    </a>\n')
        __M_writer(u'\t\t    </a>\n\t\t    </table1>\n\n                    </p>\n\t\t    \n                </fieldset>\n                <p>\n')
        if (liste):
            __M_writer(u'\t\t    Result (# \n\t\t    ')

            context.write(anzahl)
                                
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in [] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n\t\t\t):\n\t\t    <br>\n<!--\n')
            if (zipped):
                __M_writer(u'\t\t\tAll results zipped for download: <a name="zipped"  style=\'padding-left: 15px\' href="')
                __M_writer(unicode(h.url_for('tools/v4rna/generator/download', filename='zipped', task_id=1)))
                __M_writer(u'">results</a>\n\t\t    <br>\n')
            __M_writer(u'-->\n                    ')

            i=0
            g=len(liste)
                                
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['i','g'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n                    <table border="0">\n')
            if (headerlist[i]!=""):
                __M_writer(u'                            <thead>\n                                <td><b>Vol-File<img src="static/img/helpbubble.png" alt="logo" title="extends the original PDB-file by \nvan der Waals volume, solvent excluded volume and indicates whether the atom is buried or exposed (for more information consult the FAQ)"></img></b></td>\n                                <td><b>Header</b></td>\n\t\t\t\t<td><b>z-Score-RMS<img src="static/img/helpbubble.png" alt="logo" title="indicates how the packing density \nrelates to reference values (for more information consult the FAQ)"></img></b></td>\n                                <td><b>PDB-File<img src="static/img/helpbubble.png" alt="logo" title="a pre-filtered PDB-file (for more \ninformation consult the FAQ)"></img></b></td>\n\t\t\t\t<td><b>extended Vol-File<img src="static/img/helpbubble.png" alt="logo" title="Vol-file extended by packing \ndensity values and z-Score (for more information consult the FAQ)"></img></b></td>\n\t\t\t\t<td><b>Visualisation</b></td>\n\t\t\t\t<td><b>zipped Files<img src="static/img/helpbubble.png" alt="logo" title="contains Vol-, PDB- and extended Vol-File"></img></b></td>\n                            </thead>\n')
            __M_writer(u'                        <tbody>\n')
            while i!=g:
                __M_writer(u'                        <tr>\n                            <td>\n                                \n\t\t\t\t<a name="pdbfile" href="')
                __M_writer(unicode('staticpdb/'+liste[i]+'.pdb/'+liste[i]+'.pdb.vol'))
                __M_writer(u'">\n\t\t\t\t    ')

                context.write(liste[i])
                                                    
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in [] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\n\t\t\t\t</a>\n                            </td>\n\t\t\t    <td>\n                                ')

                context.write(headerlist[i])
                                                
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in [] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\n                            </td>\n\t\t\t    <td>\n                                ')

                context.write(zscorelist[i])
                                                
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in [] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\n                            </td>\n\t\t\t    <td>\n                                ')

                j=liste[i]
                                                
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['j'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\n')
                if (headerlist[i]!=""):
                    __M_writer(u'                                        <a name="pdbfile" href="')
                    __M_writer(unicode('staticpdb/'+liste[i]+'.pdb/'+liste[i]+'.pdb'))
                    __M_writer(u'">pdb-file </a>\n')
                __M_writer(u'                            </td>\n\t\t\t    <td>\n                                \n\t\t\t\t<a name="pdbfile" href="')
                __M_writer(unicode('staticpdb/'+liste[i]+'.pdb/'+liste[i]+'.pdb.vol.extended.vol'))
                __M_writer(u'">\n\t\t\t\t    ')

                context.write(liste[i])
                                                    
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in [] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\n\t\t\t\t</a>\n                            </td>\n\t\t\t    <td>\n                                \n\t\t\t\t<!-- moin jo, der link hier zeigt nun zu provi -->\n\t\t\t\t<a name="pdbfile" target="_blank" href="')
                __M_writer(unicode(proviurl+'/static/html/voro.html?example_json_url='+environurl+'/staticpdb/'+liste[i]+'.pdb/'+liste[i]+'.provi'))
                __M_writer(u'">\n\t\t\t\t    ')

                context.write(liste[i])
                                                    
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in [] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\n\t\t\t\t</a>\n                            </td>\n\t\t\t    <td>\n                                 <a name="singlezip"  style=\'padding-left: 15px\' href="')
                __M_writer(unicode(h.url_for('tools/v4rna/generator/download2', filename='singlezip', task_id=2, codefile=liste[i])))
                __M_writer(u'">\n\t\t\t\t    ')

                context.write(liste[i])
                                                    
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in [] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\n\t\t\t\t </a>\n\t\t\t\t ')

                i=i+1
                                                
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['i'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\n                            </td>\n                        </tr>\n')
            __M_writer(u'                    </tbody>\n                        <tfoot>\n                            \n                        </tfoot>\n                    </table>\n')
        __M_writer(u'                </p>\n                <h4>OR</h4>\n                <fieldset id="example_1">\n                    <legend>Calculate the atomic packing density with self-loaded RNA-structure:</legend>\n                    <p style="text-indent:1.0em;">Please load a PDB-file:\n                        <input name="data_pdb" type="file" value="pdb_datei" size="20" maxlength="100000" accept="text/*" />\n                        <form:error name="data_pdb" />\n                        <input class="clear_btn" type="button" value="Clear" />\n                    </p>\n                    \n                </fieldset>\n                <form:error name="blub" />\n                <br>\n                <a href="')
        __M_writer(unicode(h.url_for('tools/v4rna/generator/old_tasks')))
        __M_writer(u'">previous calculation tasks</a>\n                <p><input type="submit" name="submit" value="submit" /> <input type="reset" value="reset all" />\n                <br>\n                \n                \n            </form>\n        </div>\n    </div>\n</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"128": 153, "134": 155, "135": 159, "136": 159, "137": 160, "143": 162, "144": 164, "150": 166, "151": 170, "152": 176, "153": 189, "154": 189, "27": 0, "160": 154, "42": 1, "43": 65, "44": 66, "45": 66, "46": 66, "47": 67, "53": 69, "54": 72, "55": 79, "56": 80, "57": 81, "63": 83, "64": 87, "65": 88, "66": 88, "67": 88, "68": 91, "69": 92, "76": 95, "77": 97, "78": 98, "79": 112, "80": 113, "81": 114, "82": 117, "83": 117, "84": 118, "90": 120, "91": 124, "97": 126, "98": 129, "104": 131, "105": 134, "111": 136, "112": 137, "113": 138, "114": 138, "115": 138, "116": 140, "117": 143, "118": 143, "119": 144, "125": 146, "126": 152, "127": 152}, "uri": "v4rna/v4rna-formular.mako", "filename": "/home/webit/app/v4rna/app/templates/v4rna/v4rna-formular.mako"}
__M_END_METADATA
"""
