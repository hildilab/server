<?php /* Smarty version 2.6.20, created on 2018-03-28 16:37:45
         compiled from helix_result_infobox.tpl */ ?>
<?php require_once(SMARTY_CORE_DIR . 'core.load_plugins.php');
smarty_core_load_plugins(array('plugins' => array(array('block', 'addslashesRemoveNl', 'helix_result_infobox.tpl', 1, false),array('modifier', 'string_format', 'helix_result_infobox.tpl', 12, false),)), $this); ?>
<?php $this->_tag_stack[] = array('addslashesRemoveNl', array()); $_block_repeat=true;$this->_plugins['block']['addslashesRemoveNl'][0][0]->addslashesRemoveNl($this->_tag_stack[count($this->_tag_stack)-1][1], null, $this, $_block_repeat);while ($_block_repeat) { ob_start(); ?>
<div class='infobox'>
  <span><big><?php echo $this->_tpl_vars['a']['aaName']; ?>
&nbsp;<?php echo $this->_tpl_vars['a']['aaId']; ?>
<?php if ($this->_tpl_vars['a']['contact']): ?>&nbsp;-&nbsp;<b><?php echo $this->_tpl_vars['a']['contact']; ?>
</b><?php endif; ?><big></span>
  <?php if (defined ( 'DEBUG' )): ?>
  <hr/>
  <table>
    <tr>
      <th colspan='3'>Scores</th>
    </tr>
    <tr>
      <td>Helix</td>
      <td class='data'><?php echo ((is_array($_tmp=$this->_tpl_vars['a']['helixScore'])) ? $this->_run_mod_handler('string_format', true, $_tmp, "%.2f") : smarty_modifier_string_format($_tmp, "%.2f")); ?>
</td>
    </tr>
    <tr>
      <td>Membrane</td>
      <td class='data'><?php echo ((is_array($_tmp=$this->_tpl_vars['a']['membraneScore'])) ? $this->_run_mod_handler('string_format', true, $_tmp, "%.2f") : smarty_modifier_string_format($_tmp, "%.2f")); ?>
</td>
    </tr>
    <tr>
      <td>Water</td>
      <td class='data'><?php echo ((is_array($_tmp=$this->_tpl_vars['a']['waterScore'])) ? $this->_run_mod_handler('string_format', true, $_tmp, "%.2f") : smarty_modifier_string_format($_tmp, "%.2f")); ?>
</td>
    </tr>
  </table>
  <?php endif; ?>
  <?php if ($this->_tpl_vars['a']['pfamDom']): ?>
  <hr/>
  <table>
    <tr>
      <th colspan='3'>Pfam&nbsp;domains</th>
    </tr>
    <?php $_from = $this->_tpl_vars['a']['pfamDom']; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array'); }if (count($_from)):
    foreach ($_from as $this->_tpl_vars['dom'] => $this->_tpl_vars['type']):
?>
    <tr>
      <td><?php echo $this->_tpl_vars['dom']; ?>
</td>
      <td class='data'>
	<?php if (defined ( 'DEBUG' )): ?>
	(<?php echo $this->_tpl_vars['type']; ?>
)
	<?php else: ?>
	<?php if ($this->_tpl_vars['type'] == '+'): ?>
	(similarly&nbsp;conserved)
	<?php elseif (is_upper ( $this->_tpl_vars['type'] )): ?>
	(fully&nbsp;conserved)
	<?php elseif (is_lower ( $this->_tpl_vars['type'] )): ?>
	(highly&nbsp;conserved)
	<?php else: ?>
	(conservation&nbsp;status&nbsp;unknown)
	<?php endif; ?>
	<?php endif; ?>
      </td>
    </tr>
    <?php endforeach; endif; unset($_from); ?>
  </table>
  <?php endif; ?>
  <?php if ($this->_tpl_vars['a']['curated']): ?>
  <hr/>
  <table>
    <tr>
      <th colspan='3'>Curated data info</th>
    </tr>
    <?php $_from = $this->_tpl_vars['a']['curated']; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array'); }if (count($_from)):
    foreach ($_from as $this->_tpl_vars['k'] => $this->_tpl_vars['i']):
?>
    <tr>
      <td><?php echo $this->_tpl_vars['k']; ?>
</td>
      <td class='data'>
	<?php echo $this->_tpl_vars['i']; ?>

      </td>
    </tr>
    <?php endforeach; endif; unset($_from); ?>
  </table>
  <?php endif; ?>
</div>
<?php $_block_content = ob_get_contents(); ob_end_clean(); $_block_repeat=false;echo $this->_plugins['block']['addslashesRemoveNl'][0][0]->addslashesRemoveNl($this->_tag_stack[count($this->_tag_stack)-1][1], $_block_content, $this, $_block_repeat); }  array_pop($this->_tag_stack); ?>