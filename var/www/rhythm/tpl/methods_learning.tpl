<h2>Matrix prediction</h2>
<div class="contentblock">

  <div class="textblock">
    <p>
      The prediction of buried vs. exposed residues is based on two different
      sets of propensity matrices derived from representative and non-redundant datasets of
      21 channels and 14 membrane-coils (<a href="data/protein_data.zip">dataset</a>). The data 
      were first selected and analyzed as described in [{'hildebrand06'|ref}]. In the matrices the propensity of all amino acids to contact another helix, the membrane or water, is stored for every position (i. e. at the contact, at position +2 or -4 relative to the contact). The propensity matrices are shown below and available for <a href="data/propensity_matrices.zip">download</a> (including corresponding standard deviation matrices based on all subsets excluding one protein).
      <br/>
      The matrices are regularly updated using the growing information on high resolution membrane protein structures (see <a href="http://blanco.biomol.uci.edu/Membrane_Proteins_xtal.html">here</a> for an overview). The last analysis and evaluation published in 2006 was based on a data set that was only about half the size of the present data set. It resulted in an AUC (area under curve = sensitivity/specificity) prediction value of up to <b>76%</b> [{'hildebrand06'|ref}]. With the updated data set the accuracy of the prediction enhanced by <b>3-5%</b>. With growing data a continuous improvement of the predictions is expected.    
    </p>

  </div>

  <div class="spaceblock">
    datasets<br/>&amp;&nbsp;matrices
  </div>
  
  <div class="textblock">

    <p>
      The propensity of an amino acid is normalized measure describing the tendency of the residue to be buried or exposed.
      <span class="moreLess"></span>
    </p>
    <p>
      For an amino acid for a certain contact type (e. g.
      buried) it is calculated by dividing the fraction of this type of
      contact showing the specified amino acid by the fraction of all
      other contacts showing the specified amino acid and by taking the logarithm
      of this value. A 2D (position specific) matrix is generated from the propensities of all amino acids at different positions relative to the contact. To predict whether an amino acid is buried or exposed the amino acid position itself and all the neighboring positions up to a specified window
      width are assessed as well [{'hildebrand06'|ref}].

    </p>

  </div>

  <div class="spaceblock">
    propensities
  </div>
  

  <!--
      </div>
      &nbsp;
      <br/>
      <hr/>

      <div class="contentblock">
	-->

  <div class="textblock">

    <p>
      In the helix-helix matrix of channels a clear periodicity of 4.0 is observed, while in membrane-coils the periodicity is 3.5 [{'hildebrand06'|ref}].
      <span class="moreLess"></span>
    </p>
    <p>
The best predictions for channels are obtained with the channels scale using a window width of 4 amino acids. For membrane-coils, best predictions are obtained with the membrane-coils scale and a window width of 7 amino acids. The different periodicity correlates with the different packing modes of the transmembrane helices that is <i>right-handed</i> crossing angles in channels and <i>left-handed</i> crossing angles in membrane-coils [{'hildebrand08'|ref}].
    </p>

  </div>

  <div class="spaceblock">
    RHYTHM
  </div>

  <div class="textblock">
    <p>
      For the prediction of the 5th amino acid <b>S</b>erin in the sequence <span style="font-size:16px; font-family:Lucidatypewriter, monospace;">GEIP<b>S</b>KASE</span> the score is calculated as follows.
      <span class="moreLess"></span>
    </p>
    <p>
      Using the channel matrix the score is 0.54 + (-0.19) + 0.21 + 0.38 + <b>1.12</b> + (-0.25) + 0.19 + 0.44 + 0.59 = 3.03. In general it holds that the score for Ser at position 0 is with 1.12 quite high. Therefore Ser occurs often at position 0 in helices of channel membrane proteins. The same  accounts for Ser at positions +4 and -4. By contrast, Lys at position 0 has with -2.06 a very low value. The same accounts for Lys at positions +4 and -4.
    </p>

  </div>

  <div class="spaceblock">
    prediction
  </div>

</div>

&nbsp;
<br/>

<h2>Propensity matrices</h2>

<div class="contentblock">
  
  <div class="textblock">

    <p>
      The propensity matrices are also available in a single zip <a href="data/propensity_matrices.zip">file</a>.
    </p>

  </div>

  <div class="spaceblock">
    download
  </div>

</div>

&nbsp;
<br/>

<div align="center">
  {foreach from=$propMatrices item=a}
  {include file=methods_learning_matrix.tpl}
  <br/>
  {/foreach}
</div>
