<h2>Prediction</h2>

<div align="center">

  <img src="img/pred-scheme.jpg" />


<!--
  <object data="img/pred-scheme.svg" type="image/svg+xml" width="800px">
    <param name="src" value="img/pred-scheme.svg" />
    <img src="img/pred-scheme.jpg" />
  </object>
-->

</div>

<hr class="h2"/>

<div class="contentblock">

  <div class="textblock">

    <ul>
      <li style="list-style-image:url(img/1.jpg)">
	<p>
	  Matrix prediction: All transmembrane amino acids are scored according to the propensity matrices specific for helix-helix and for helix-membrane contacts. The residues above the specificity threshold for helix-helix contacts (medium, high, very high, highest) in <i>channels</i> are assigned as helix-helix contacts. The specificities for a single contact type range - in steps of 5 - from 75% for medium to 90% for very high thresholds.
	</p>
      </li>


      <li style="list-style-image:url(img/2.jpg)">
	<p>
	  Matrix prediction: The remaining residues are assigned analogous as helix-membrane contact using the helix-membrane contact specific threshold (medium to highest). The specificities for that prediction range from about 75% to 90%. In conjunction maximum of 70% to a minimum of 20% of the residues are assigned by the matrix prediction method at medium to highest specificity thresholds.
	</p>
      </li>

      <li style="list-style-image:url(img/3.jpg)">
	<p>
	  Pfam Prediction: To optimize the coverage of the helix-helix contact prediction, residues not assigned by the matrix prediction method are evaluated using the conservation criterium. The conservation information is drawn using Pfam domains. The Pfam database is searched by HMMER. The HMMER results are limited to a score 20 and an e-value of 0.1 (not shown in above scheme). Only fully conserved residues are rescored. A plus of 10% to 20% residues are additionally assigned thereby.
</p>

<p>
  The bonus for conserved residues is calculated such that the positive predictive value gets optimized. It depends on the selected protein type and the selected specificity level. The values for channels are 0.8 for the highest specificity level and 0.6, 0.3, 0.0 for the levels very high, high, medium; for membrane-coils 0.1, 0.2, 0.5 and 0.5, beginning with the highest level. For channels these boni increase with higher specificity, for membrane-coils they decrease. This is due to the optimization for the selected protein type and supportes the distinction between these. Tables containing the specificity, the corresponding sensitivity and the threshold/cutoff-value for all levels can be <a href="data/sensitivity-specificity_thresholds.zip">downloaded here</a>.
</p>

      </li>
    </ul>

<p>
  The average AUC-values (from a leave one out cross validation) for the prediction of helix-helix contacts is 0.72 for channels and 0.68 for membrane-coils, respectively.
</p>

  </div>

  <div class="spaceblock">
    multistep approach
  </div>  

</div>
