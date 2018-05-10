<?php /* Smarty version 2.6.20, created on 2018-03-28 16:37:45
         compiled from helix_result.tpl */ ?>


<!--
<h3 id="helpToggle" class="toggleNext">Help</h3>
<div>
  <ul>
    <li>I can put some help here...</li>
  </ul>
</div>
-->

<?php if (isset ( $this->_tpl_vars['waitTplFile'] )): ?>
<h3>
  Update
  <span class="help">The searching for Pfam domains is done in the background,<br/>while you can already see first results.<span class="hline"></span>If this says 'still searching...' for several minutes you may try to click the update-button below.</span>
</h3>	
<p><a id="hmmerStatusLink" href="index.php?<?php echo $this->_tpl_vars['params']; ?>
">click to see if there were conserved amino acids via pfam domains found?</a></p>
<?php endif; ?>


<?php if (isset ( $this->_tpl_vars['update'] )): ?>
<h3 id="adjustToggle" class="toggleNext">Adjust</h3>
<div class="formSettings" align="center">
  <form enctype="multipart/form-data" action="index.php?<?php echo $this->_tpl_vars['updateParams']; ?>
" method="POST">
    <?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "helix_form_settings.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>
  </form>
</div>
<?php endif; ?>

  <h3>Results</h3>	
  <div>
    <?php if (isset ( $this->_tpl_vars['example'] )): ?>
    <p>Example: <?php echo $this->_tpl_vars['example']; ?>
, <a href="examples/<?php echo $this->_tpl_vars['example']; ?>
.pdb">PDB</a></p>
    <?php endif; ?>

    <p>
      To see detailed results scroll down or use the mouse and move over the amino acids in the image.
    </p>

    <div align="center">
      <map name="tt_map">
	<?php $_from = $this->_tpl_vars['resultImagemap']; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array'); }if (count($_from)):
    foreach ($_from as $this->_tpl_vars['a']):
?>
	<area nohref="nohref" onmouseover="Tip('<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "helix_result_infobox.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>')" onmouseout="UnTip()" shape="rect" coords="<?php echo $this->_tpl_vars['a']['coords']; ?>
" />
	<?php endforeach; endif; unset($_from); ?>
      </map>
      <img src="<?php echo $this->_tpl_vars['imageFile']; ?>
" usemap="#tt_map" border="0" alt="Transmembran helices" />
    </div>

    <?php if (isset ( $this->_tpl_vars['resultImagemap2'] )): ?>
    <br/>
    <h4>helix from strucural data</h4>
    <div align="center">
      <map name="tt_map2">
	<?php $_from = $this->_tpl_vars['resultImagemap2']; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array'); }if (count($_from)):
    foreach ($_from as $this->_tpl_vars['a']):
?>
	<area nohref="nohref" onmouseover="Tip('<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "helix_result_infobox.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>')" onmouseout="UnTip()"  shape="rect" coords="<?php echo $this->_tpl_vars['a']['coords']; ?>
" />
	<?php endforeach; endif; unset($_from); ?>
      </map>
      <img src="<?php echo $this->_tpl_vars['imageFile2']; ?>
" usemap="#tt_map2" border="0" alt="Transmembran helices" />
    </div>
    <?php endif; ?>

    <?php if (isset ( $this->_tpl_vars['aResultImagemap'] )): ?>
    <?php $_from = $this->_tpl_vars['aResultImagemap']; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array'); }if (count($_from)):
    foreach ($_from as $this->_tpl_vars['c'] => $this->_tpl_vars['im']):
?>
    <br/>
    <h4>helix from strucural data, chain <?php echo $this->_tpl_vars['c']; ?>
</h4>
    <div align="center">
      <map name="tt_map-<?php echo $this->_tpl_vars['c']; ?>
">
	<?php $_from = $this->_tpl_vars['im']; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array'); }if (count($_from)):
    foreach ($_from as $this->_tpl_vars['a']):
?>
	<area nohref="nohref" onmouseover="Tip('<?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => "helix_result_infobox.tpl", 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>')" onmouseout="UnTip()"  shape="rect" coords="<?php echo $this->_tpl_vars['a']['coords']; ?>
" />
	<?php endforeach; endif; unset($_from); ?>
      </map>
      <img src="<?php echo $this->_tpl_vars['aImageFile'][$this->_tpl_vars['c']]; ?>
" usemap="#tt_map-<?php echo $this->_tpl_vars['c']; ?>
" border="0" alt="Transmembran helices" />
    </div>

    <?php endforeach; endif; unset($_from); ?>
    <?php endif; ?>


  </div>

  
  <h3  id="legendToggle" class="toggleNext">Legend</h3>
  <div>
    <ul>
      <li>
	Contact colorcodes:
	<span class="legendAaPred" style="color:#ff4500;">A</span> helix contact,&nbsp;
	<span class="legendAaPred" style="color:#002BB8;">A</span> membrane contact
	<!--,&nbsp;<span class="legendAaPred" style="color:#1e90ff;">A</span> water contact.-->
      </li>
      <?php if (isset ( $this->_tpl_vars['pfamDomains'] )): ?><li>Dots on the left mark conserved (Pfam) amino acid, bigger dots mean higher conservation. Different Pfam domains get a differently colored dot.</li><?php endif; ?>
      <?php if (isset ( $this->_tpl_vars['example'] )): ?><li>dots on the right =&gt; red: real helix contact, green: real membran contact</li><?php endif; ?>
    </ul>
  </div>

  <?php if (isset ( $this->_tpl_vars['pfamDomains'] )): ?>
  <h3 id="pfamToggle" class="toggleNext">Pfam Domains</h3>		
  <ul>
    <?php $_from = $this->_tpl_vars['pfamDomains']; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array'); }if (count($_from)):
    foreach ($_from as $this->_tpl_vars['name']):
?>
    <li><a href="http://pfam.sanger.ac.uk/family?entry=<?php echo $this->_tpl_vars['name']; ?>
" target="_blank"><?php echo $this->_tpl_vars['name']; ?>
</a></li>
    <?php endforeach; endif; unset($_from); ?>
  </ul>
  <?php endif; ?>

<!--
  <h3 id="paramsToggle" class="toggleNext">Used parameters/info</h3>		
  <div>
    <b>protein type:&nbsp;</b><?php echo $this->_tpl_vars['matType']; ?>
<br/>
    <b>located membran sections:&nbsp;</b><?php echo $this->_tpl_vars['countMembranSections']; ?>
<br/>
    <b>specificity:&nbsp;</b><?php echo $this->_tpl_vars['optLevel']; ?>
<br/>
  </div>
-->

  <h3 id="downloadsToggle" class="toggleNext">Downloads</h3>
  <dl>
    <dt><a href="<?php echo $this->_tpl_vars['resultFile']; ?>
" target="_blank">Results textfile</a></dt>
    <dd>Contains the given <i>sequence</i> and three strings aligned to it containing the predicted  contact, the conservation status and the membrane helix section definition (either given by you or predicted by HMMTOP).</dd>
    
    <?php if (isset ( $this->_tpl_vars['imageFileHighRes'] )): ?>
    <dt><a href="<?php echo $this->_tpl_vars['imageFileHighRes']; ?>
" target="_blank">High resolution image</a></dt>
    <dd>A high resolution version of the image above.</dd>
    <?php endif; ?>

    <dt><a href="<?php echo $this->_tpl_vars['pymolFile']; ?>
" target="_blank">PyMOL coloring script</a></dt>
    <dd>If you already have some 3d model viewable in <a href="http://pymol.sourceforge.net/">PyMOL</a>, then you can use this script to show the results from RHYTHM directly with your model. However you must take care that the indices of the sequence you uploaded to RHYTHM and those in your model map to the same residues. To use the script download it, load your model into PyMOL and issue the script via the <i>Run...</i> command.</dd>
  </dl>

  <ul>
    <?php if (isset ( $this->_tpl_vars['resultFile2'] )): ?>
    <li><a href="<?php echo $this->_tpl_vars['resultFile2']; ?>
" target="_blank">Download results (helix from strucural data)</a></li>
    <?php endif; ?>

    <?php if (isset ( $this->_tpl_vars['pymolFile2'] )): ?>
    <li><a href="<?php echo $this->_tpl_vars['pymolFile2']; ?>
" target="_blank">Pymol coloring script (helix from strucural data)</a></li>
    <?php endif; ?>

    <?php if (isset ( $this->_tpl_vars['pymolFile3'] )): ?>
    <li><a href="<?php echo $this->_tpl_vars['pymolFile3']; ?>
" target="_blank">Pymol coloring script (contacts from strucural data)</a></li>
    <?php endif; ?>


    <?php if (isset ( $this->_tpl_vars['pymolFileAllchains'] )): ?>
    <li><a href="<?php echo $this->_tpl_vars['pymolFile2']; ?>
" target="_blank">Pymol coloring script (helix from strucural data, all chains)</a></li>
    <?php endif; ?>

    <?php if (isset ( $this->_tpl_vars['pymolFileCurchains'] )): ?>
    <li><a href="<?php echo $this->_tpl_vars['pymolFileAllchains']; ?>
" target="_blank">Pymol coloring script (contacts from strucural data, all chains)</a></li>
    <?php endif; ?>

  </ul>		


  <h3 id="locToggle" class="toggleNext">Locations of helices:</h3>
  <div>
    <?php if ($this->_tpl_vars['helixHmmtop']): ?>This membrane helix sections were predicted using <a href="http://www.enzim.hu/hmmtop/" target="_blank">HMMTOP</a>. Please be aware it's limitations.<?php endif; ?>

    <div style="margin-left: 140px; font-size:140%;">
      <?php echo $this->_tpl_vars['helixLocations']; ?>

    </div>
  </div>
