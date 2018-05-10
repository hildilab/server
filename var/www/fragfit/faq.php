<!doctype html>

<html lang="en">
<head>
	<link rel="stylesheet" type="text/css" href="stylesheet.css">
	<title>FAQ</title>
</head>
<body>
	<div id="container">
	<?php
	include('navi.html');
	?>	
	</div>
	<div id="content" class="content">
		<h1>Frequently asked questions</h1> 
		<h4>Is a registration required?</h4>
		<br>No, FragFit is free for all users and no login is required.
		<h4>Which web-browsers are supported?</h4>
		<br>Every modern web-browser that supports WebGL. To check the compatibility of your
			browser and further information see the <a target="_blank" href=https://github.com/arose/ngl#browser-support>NGL documentation</a>.
		<h4>How do I use the NGL viewer?</h4>
		<br>A complete documentation of the NGL viewer can be found
			<a target="_blank" href="http://proteinformatics.charite.de/ngl-tools/ngl/doc/index.html#User_manual/Introduction/Welcome">here</a> and a Tutorial video <a target="_blank" href="https://youtu.be/6TjtE8c4Ys8">here</a>.
		<h4>Do I have to install a plugin to use the NGL viewer?</h4>
		<br>No, the NGL viewer is based solely on browser technologies
			that are provided by every modern web-browser. Additional
			installations are not needed. Please make sure that you have updated your browser
			to the latest version.
		<h4>What is the purpose of FragFit?</h4>
		<br>FragFit can be used to interactively insert protein segments, such as loops of 3 to 35
			residues length, into gaps of protein structures guided by a cryo-EM density map.
		<h4>What has to be provided to start a search?</h4>
		<br>The user has to upload a protein and a cryo-EM density map (upload of compressed files possible), specify the sequence of the destined
			segment, the two stem residues of the gap where the segment has to be inserted and the resolution of the map.
		<h4>I get no results, what might be the problem?</h4><br>
			In some rare cases (too long or too short sequences for the given stem distance) no suitable
			loops can be found. Try to extend the loop search by one amino acid in C- or N-terminal direction. Additionally, the chains must contain the same name.
		<h4>Is the upload saved at the server?</h4>
		<br>No, the results are deleted after reload of the website.
		<h4>Why are the sequence and the stems not further enlonged?</h4><br>
			In this case the end of the protein chain is reached. Try to enlong in the other direction.

		<h4>What does the color range stand for?</h4>
		<br>The different colour schemes range from its min to its max value.
		<br>Clash scheme: white (no clashes) to orange to red (many)
		<br>SequenceID scheme:  dark green (high) to light green (low)
		<br>Score scheme: green (high score --> better results) to blue (medium) to purple (low)
		<br>Correlation sheme: dark blue (high score --> better results)to  light blue to yellow (low)
		<h4>Can the completed structure be downloaded from the server?</h4>
		<br>As soon as a suitable fragment is found and selected by the user,
			the structure can be downloaded with the inserted fragment which
			sequence is automatically mutated to the destined sequence provided
			by the user.
		<h4>Are the sidechains included in density fitting?</h4>
		<br>Sidechains are not considered automatically during modeling, only the backbone is used. The user can visually analyse the results in context of side-chain composition. The included sidechains are not optimized.
		<h4>Are the sidechains of the loop included in the download?</h4>
		<br>We add sidechains in a standard configuration.
			This might lead to clashes. Please have in mind
			that an energy minimization might be necessary
			before further usage of the model.
		<h4>What is included in the different download files?</h4>
		<br>All found loops can be downloaded in a single PDB-file where the individual loops are separated by a model tag.<br>
			A single loop can be downloaded renumbered and inserted at the correct position in the user-provided structure file.
		<h4>What map formats are supported?</h4>
		<br>FragFit supports MRC and CCP4 (MAP) file formats. They can be uploaded in a compress manner.
		<h4>Do stem residues have to be included in the search sequence?</h4>
		<br>No, please only include the search sequence.
		<h4>Can I remodel regions prior to deletion?</h4>
		<br>Yes, clashes are not automatically sorted out but stated in the result table. The loop will automatically be exchanged.
		<h4>Can modifications like carbohydrate modifications provide difficulties?</h4>
		<br>No.
		<h4>Up to which map sizes can be used?</h4>
		<br>We do not have a size limitation but strongly recommend to minimize the map size as much as possible as those files have to be transmitted to our server. This will also speed up results.
		<h4>How can a run be restarted?</h4>
		<br>Up to now, a FragFit session can only be restarted upon reloading of the webpage.

		<h4>How can my results be validated?</h4>
		<br>
		A validation can be done by using <a href="http://molprobity.biochem.duke.edu/">MolProbity</a>. For the given example sets we found that Fragfit could improve the MolProbity Score. It can happen that 		the downloaded structure from Fragfit can not be uploaded to MolProbity, if that happens do the following: Copy the atoms of the loop from the Fragfit result into the original pdb and delete the 		original loop, then upload this file.
        </div>

         </div>
   	<?php
	include('footer.html');
	?>
    </div>

    <!-- Insert your content here -->
</body>
</html>
