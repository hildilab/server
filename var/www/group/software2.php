<html lang="en">
<head>
	<link rel="stylesheet" type="text/css" href="stylesheetHawai.css">
	<title>Software</title>
</head>
 <body>
	   <div align="center">
 <div class="seitenbereich">

	<?php
	include("navi.html");
	?>

	<h1 style="margin-left: auto; margin-right: auto; text-align: center;">Software</h1>


	<br>
	<table style="margin-left: auto; margin-right: auto; width: 80%">
	<tr>
	<td><img src="fragfit.jpg" width="300"></td>
	<td><img src="mdsrv.jpg" width="300"></td>
  <td><img src="water.jpg" width="300"></td>
	</tr>
  <tr>

    <th><a target="_blank" href="http://proteinformatics.charite.de/ngl-tools/fragfit/start.php">FragFit</a></th>
    <th><a target="_blank" href="http://nglviewer.org/mdsrv/index.html">MDsrv</a></th>
    <th><a target="_blank" href="http://proteinformatics.charite.de/mppd/">MP:PD</a></th>
	</tr>
	<tr>
	<td valign="top"><br>FragFit is an interactive web service for guided modeling of missing segments such as loops or hige regions into cryo-Electron Microscopy (cryo-EM) density maps.
    Segments of up to 3-35 residues length can be effectively modeled into maps of different resolution. Fragments are taken from a precalculated and frequently updated database extracted from structural coordinates deposited in the PDB. <br>
    A fast hierarchical search algorithm selects up to 100 suitable fragments by using sequence similarity and geometrical fitting as evaluation criteria. The found fragments are then reranked by their cross-correlation to the user provided cryo-EM density map.  </td>
	<td valign="top"><br>
    MDsrv is a web-based tool developed to enhance collaborative research by providing non-experts with easy and quick on-line access to molecular dynamics (MD) simulations. <br>
    As a member of the nglviewer family, MDsrv channels MD trajectories through a web server using a powerful web application (NGL viewer) to visualize them. </td>
<td valign="top">
<br>
    MP:PD is a comprehensive database of helical membrane proteins featuring internal atomic packing densities, internal cavities and internal waters.

</td>
	</tr>
  <tr>
	<td style="padding-top: 20px;"><img src="ngl2.jpg" width="300"></td>
	<td style="padding-top: 20px;"><img src="rhythm2.jpg" width="300"></td>
  <td style="padding-top: 20px;"><img src="sl22.jpg" width="300"></td>
	</tr>
  <tr>

    <th><a target="_blank" href="http://proteinformatics.charite.de/ngl-tools/ngl/doc/index.html#User_manual/Introduction/Welcome">NGL</a></th>
    <th><a target="_blank" href="http://proteinformatics.charite.de/rhythm/">RHYTHM</a></th>
    <th><a target="_blank" href="http://proteinformatics.charite.de/ngl-tools/sl2/start.php">SL2</a></th>
	</tr>
  <tr>
	<td valign="top"><br>NGL is an online viewer for proteins and other molecular structures. It is intended for users of the web application including a graphical interface and for developers who want to use NGL in their own projects.
</td>
	<td valign="top"><br>
    Starting from a given protein sequence, secondary and tertiary structure information is calculated by RHYTHM within only a few seconds. <br>
		To account for different packing motifs the program uses various approaches for the prediction of channels and transporters (channels) or other membrane proteins (membrane-coils), respectively. The prediction applies structural information from a growing data base of precalculated packing files and evolutionary information from sequence patterns conserved in a represantative dataset of membrane proteins (pfam-domains). </td>
<td valign="top">
<br>
    SuperLooper2 is an interactive web service for the insertion of missing segments such as loops in proteins. <br>
    Loop candidates are selected from a precalculated database containing ~700 million protein fragments with a residue length of 3-35. The fragments are extracted from structural coordinates deposited in the RSCB PDB.

</td>
	</tr>
  <tr>
  <td style="padding-top: 20px;"><img src="eda.jpg" width="300"></td>
  <td style="padding-top: 20px;"><img src="v4rna.jpg" width="300"></td>
  </tr>
  <tr>
    <th><a target="_blank" href="http://proteinformatics.charite.de/eda/tools/eda/index">ValiDen</a></th>
    <th><a target="_blank" href="http://proteinformatics.charite.de/voronoia4rna/tools/v4rna/index">voronoia4rna</a></th>
  </tr>
  <tr>
  <td valign="top"><br>The ValiDen webserver generates electron density maps. As a highlighting feature ValiDen provides the opportunity to convert the formats of electron microscopy maps (e.g. CCP4, X-PLOR, DSN6, BRIX) via the program MAPMAN in feasible map formats (e.g. MAP) for representation of EM-maps in e.g. COOT or PyMOL.</td>
  <td valign="top"><br>
  Voronoia4RNA is a database storing data on atomic packing densities of RNA structures and complexes.
  Compared to other methods, that solely estimate van der Waals interactions i.e. by gain of solvent excluded surfaces, Voronoia4RNA allocates the free space between neighbouring atoms.
  <br>It explicitly takes packing defects into consideration and is therefore an appropriate method to calculate van der Waals interactions and to estimate the underlying forces. </td>

  </tr>
	</table>
	<br>
	<br>
	<br>

	</div>
	</div>
</body>
</html>
