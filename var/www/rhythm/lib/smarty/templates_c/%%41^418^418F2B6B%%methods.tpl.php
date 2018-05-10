<?php /* Smarty version 2.6.20, created on 2018-05-07 09:00:16
         compiled from methods.tpl */ ?>
<h1>Methods</h1>

<div class="submenu">
    <a target="_self" <?php if ($this->_tpl_vars['subsite'] == 'general'): ?>class="active"<?php endif; ?> href="./index.php?site=methods&sub=general">Overview/Workflow</a>
    <a target="_self" <?php if ($this->_tpl_vars['subsite'] == 'learning'): ?>class="active"<?php endif; ?> href="./index.php?site=methods&sub=learning">Matrix prediction</a> 
    <a target="_self" <?php if ($this->_tpl_vars['subsite'] == 'databases'): ?>class="active"<?php endif; ?> href="./index.php?site=methods&sub=databases">Pfam domains</a>
    <a target="_self" <?php if ($this->_tpl_vars['subsite'] == 'prediction'): ?>class="active"<?php endif; ?> href="./index.php?site=methods&sub=prediction">Prediction</a>
</div>

<div class="subcontent">
  <?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => $this->_tpl_vars['subpageTplFile'], 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>
</div>