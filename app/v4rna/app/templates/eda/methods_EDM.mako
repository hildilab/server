<%inherit file="base.mako" />

<form action="form" method="post" enctype="multipart/form-data">
    
        <div id="content" class="content">
<!--             <script type="text/javascript">
                document.write("<div class='toggleNice' style='display:none;'>");
            </script> -->
	
            <div>
                <h1>Methods to generate Electron Density Maps</h1>


<h2>Workflow related to CCP4</h2>
<div id="teaser" align="center">
	<img src="/static/img/workflow_ccp4.png" width="800" height="450" alt="workflow" />
	<!-- <img src="/static/img/logo.jpg" alt="example result" /> -->
</div>

<h2>Used programs from CCP4</h2>

<h3>- cif2mtz - Convert an mmCIF reflection file to MTZ format:</h3>
The program cif2mtz uses a procedure of programs to convert an mmCIF reflection
file to MTZ format:<br>

<a target="_blank" href="http://www.ccp4.ac.uk/html/mtzdump.html">MTZDUMP</a> gives a file dump of a standard `MTZ' reflection data file.
<a target="_blank" href="http://www.ccp4.ac.uk/html/unique.html">UNIQUE</a> produces a list of the unique reflections in an MTZ file with the
appropriate cell parameters, symmetry and resolution range.
<a target="_blank" href="http://www.ccp4.ac.uk/html/freerflag.html">FREERFLAG</a> adds a column of free-R flags to the MTZ file, to be used later
for cross-validation and with <a target="_blank" href="http://www.ccp4.ac.uk/html/cad.html">CAD</a> it is added to the dataset MTZ file.
MTZDUMP is used on the output of CAD to get various statistics, including the number
of missing data entries (i.e. Missing Number Flags = unmeasured data) for each column of data. This gives the
completeness of the dataset for the specified resolution range.
<br>If a column of free-R flags is already present in the incomplete dataset, then a
modified procedure is followed:
MTZDUMP is used to give a file dump of a standard `MTZ' reflection data file.
UNIQUE produces a list of the unique reflections.
The output of UNIQUE is merged with the dataset using CAD.
FREERFLAG completes the free-R column. <a target="_blank" href="http://www.ccp4.ac.uk/html/mtzutils.html">MTZUTILS</a> removes the surplus columns originating from UNIQUE.
And MTZDUMP is again used to analyse the dataset.

<p align="center">For more informations: <a target="_blank" href="http://www.ccp4.ac.uk/html/cif2mtz.html">link to "cif2mtz"</a></p>
<h3>- SIGMAA - Improved Fourier coefficients using calculated phases:</h3>

The program SIGMAA is used to combine a set of calculated
phases with a set of previously determined phases for which the phase probability
profiles are held in the form of Hendrickson-Lattman coefficients.
<br><a target="_blank" href="http://www.ccp4.ac.uk/html/sfall.html">SFALL</a> calculates structure factors and X-ray gradients for refinement
using inverse and forward fast Fourier techniques.

<p align="center">For more informations: <a target="_blank" href="http://www.ccp4.ac.uk/html/sigmaa.html">link to "SIGMAA"</a></p>
<h3>- Run FFT - Create Map:</h3>
Run FFT - Create Map

The FFT (Fast Fourier Transform) program may is used to calculate Fouriers and 
difference Fouriers from reflection data. With the help of <a target="_blank" href="http://www.ccp4.ac.uk/html/mapmask.html">MAPMASK</a>, which
is a general map and mask manipulation program fo-fc- and 2fo-fc-maps are created.
The role of the molecule in the map calculation is decided (i.e. the map to cover
'asymmetric unit'or 'all atoms in PDB file'). 

<p align="center">For more informations: <a target="_blank" href="http://www.ccp4.ac.uk/html/fft.html">link to "FFT"</a></p>
<h3>- SFCHECK - quality check & Omit Map:</h3>
SFCHECK is a program for assessing the agreement between the atomic model and X-ray data or EM map.<br>
Amoung other things the program gives information about R-factor, correlation, Luzzati plot, Wilson
plot, Boverall, pseudo-translation, twinning test and local error estimation by
residues.
<br>An total omit map is a way to reduce the model bias in the electron density calculated
with model phases.
First, the initial map is divided into N boxes. For each
box, the electron density in it is set to zero and new phases are calculated from this
modified map. A new map is calculated using these phases and Fobs. This map contains
the omit map for the given box which is stored until the procedure is repeated for
all boxes. At the end, all the boxes with omit maps compose the total omit map.
Phases calculated from the total omit map are combined with the initial phases.
The whole procedure is repeated twice.<br>
<p align="center">For more informations: <a target="_blank" href="http://www.ccp4.ac.uk/html/sfcheck.html">link to "SFCHECK"</a></p>
            </div>
            <script type="text/javascript">
                document.write("</div>");
            </script>
        </div>
</form>