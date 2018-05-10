<?php /* Smarty version 2.6.20, created on 2018-05-02 07:55:04
         compiled from methods_learning_matrix.tpl */ ?>
<?php require_once(SMARTY_CORE_DIR . 'core.load_plugins.php');
smarty_core_load_plugins(array('plugins' => array(array('modifier', 'getScoreClass', 'methods_learning_matrix.tpl', 20, false),array('modifier', 'string_format', 'methods_learning_matrix.tpl', 20, false),)), $this); ?>

<h4>Propensity matrix: <?php echo $this->_tpl_vars['a']['name']; ?>
</h4>

<table class="propMatrix">

  <tr>
    <th></th>
    <?php $_from = $this->_tpl_vars['a']['colNames']; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array'); }if (count($_from)):
    foreach ($_from as $this->_tpl_vars['colName']):
?>
    <th><?php echo $this->_tpl_vars['colName']; ?>
</th>
    <?php endforeach; endif; unset($_from); ?>
    <th></th>
  </tr>
  
  <?php $_from = $this->_tpl_vars['a']['propMatrix']; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array'); }$this->_foreach['row'] = array('total' => count($_from), 'iteration' => 0);
if ($this->_foreach['row']['total'] > 0):
    foreach ($_from as $this->_tpl_vars['rowName'] => $this->_tpl_vars['row']):
        $this->_foreach['row']['iteration']++;
?>
  <tr>
    <th><?php echo $this->_tpl_vars['rowName']; ?>
</th>
    <?php $_from = $this->_tpl_vars['row']; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array'); }$this->_foreach['col'] = array('total' => count($_from), 'iteration' => 0);
if ($this->_foreach['col']['total'] > 0):
    foreach ($_from as $this->_tpl_vars['data']):
        $this->_foreach['col']['iteration']++;
?>
    <?php if (in_array ( ($this->_foreach['col']['iteration']-1) , $this->_tpl_vars['a']['mark'] )): ?>
    <?php if (($this->_foreach['row']['iteration'] <= 1)): ?>
    <td class="<?php echo ((is_array($_tmp=$this->_tpl_vars['data'])) ? $this->_run_mod_handler('getScoreClass', true, $_tmp) : $this->_plugins['modifier']['getScoreClass'][0][0]->getScoreClass($_tmp)); ?>
 mark markTop"><?php echo ((is_array($_tmp=$this->_tpl_vars['data'])) ? $this->_run_mod_handler('string_format', true, $_tmp, "%.2f") : smarty_modifier_string_format($_tmp, "%.2f")); ?>
</td>
    <?php elseif (($this->_foreach['row']['iteration'] == $this->_foreach['row']['total'])): ?>
    <td class="<?php echo ((is_array($_tmp=$this->_tpl_vars['data'])) ? $this->_run_mod_handler('getScoreClass', true, $_tmp) : $this->_plugins['modifier']['getScoreClass'][0][0]->getScoreClass($_tmp)); ?>
 mark markBottom"><?php echo ((is_array($_tmp=$this->_tpl_vars['data'])) ? $this->_run_mod_handler('string_format', true, $_tmp, "%.2f") : smarty_modifier_string_format($_tmp, "%.2f")); ?>
</td>
    <?php else: ?>
    <td class="<?php echo ((is_array($_tmp=$this->_tpl_vars['data'])) ? $this->_run_mod_handler('getScoreClass', true, $_tmp) : $this->_plugins['modifier']['getScoreClass'][0][0]->getScoreClass($_tmp)); ?>
 mark"><?php echo ((is_array($_tmp=$this->_tpl_vars['data'])) ? $this->_run_mod_handler('string_format', true, $_tmp, "%.2f") : smarty_modifier_string_format($_tmp, "%.2f")); ?>
</td>
    <?php endif; ?>
    <?php else: ?>
    <td class="<?php echo ((is_array($_tmp=$this->_tpl_vars['data'])) ? $this->_run_mod_handler('getScoreClass', true, $_tmp) : $this->_plugins['modifier']['getScoreClass'][0][0]->getScoreClass($_tmp)); ?>
"><?php echo ((is_array($_tmp=$this->_tpl_vars['data'])) ? $this->_run_mod_handler('string_format', true, $_tmp, "%.2f") : smarty_modifier_string_format($_tmp, "%.2f")); ?>
</td>
    <?php endif; ?>
    <?php endforeach; endif; unset($_from); ?>
    <th><?php echo $this->_tpl_vars['rowName']; ?>
</th>
  </tr>
  <?php endforeach; endif; unset($_from); ?>
  
  <tr>
    <th></th>
    <?php $_from = $this->_tpl_vars['a']['colNames']; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array'); }if (count($_from)):
    foreach ($_from as $this->_tpl_vars['colName']):
?>
    <th><?php echo $this->_tpl_vars['colName']; ?>
</th>
    <?php endforeach; endif; unset($_from); ?>
    <th></th>
  </tr>

</table>