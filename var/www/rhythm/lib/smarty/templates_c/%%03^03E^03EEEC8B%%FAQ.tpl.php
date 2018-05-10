<?php /* Smarty version 2.6.20, created on 2018-05-02 07:55:17
         compiled from FAQ.tpl */ ?>
<h1>FAQ</h1>

<div class="subcontent">

  <div class="faq">
    <div class="question">
	How are transmembrane helix sections determined from the protein sequence?
    </div>
    <div class="answer">
	The prediction of the secondary structure of membrane proteins is one of the best working approaches in bioinformatics. Here we installed <a href="http://www.enzim.hu/hmmtop/">HMMTOP</a> to do the prediction automatically. It reliably predicts the position and membrane topology (in-out). However, the exact borders of the membrane spanning helices are generally not predicted that well. Therefore, RHYTHM allows the user to specify this and other information manually.
    </div>
  </div>

  <div class="faq">
    <div class="question">
      What is the basis for the prediction of tertiary structure contacts?
    </div>
    <div class="answer">
      The knowledge based method underlying the contact prediction uses structural and evolutionary information derived from a regularly updated, non-redundant data set of membrane protein structures based on the PDB (see <a href="./index.php?site=methods&sub=learning">Methods &gt; Matrix prediction</a>) and from the <a href="http://pfam.sanger.ac.uk/" target="_blank">Pfam-domains</a> (see <a href="./index.php?site=methods&sub=databases">Methods &gt; Pfam domains</a>).
    </div>
  </div>

  <div class="faq">
    <div class="question">
      Why are different matrices used for the prediction of channels and transporters (<i>channels</i>) and other membrane proteins (<i>membrane-coils</i>)?
    </div>
    <div class="answer">
      The amino acid composition of channels and membrane-coils differs significantly, according to their different architecture. Different types of helix crossing angles lead to different contact RHYTHMs. Generally, in channels small and weakly polar amino acids are buried between helices, while in membrane-coils polar amino acids have higher propensities. In channels the RYHTHM of helix-helix contacts is every 4th residue, in membrane-coils every 3.5th residue. 
   </div>
  </div>

  <div class="faq">
    <div class="question">
      Why are conserved residues regularly involved in helix-helix contacts?
    </div>
    <div class="answer">
      The interaction of helices is quite specific and determines together with the loop structures the 3-D fold. Amino acids that are part of helix-helix interactions are thus evolutionary conserved. By contrast, exposed residues are highly variable for the unspecific interaction with the lipids only requires a hydrophobic character of the amino acid.  
    </div>
  </div>

  <div class="faq">
    <div class="question">
      How are the two different prediction methods (contact matrix and Pfam-domains) combined?
    </div>
    <div class="answer">
      In a multistep prediction approach we first predict helix-helix and helix-membrane contacts using the matrix prediction method at high specificity. To increase the sensitivity of the prediction a downstream prediction using conservation criteria is performed (see <a href="./index.php?site=methods&sub=prediction">prediction</a>).
    </div>
  </div>

  <div class="faq">
    <div class="question">
      How can the results from the predictions of RHYTHM help to obtain low resolution models for membrane proteins?
    </div>
    <div class="answer">
      Due to the optimization of RHYTHM for high specific predictions (check: different default parameters: medium to very high) reasonable information about residues that are important for helix-helix interactions and tertiary structure folding becomes available. That can be used as additional spatial constraints during modeling of a membrane protein. Homology models built on the background of low homology (e.g. &lt; 50%) could be further refined. 3D contacts are directly viewable in <a href="http://pymol.sourceforge.net">PyMOL</a> with the model, if the indices of the sequence you uploaded to RHYTHM and those in your model exactly map to the same residues. For the secondary structure prediction of membrane proteins is highly reliable, it can be used to derive preliminary <i>de novo</i> models. These models could be validated with experimental methods i.e. mutation analysis, or cross linking.  
    </div>
  </div>



<!--
  <div class="faq">
    <div class="question">
	something with specificity vs. sensitivity
    </div>
    <div class="answer">
	... Optimizing for sensitivity while keeping the positive predictive value good. 
    </div>
  </div>
-->


</div>