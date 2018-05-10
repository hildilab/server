<?php /* Smarty version 2.6.20, created on 2018-05-07 09:00:16
         compiled from sidebar.tpl */ ?>
<div class="leftcol">

  <?php $_smarty_tpl_vars = $this->_tpl_vars;
$this->_smarty_include(array('smarty_include_tpl_file' => 'header.tpl', 'smarty_include_vars' => array()));
$this->_tpl_vars = $_smarty_tpl_vars;
unset($_smarty_tpl_vars);
 ?>

  <div class="navi">
    <a target="_self" <?php if ($this->_tpl_vars['site'] == 'home'): ?>class="active"<?php endif; ?> href="./index.php?site=home">Home</a>
    <a target="_self" <?php if ($this->_tpl_vars['site'] == 'helix'): ?>class="active"<?php endif; ?> href="./index.php?site=helix">Prediction calculate</a>
    <a target="_self" href="./index.php?site=methods">Methods</a>
    <div style="margin-left: 24px;">
      <a target="_self" <?php if ($this->_tpl_vars['subsite'] == 'general'): ?>class="active"<?php endif; ?> href="./index.php?site=methods&sub=general">Overview/Workflow</a>
      <a target="_self" <?php if ($this->_tpl_vars['subsite'] == 'learning'): ?>class="active"<?php endif; ?> href="./index.php?site=methods&sub=learning">Matrix prediction</a> 
      <a target="_self" <?php if ($this->_tpl_vars['subsite'] == 'databases'): ?>class="active"<?php endif; ?> href="./index.php?site=methods&sub=databases">Pfam domains</a>
      <a target="_self" <?php if ($this->_tpl_vars['subsite'] == 'prediction'): ?>class="active"<?php endif; ?> href="./index.php?site=methods&sub=prediction">Prediction</a>
    </div>
    <a target="_self" <?php if ($this->_tpl_vars['site'] == 'references'): ?>class="active"<?php endif; ?> href="./index.php?site=references">References</a>
    <a target="_self" <?php if ($this->_tpl_vars['site'] == 'FAQ'): ?>class="active"<?php endif; ?> href="./index.php?site=FAQ">FAQ</a>
  </div>

  <div style="margin-top: 24px;">&nbsp;</div>

  <div class="navi">
    <a target="_self" <?php if ($this->_tpl_vars['site'] == 'links'): ?>class="active"<?php endif; ?> href="./index.php?site=links">Links/related Projects</a>
  </div>

</div>