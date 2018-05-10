<h2>Workflow</h2>

<div align="center">
  Move the mouse over the framed areas in the scheme to get additional information.

  <img src="img/scheme.jpg" alt="workflow" border="0" usemap="#workflow" />

  <map name="workflow" id="workflow">
    <area shape="rect" coords="6,109,222,138"  nohref="nohref" onmouseover="Tip('in&nbsp;fasta&nbsp;format or as a plain string')" onmouseout="UnTip();"/>
    <area shape="rect" coords="7,250,224,279"  nohref="nohref" onmouseover="Tip('different levels, to optimize<br/>the prediction for your needs')" onmouseout="UnTip();"/>
    <area shape="rect" coords="7,308,223,338"  nohref="nohref" onmouseover="Tip('specify the type of your protein<br/>to get optimal results')" onmouseout="UnTip();"/>
    <area shape="rect" coords="378,128,481,155" href="http://www.enzim.hu/hmmtop/" target="_blank" onmouseover="Tip('secondary structure prediction<br/>(click&nbsp;to&nbsp;go&nbsp;to&nbsp;applications&nbsp;website)')" onmouseout="UnTip();"/>
    <area shape="rect" coords="320,280,538,324" href="index.php?site=methods&sub=learning" onmouseover="Tip('click to go to <b>Methods &gt; Matrix Prediction</b> for more info')" onmouseout="UnTip();"/>
    <area shape="rect" coords="319,337,538,380" href="index.php?site=methods&sub=databases" onmouseover="Tip('click to go to <b>Methods &gt; Pfam domains</b> for more info')" onmouseout="UnTip();"/>
    <area shape="rect" coords="58,445,500,475" href="index.php?site=methods&sub=prediction" onmouseover="Tip('click to go to <b>Methods &gt; Prediction</b> for more info')" onmouseout="UnTip();"/>
  </map>

</div>

<h2>Overview</h2>
<div class="contentblock">

  <div class="textblock">
    <p>
      RHYTHM combines a structure based prediction method (matrix prediction) with evolutionary information (Pfam-domains) to gain information on the exposure or burial of every transmembrane residue. Moreover, RHYTHM takes into account the structural specificities of membrane proteins with different functions, i.  e. treating channels and transporters (subsumed as <i>channels</i>) different from other membrane proteins (<i>membrane-coils</i>) [{'hildebrand06'|ref}]. RHYTHM also integrates the secondary structure prediction <a href="http://www.enzim.hu/hmmtop/">HMMTOP</a> [{'hmmtop'|ref}].
    </p>
  </div>

  <div class="spaceblock">
    prediction method
  </div>
  
  <div class="textblock">
    <p>
      After the upload of a sequence file and the specification of the prediction matrix (channel or membrane-coil) the prediction process is started. Results are processed within only a few seconds. The graphical output contains information on the secondary structure and topology of the protein as well as specific information on the contact type of each residue and its conservation derived from the Pfam database [{'pfam'|ref}]. The information can be downloaded as a graphical file (for illustration) or a text file (for analysis and statistics).
    </p>
  </div>

  <div class="spaceblock">
    workflow
  </div>

  <div class="textblock">
    <p>
      All computations are done on this server including optional prediction of membrane helix sections and searching for Pfam domains. Modern web technologies (AJAX, JavaScript, PHP, CSS) were used to create a fast and intuitive usable web application.
    </p>
  </div>

  <div class="spaceblock">
    technical
  </div>
  
</div>
