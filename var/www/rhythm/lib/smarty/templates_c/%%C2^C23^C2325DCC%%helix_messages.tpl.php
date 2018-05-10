<?php /* Smarty version 2.6.20, created on 2018-05-07 09:00:07
         compiled from helix_messages.tpl */ ?>

<?php if (isset ( $this->_tpl_vars['warnings'] ) || isset ( $this->_tpl_vars['notes'] )): ?>
<div class="messages">
    
    <?php if (isset ( $this->_tpl_vars['warnings'] )): ?>
    <div class="warnings">
      <ul>
        <?php $_from = $this->_tpl_vars['warnings']; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array'); }if (count($_from)):
    foreach ($_from as $this->_tpl_vars['w']):
?>
        <li><?php echo $this->_tpl_vars['w']; ?>
</li>
        <?php endforeach; endif; unset($_from); ?>
      </ul>
    </div>
    <?php endif; ?>
    
    <?php if (isset ( $this->_tpl_vars['notes'] )): ?>
    <div class="notes">
      <ul>
        <?php $_from = $this->_tpl_vars['notes']; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array'); }if (count($_from)):
    foreach ($_from as $this->_tpl_vars['n']):
?>
        <li><?php echo $this->_tpl_vars['n']; ?>
</li>
        <?php endforeach; endif; unset($_from); ?>
      </ul>
    </div>
    <?php endif; ?>

</div>
<?php endif; ?>