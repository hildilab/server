# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1478960231.854825
_enable_loop = True
_template_filename = '/home/webit/app/v4rna/app/templates/v4rna/references.mako'
_template_uri = 'v4rna/references.mako'
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
        __M_writer(u'\n<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.6.2/jquery.min.js"></script>\n    <div id="content" class="content">\n<!--             <script type="text/javascript">\n                document.write("<div class=\'toggleNice\' style=\'display:none;\'>");\n            </script> -->\n\t<div>\n\t    <h1>References</h1>\n\t    <ol>\n\t    <li>\n\t\t<div class="reference" id="1">\n\t\t    <span class="title">Deviations from standard atomic volumes as a quality measure for protein crystal structures</span>\n\t\t    <span class="authors">Pontius, J., J. Richelle, and S. J. Wodak.</span>\n\t\t    <span class="magazine">J Mol Biol 264</span>\n\t\t    <span class="year">(1996)</span>\n\t\t    <span class="issue">9, 121-136</span>\n\t\t</div> \n\t    </li>\n\t    <li>\n\t\t<div class="reference" id="2">\n\t\t    <span class="title">Voronoi Cell: New Method for Allocation of Space among Atoms: Elimination of Avoidable Errors in computation of Atomic Volume and Density.</span>\n\t\t    <span class="authors">Goede, A., R. Preissner, and C. Froemmel.</span>\n\t\t    <span class="magazine">Bioinformatics 18</span>\n\t\t    <span class="year">(1997)</span>\n\t\t    <span class="issue">42, 985-995</span>\n\t\t</div> \n\t    </li>\n\t    <li>\n\t\t<div class="reference" id="3">\n\t\t    <span class="title">Computations of protein volumes: sensitivity analysis and parameter database</span>\n\t\t    <span class="authors">Tsai, J. and M. Gerstein.</span>\n\t\t    <span class="magazine">Bioinformatics 18</span>\n\t\t    <span class="year">(2002)</span>\n\t\t    <span class="issue">42, 985-995</span>\n\t\t</div> \n\t    </li>\n\t    <li>\n\t\t<div class="reference" id="4">\n\t\t    <span class="title">Inhomogeneous molecular density: reference packing densities and distribution of cavities within proteins</span>\n\t\t    <span class="authors">Rother, K., R. Preissner, A. Goede, and C. Froemmel.</span>\n\t\t    <span class="magazine">Bioinformatics 19</span>\n\t\t    <span class="year">(2003)</span>\n\t\t    <span class="issue">5, 2112-2121</span>\n\t\t</div> \n\t    </li>\n\t    <li>\n\t\t<div class="reference" id="5">\n\t\t    <span class="title">Molecular packing and packing defects in helical membrane proteins</span>\n\t\t    <span class="authors">Hildebrand, P. W., K. Rother, A. Goede, R. Preissner, and C. Froemmel</span>\n\t\t    <span class="magazine">Biophys J 88</span>\n\t\t    <span class="year">(2005)</span>\n\t\t    <span class="issue">49, 1970-1977</span>\n\t\t</div> \n\t    </li>\n\t    <li>\n\t\t<div class="reference" id="6">\n\t\t    <span class="title">Determining the minimum number of types necessary to represent the sizes of protein atoms</span>\n\t\t    <span class="authors">J. Tsai, N. Voss, and M. Gerstein.</span>\n\t\t    <span class="magazine">Bioinformatics 17</span>\n\t\t    <span class="year">(2001)</span>\n\t\t    <span class="issue">10, 949-956</span>\n\t\t</div> \n\t    </li>\n\t    <li>\n\t\t<div class="reference" id="7">\n\t\t    <span class="title">An effective solvation term based on atomic occupancies for use in protein</span>\n\t\t    <span class="authors">P. F. W. Stouten, C. Froemmel, H. Nakamura, and C. Sander</span>\n\t\t    <span class="magazine">Mol Simul</span>\n\t\t    <span class="year">(1993)</span>\n\t\t    <span class="issue">10, 97-120</span>\n\t\t</div> \n\t    </li>\n\t    <li>\n\t\t<div class="reference" id="8">\n\t\t    <span class="title">Voronoia: analyzing packing in protein structures.</span>\n\t\t    <span class="authors">Rother K, Hildebrand PW, Goede A, Gruening B, Preissner R.</span>\n\t\t    <span class="magazine">Nucleic Acids Res. (Database issue)</span>\n\t\t    <span class="year">(2009)</span>\n\t\t    <span class="issue">37, D393-5</span>\n\t\t</div> \n\t    </li>\n\t    <li>\n\t\t<div class="reference" id="9">\n\t\t    <span class="title">Calculation of standard atomic volumes for RNA and comparison with proteins: RNA is packed more tightly.</span>\n\t\t    <span class="authors">Voss N R, Gerstein M.</span>\n\t\t    <span class="magazine">Journal of molecular biology</span>\n\t\t    <span class="year">(2005)</span>\n\t\t    <span class="issue">346.2, 477-92</span>\n\t\t</div> \n\t    </li>\n\t    </ol>\n\t    \n\t    \n\t</div>\n    </div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"32": 1, "27": 0, "38": 32}, "uri": "v4rna/references.mako", "filename": "/home/webit/app/v4rna/app/templates/v4rna/references.mako"}
__M_END_METADATA
"""
