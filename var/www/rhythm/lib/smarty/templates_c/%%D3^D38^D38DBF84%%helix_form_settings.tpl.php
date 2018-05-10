<?php /* Smarty version 2.6.20, created on 2018-05-07 09:00:07
         compiled from helix_form_settings.tpl */ ?>
<?php require_once(SMARTY_CORE_DIR . 'core.load_plugins.php');
smarty_core_load_plugins(array('plugins' => array(array('function', 'html_options', 'helix_form_settings.tpl', 11, false),)), $this); ?>
<table>
  <tr>
    <td>
      <label for="mat">
	Protein type:
	<span class="help">Specify channel or membrane-coil to get optimal results<br/>as explained in <b>Methods&nbsp;&gt;&nbsp;Matrix Prediction</b></span>
      </label>
    </td>
    <td>
      <select name="mat" id="mat" size="1">
	<?php echo smarty_function_html_options(array('values' => $this->_tpl_vars['vars']['mat']['values'],'output' => $this->_tpl_vars['vars']['mat']['names'],'selected' => $this->_tpl_vars['mat']), $this);?>

      </select>
    </td>
  </tr>
  <tr>
    <td>
      <label for="optLevel">
	Specificity:
	<span class="help">Specificity contra&nbsp;sensitivity. This is also related to precision<br/>as&nbsp;explained in <b>Methods&nbsp;&gt;&nbsp;Prediction</b></span>
      </label>
    </td>
    <td>
      <select name="optLevel" id="optLevel" size="1">
	<?php echo smarty_function_html_options(array('values' => $this->_tpl_vars['vars']['optLevel']['values'],'output' => $this->_tpl_vars['vars']['optLevel']['names'],'selected' => $this->_tpl_vars['optLevel']), $this);?>

      </select>
    </td>
  </tr>
  <tr>
    <td>
      <label for="useCons">
	Conservation:
	<span class="help">Use conservation information as explained<br/>in <b>Methods&nbsp;&gt;&nbsp;Pfam&nbsp;domains</b></span>
      </label>
    </td>
    <td>
      <input type="checkbox" name="useCons" id="cons" <?php if ($this->_tpl_vars['useCons'] == 1): ?> checked="checked"<?php endif; ?> value="1">
    </td>
  </tr>
  <tr>
    <td>
      <label for="helix">
	Helix positions:
	<span class="help"><b>The membrane helices will be automatically predicted by<br/>HMMTOP</b>, if you leave this empty.<span class="hline"></span>Define your own membrane helix position with this format:<br/><i>helix1begin-helix1end,helix2begin-helix2end</i>.<br/>The helices must be in ascending order and non-overlapping.<span class="hline"></span>Example: '12-24,30-41' defines two helices<br/>one spanning from 12 to 24 and the other from 30 to 41.<span class="hline"></span>Additionally you can define the orientation of the helix as spanning from <b>IN</b> to <b>OUT</b><br/> or the other way around. To do this write helix1orientation:helix1begin-helix1end,<br/>where helix1orientation is either 'i' or 'o'. If you do not define the orientation of<br/>some helix an alternation between 'i' and 'o' is assumed for those.</span><br/>(optional)
      </label>
    </td>
    <td>
      <input type="text" id="helix" name="helix" value="<?php echo $this->_tpl_vars['helix']; ?>
" size="60" />
    </td>
  </tr>
  <?php if (isset ( $this->_tpl_vars['hmmtopHelix'] )): ?>
  <tr>
    <td></td>
    <td>
      <?php echo $this->_tpl_vars['hmmtopHelix']; ?>

    </td>
  </tr>
  <?php endif; ?> 
  <tr>
    <td>
      <label for="chainName">
	Chain name:
	<span class="help">If you want to use the PyMOL coloring script you can define to which chain it should apply.<br/>The maximal length is two.</span><br/>(optional)
      </label>
    </td>
    <td>
      <input type="text" id="chainName" name="chainName" value="<?php echo $this->_tpl_vars['chainName']; ?>
" size="2" />
    </td>
  </tr>
  <tr>
    <td colspan="2" align="center" style="text-align: center;">
      <?php if (isset ( $this->_tpl_vars['update'] )): ?>	
      <input type="submit" id="doUpdate" name="doUpdate" value="Update" onclick="value='Update in progress'; addClassName('clicked');" />
      <?php else: ?> 
      <input type="submit" name="doPrediction" value="Predict" onclick="value='Prediction in progress'; addClassName('clicked');" />
      <?php endif; ?> 

    </td>
  </tr>
</table>