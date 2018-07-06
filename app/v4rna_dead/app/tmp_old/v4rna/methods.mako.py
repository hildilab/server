# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1467656988.753368
_enable_loop = True
_template_filename = '/home/webit/app/v4rna/app/templates/v4rna/methods.mako'
_template_uri = 'v4rna/methods.mako'
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
        __M_writer = context.writer()
        __M_writer(u'\n\n<form action="form" method="post" enctype="multipart/form-data">\n    \n        <div id="content" class="content">\n<!--             <script type="text/javascript">\n                document.write("<div class=\'toggleNice\' style=\'display:none;\'>");\n            </script> -->\n\t\n            <div>\n                <h1>Calculation, Packing density and Cavities</h1>\n\n<h2>Calculation</h2>\n\nVoronoia4RNA calculates atomic volumes by applying the Voronoi Cell algorithm described in <a target="_self"  href="')
        __M_writer(unicode(h.url_for('tools/v4rna/references')))
        __M_writer(u'">[2]</a>. The volume calculated for each atom is split into two portions, \nboth of which are represented in the .vol files produced by the server. The first is the vdW volume (the volume inside an atoms\' van der Waals sphere), the second is the solvent excluded volume (within a 1.4 Angstrom layer around \nthe vdW sphere). The space is allocated among atoms using hyperboloid surfaces. The calculation is performed by applying a cubic lattice of 0.1 Angstrom grid width.\n<br>\nCavities are found by applying a Delaunay triangulation and looking for edges above a cutoff length in the resulting graph corresponding to a 1.4 Angstrom probe radius. Their locations are approximated by the center of mass of all neighboring atoms.\n<br>\n<br>\nThe core algorithm of Voronoia4RNA has been implemented in Delphi and an intermediate layer in Python. The core algorithm calculates atomic volumes and cavities from PDB structures, prefiltered for modifications. It produces modified PDB files from which packing densities, cavity positions, and tabular reports containing average volumes and densities are calculated.\n<br>\n<br>\n<h3>Visualization</h3>\n<br>\nFor visualization of packing densities and cavities, the Jmol based viewer Provi can be used directly on the website (Oracle Java is needed). \nThe atomic packing density is represented by a colour scale which is given by the range of the minimal and maximal packing density values or a \nuser defined range.\n<br>Cavities can be visualized schematically as balls, which is the appropriate way for large structures as ribosomes containing hundreds of cavities, \nor by their exact shape.\n<h2>Packing density</h2>\n\nThe atomic packing density quantifies the space between atoms. It allows a better approximation of van der Waals contacts and surfaces (and thus forces) \nthan the simple calculation of solvent excluded surfaces that does not respect packing defects enclosed therein. It uses two portions of atomic volume, \nthe van der Waals volume V(vdW) (inside the van der Waals radius), and the solvent excluded volume V(se) (a 1.4 Angstrom layer cushioning the vdW sphere). \nThe Voronoi Cell algorithm <a target="_self"  href="')
        __M_writer(unicode(h.url_for('tools/v4rna/references')))
        __M_writer(u'">[9]</a> calculates, how much of the V(vdW) and V(se) is \noccupied by other atoms. The packing density (PD) is then calculated from the remaining volumes V(vdW) and the sum of V(vdW) and V(se). \n<br>\n<br>\nPD = V(vdW) / [V(vdW) + V(se)]\n<br>\n\n<h2>Cavities</h2>\n\nCavities are locations inside a structure big enough to enclose at least one water molecule. In our calculations a probe of 1.4 Angstrom radius, that is \nused to model the cavities shape, must be trapped inside the cavity, i.e. no tunnels to the outside exist. Cavities are frequently found in protein \ndomains above 150 amino acids or RNA structures above 200 nucleotides. Many of them are presumably filled with water that is often not resolved in the \ncrystal structures. \n</div>\n\n\n            <script type="text/javascript">\n                document.write("</div>");\n            </script>\n        </div>\n</form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"33": 1, "34": 15, "35": 15, "36": 37, "37": 37, "43": 37, "27": 0}, "uri": "v4rna/methods.mako", "filename": "/home/webit/app/v4rna/app/templates/v4rna/methods.mako"}
__M_END_METADATA
"""
