<%inherit file="base.mako" />

    <div id="content" class="content">
	<h1>FAQ</h1>

	<div class="subcontent">
	    <div class="faq">
		<div class="question">
		    Why do I get an error?
		</div>
		<div class="answer">
		    Please make sure, you loaded an sf-mm.cif or an mtz file. An example
		    of such a file can you find on this site. If the error is still there
		    please send us a mail.
		</div>
	    </div>
	    <div class="faq">
		<div class="question">
		    How can I see the maps in coot?
		</div>
		<div class="answer">
		    Start COOT, then open the pdb-file via 'File -> Open Coordinate'.
		    Then open the maps via 'File -> Open Map'. For the fofc-map
		    select 'difference map'. You can display or hide single maps on 'Display Manager'.
		    For more informations, please visit the <a href="http://biop.ox.ac.uk/coot/" target="_blank">website</a>.
		</div>
	    </div>
	    <div class="faq">
		<div class="question">
		    How can I see the maps in pymol?
		</div>
		<div class="answer">
		    Start PYMOL, then open the pdb-file and the density-map via 'File -> Open'.
		    By selecting action and then mesh, you can make the map visible
		    For more informations, please visit the <a href="http://www.pymol.org/" target="_blank">website</a>.
		</div>
	    </div>
<h4>Example of a CIF-file of structure factor amplitudes:</h4>
          data_structure_9ins<br>
          _entry.id  9ins  <br>
          _cell.length_a      100.000<br>
          _cell.length_b      100.000<br>
          _cell.length_c      100.000<br>
          _cell.angle_alpha    90.000<br>
          _cell.angle_beta     90.000<br>
          _cell.angle_gamma    90.000<br>
          _symmetry.space_group_name_H-M  'P 1 21 1'<br>
	  _reflns.d_resolution_high          3.200<br>
	  _reflns.d_resolution_low         48.224<br>
          loop_<br>
          _refln.index_h<br>
          _refln.index_k<br>
          _refln.index_l<br>
	  _refln.status<br>
          _refln.F_meas_au<br>
          _refln.F_meas_au_sigma<br>
             2  3   4    12.3   1.2<br>
            -2 -3  -4    11.4   1.1<br>
           . . . . . . . . . . . . .<br><br>

<h4>Definition of the density files</h4>
	          <div id="teaser" align="center">
	<!--<img src="/static/img/h-two.png" width="300" height="300" alt="logo" />-->
	<img src="/static/img/h-two.png"  width="800" height="275" alt="example result" />
      </div>
      A density map shows, where would be space for example for a residue or a water.
      It also shows, if a residue could have another orientation.<br>
	    
	</div>
    </div>