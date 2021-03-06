<%inherit file="base.mako" />

<form action="form" method="post" enctype="multipart/form-data">
    <div id="content" class="content">
<!--       <script type="text/javascript">
	document.write("<div class='toggleNice' style='display:none;'>");
      </script> -->
      <h1>VORONOIA 4 RNA </h1>
      <div id="teaser" align="center">
	<img src="static/img/logo_v4rna.png" width="30%" height="30%" alt="logo" />
	<!--<img src="/static/img/logo.jpg" width="100" height="100" alt="logo" /> -->
	<!-- <img src="/static/img/logo.jpg" alt="example result" /> -->
      </div>
      <h2>Motivation</h2>

	<div class="middleblock">
	  <p>
	    
	  <h3>A method to calculate atomic packing and packing defects</h3>
Voronoia4RNA is a database storing data on atomic packing densities of RNA structures and complexes. Compared to other methods, that solely estimate van 
der Waals interactions i.e. by gain of solvent excluded surfaces, Voronoia4RNA allocates the free space between neighbouring atoms. It explicitly takes 
packing defects into consideration and is therefore an appropriate method to calculate van der Waals interactions and to estimate the underlying forces.
<br>
<h3>On site visualization</h3>
Packing densities and water sized cavities can be visualized by the Jmol based viewer Provi. Visualisation allows to quickly evaluate these cavities that 
often refer to internal waters not resolved in the crystal structure. Regions with large packing defects i.e. in ribosomes or riboswitches also refer to 
local flexibilities. Packing densities are also considered as a tool to assess the quality of a structure, as this measure correlates with X-ray 
structure resolution. In some cases, Voronoia4RNA may also be used to detect potential binding sites for ligands or coenzymes. 
<br>
<h3>What you can do ...</h3>
You may browse a pre-calculated set of RNA structures, visualize or download sub-datasets or individual entries, submit your own protein or RNA structure 
for calculation and compare it to reference values calculated from a set of non-redundant RNA structures by means of a given z-Score.

	    <br/>
	  </p>


      </div>
      <script type="text/javascript">
	document.write("</div>");
      </script>
    </div>
</form>
