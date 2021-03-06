<%inherit file="base.mako" />

    <div id="content" class="content">
	<h1>FAQ</h1>
	<div class="subcontent">
	    <div class="faq">
		<div class="question">
		    What is it good for?
		</div>
		<div class="answer">
		    Voronoia4RNA provides pre-calculated packing densities for RNA structures. It allows analysis of the internal packing of 
biopolymers, local packing irregularities and packing defects for a broad range of applications.
		</div>
	    </div>
	    <div class="faq">
		<div class="question">
		    What happens to splitted PDB entries?
		</div>
		<div class="answer">
		    Splitted PDB entries are joined to a single PDB file to avoid irregularities in the calculation of the surface. For splitted PDB 
entries that contain more than one biological unit like two ribosomes only the first unit is considered to increase the performance and clarity of the 
visualization.
		</div>
	    </div>
	    <div class="faq">
		<div class="question">
		    What happens to multiple models in a PDB entry?
		</div>
		<div class="answer">
		    For PDB entries with multiple models only the first model is considered.
		</div>
	    </div>
	    <div class="faq">
		<div class="question">
		    What about alternative Locations?
		</div>
		<div class="answer">
		    All PDB structures are pre-filtered. If an alternative location for an atom is given, only the first location is used for the 
calculation of the packing densities.
		</div>
	    </div>
	    <div class="faq">
		<div class="question">
		    What happens to atoms denoted as  heteroatoms in the corresponding PDB file?
		</div>
		<div class="answer">
		    For most heteroatoms no precise radii are available. Therefore the
hetero atoms are treated with standard radii.
		</div>
	    </div>
	    <div class="faq">
		<div class="question">
		    What happens to modified RNA residues?
		</div>
		<div class="answer">
		    Modified RNA residues are treated as heteroatoms (standard radii are used). A future version is planned in which modified residues 
will be replaced by standard residues.
		</div>
	    </div>
	    <div class="faq">
		<div class="question">
		    What means buried or unburied atom?
		</div>
		<div class="answer">
		    Buried means that an atom has no contact with the surrounding solvent. 
		</div>
	    </div>
	    <div class="faq">
		<div class="question">
		    What is a Vol-File?
		</div>
		<div class="answer">
		   A .vol file extends the PDB file format by three additional rows in 
the Header and its atom information by three additional fixed-width columns.
<br>The Header is extended by additional rows (starting with HOLE NUMBER) containing 
the internal cavities. The cavities are defined by their neigbouring atoms.
<br>The atom rows are extended as follows:
<br>Col 67-73, real(7:2): Van-der-Waals-volume -  Volume inside 
Van-der-Waals sphere
<br>Col 74-80, real(7:2): solvent-excluded-volume - Volume in 1.4 
Angstrom layer outside VdW-sphere
<br>Col 82: indicates buried atoms (1=buried, 0=surface)
		</div>
	    </div>
	    <div class="faq">
		<div class="question">
		    What information is given in the extended Vol-Files?
		</div>
		<div class="answer">
		    The original vol-file is extended by additional 
columns which provide the following information:
<br>Col 83-88: packing density
<br>Col 89-94: z-Score of a single atom (only buried atoms)
<br> The z-Score-RMS is added to the header. 
		</div>
	    </div>
	    <div class="faq">
		<div class="question">
		    What is the z-Score-RMS and how can it be interpreted?
		</div>
		<div class="answer">
		    The z-Score is the normalized difference between packing in a sample molecule and a reference and calculates how well the packing of 
buried atoms fits to reference values.
<br>Typical values for the z-Score-rms are:

<br>  0.0       : perfect match, this is definitely an artifact.
<br>  0.8 - 1.2 : nominal for buried atoms
<br>  1.3 - 1.4 : slightly different from the reference, maybe a structure with low resolution.
<br>  1.5 +      : clearly different data; loosely packed structures; erroneous structures.
<br>  3.0 +      : some error in the data or in program usage, e.g. surface atoms compared with       buried ones.

		</div>
	    </div>
            <div class="faq">
                <div class="question">
                    How are water molecules and other heteroatoms treated?
                </div>
                <div class="answer">
                    Non-water heteroatoms are only considered if they 
are in close contact (2.8 Angstrom) to the rest of the structure. Water 
molecules only contribute to the calculation of of the packing density 
if they are inside of cavities to avoid packing defects. All other water 
molecule that are outside of the calculated surface are ignored.
                </div>
            </div>

	    <div class="faq">
		<div class="question">
		    What residue definitions are used (ProtOr)?
		</div>
		<div class="answer">
		    To define a single atom in the pdb the ProtOr radii set is used. To look up a particular definition click <a href="static/files/RNAProt.resi-def.dat">here</a>.
		</div>
	    </div>
	    <div class="faq">
		<div class="question">
		    How often is Voronoia4RNA updated?
		</div>
		<div class="answer">
		    Voronoia4RNA is updated regularly, but at least every three month.
		</div>
	    </div>
	    <div class="faq">
		<div class="question">
		    There are problems showing the results in the built-in molecular viewer Provi.
		</div>
		<div class="answer">
Java must be installed in order to make Provi available. Make sure you are running an updated version of Java. If problem persists, please refer to the troubleshooting page or contact us.<br><br>

- The 3D protein viewer component in Provi relies entirely on Jmol which requires a working Java installation. To test weather your combination operating system, web browser and Java supports Jmol, 
please visit <a href="http://jmol.sourceforge.net/browsercheck/" target="_blank">this page</a>.<br><br>

- When you see the following message "Error in Internet Explorer 9: 'We were unable to return you to your webpage, Internet Explorer has stopped trying to restore this website. It appears that the 
website continues to have a problem'", you need to either update your Java installation or activate the 'Compatibility View' in Internet Explorer 9. For detailed instructions please see <a 
href="http://support.microsoft.com/kb/2506617" target="_blank">this support article</a> from Microsoft.<br><br>

- Active X Filtering in Internet Explorer 9 can cause the Jmol Applet not to load, resulting in a large blank area on the left side of the browser window. See <a 
href="http://wiki.jmol.org/index.php/Support/Windows" target="_blank">here</a> or <a href="http://www.mydigitallife.info/ie9-java-applet-not-loading-nor-working-blank-fix/" target="_blank">here</a> on 
how to fix this.<br><br>

- To test weather Java Applets in general are working on your computer, please consult <a href="http://www.java.com/en/download/testjava.jsp" target="_blank">this page</a> and if necessary follow the 
suggestions there.<br><br>

- If your problem persists, please do not hesitate to contact us via <a href="mailto:alexander.rose@charite.de">email</a>
		</div>
	    </div>
	</div>
    </div>
