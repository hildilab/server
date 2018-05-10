<!doctype html>

<html lang="en">
<head>
    <link rel="stylesheet" type="text/css" href="stylesheet.css">
    <title>Manual</title>
</head>
<body>
    <div id="container">
	<?php
	include('navi.html');
	?>
    </div>
    
 <div id="content" class="content">
     <div>
         <h1>Tutorial</h1>
    
           
    <table><tbody>
    <h3>Usage tutorial</h3>

	<iframe style="width:560px; height:315px; margin:0 auto;"  src="https://www.youtube.com/embed/zF4TyKTw4Pg?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
<br>
<a>Or watch the video at youtube: <a target="_blank" href="https://www.youtube.com/watch?v=zF4TyKTw4Pg">https://www.youtube.com/watch?v=zF4TyKTw4Pg</a>.
</a>
	<h3>Example sets</h3>
		<h4>Cryo-EM structure of the human gamma-secretase complex at 3.4 angstrom resolution.</h4>
			<ol>
				<li>Download the map from <a target="_blank" href="https://www.ebi.ac.uk/pdbe/emdb/">EMDB</a>: <a href="ftp://ftp.ebi.ac.uk/pub/databases/emdb/structures/EMD-3061/map/emd_3061.map.gz">EMD-3061</a> and upload it to the <a href="http://proteinformatics.charite.de/ngl-tools/fragfit/?plugin=FragFit">server</a> via the form after starting a new FragFit Job. The file can be uploaded in a compressed format.</li>
				<li>Download PDB file: <a href="http://www.ebi.ac.uk/pdbe/entry-files/download/pdb5a63.ent">5a63</a> and upload it to the server via the form. ".pdb", ".ent" and a compression is possible for uploading.</li>
				<li>
					Type in the stem residues:
					<br>Stem residue 1: 473:A
					<br>Stem residue 2: 482:A
				</li>
				<li>Type in the missing sequence: EDLNFVT</li>
				<li>Add the map resolution: 3.4</li>
				<li>Press start.</li>
				<li>Visualize results.</li>
			</ol>
			Download further example data sets here:<br>
			<ul>
				<li><a href="data/5oby.zip">5oby</a> (resolution: 3.75 Angstrom)</li>
				<li><a href="data/6bo8.zip">6bo8</a> (resolution: 3.6 Angstrom)</li>
			</ul>
			
<h3>Validation</h3>
A validation can be done by using <a href="http://molprobity.biochem.duke.edu/">MolProbity</a>. For the given example sets we found that Fragfit could improve the MolProbity Score. It can happen that the downloaded structure from Fragfit can not be uploaded to MolProbity, if that happens do the following: Copy the atoms of the loop from the Fragfit result into the original pdb and delete the original loop (if present), then upload this file.

</div> </div>
   </div>
   	<?php
	include('footer.html');
	?>
    </div>
</body>
</html>
