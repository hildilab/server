<%inherit file="base.mako" />

<form action="form" method="post" enctype="multipart/form-data">
    
        <div id="content" class="content">
<!--             <script type="text/javascript">
                document.write("<div class='toggleNice' style='display:none;'>");
            </script> -->
	
            <div>
                <h1>Calculation, Packing density and Cavities</h1>

<h2>Calculation</h2>

Voronoia4RNA calculates atomic volumes by applying the Voronoi Cell algorithm described in <a target="_self"  href="${h.url_for('tools/v4rna/references')}">[2]</a>. The volume calculated for each atom is split into two portions, 
both of which are represented in the .vol files produced by the server. The first is the vdW volume (the volume inside an atoms' van der Waals sphere), the second is the solvent excluded volume (within a 1.4 Angstrom layer around 
the vdW sphere). The space is allocated among atoms using hyperboloid surfaces. The calculation is performed by applying a cubic lattice of 0.1 Angstrom grid width.
<br>
Cavities are found by applying a Delaunay triangulation and looking for edges above a cutoff length in the resulting graph corresponding to a 1.4 Angstrom probe radius. Their locations are approximated by the center of mass of all neighboring atoms.
<br>
<br>
The core algorithm of Voronoia4RNA has been implemented in Delphi and an intermediate layer in Python. The core algorithm calculates atomic volumes and cavities from PDB structures, prefiltered for modifications. It produces modified PDB files from which packing densities, cavity positions, and tabular reports containing average volumes and densities are calculated.
<br>
<br>
<h3>Visualization</h3>
<br>
For visualization of packing densities and cavities, the Jmol based viewer Provi can be used directly on the website (Oracle Java is needed). 
The atomic packing density is represented by a colour scale which is given by the range of the minimal and maximal packing density values or a 
user defined range.
<br>Cavities can be visualized schematically as balls, which is the appropriate way for large structures as ribosomes containing hundreds of cavities, 
or by their exact shape.
<h2>Packing density</h2>

The atomic packing density quantifies the space between atoms. It allows a better approximation of van der Waals contacts and surfaces (and thus forces) 
than the simple calculation of solvent excluded surfaces that does not respect packing defects enclosed therein. It uses two portions of atomic volume, 
the van der Waals volume V(vdW) (inside the van der Waals radius), and the solvent excluded volume V(se) (a 1.4 Angstrom layer cushioning the vdW sphere). 
The Voronoi Cell algorithm <a target="_self"  href="${h.url_for('tools/v4rna/references')}">[9]</a> calculates, how much of the V(vdW) and V(se) is 
occupied by other atoms. The packing density (PD) is then calculated from the remaining volumes V(vdW) and the sum of V(vdW) and V(se). 
<br>
<br>
PD = V(vdW) / [V(vdW) + V(se)]
<br>

<h2>Cavities</h2>

Cavities are locations inside a structure big enough to enclose at least one water molecule. In our calculations a probe of 1.4 Angstrom radius, that is 
used to model the cavities shape, must be trapped inside the cavity, i.e. no tunnels to the outside exist. Cavities are frequently found in protein 
domains above 150 amino acids or RNA structures above 200 nucleotides. Many of them are presumably filled with water that is often not resolved in the 
crystal structures. 
</div>


            <script type="text/javascript">
                document.write("</div>");
            </script>
        </div>
</form>
