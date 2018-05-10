<h1>Methods</h1>

<div class="submenu">
    <a target="_self" {if $subsite == 'general'}class="active"{/if} href="./index.php?site=methods&sub=general">Overview/Workflow</a>
    <a target="_self" {if $subsite == 'learning'}class="active"{/if} href="./index.php?site=methods&sub=learning">Matrix prediction</a> 
    <a target="_self" {if $subsite == 'databases'}class="active"{/if} href="./index.php?site=methods&sub=databases">Pfam domains</a>
    <a target="_self" {if $subsite == 'prediction'}class="active"{/if} href="./index.php?site=methods&sub=prediction">Prediction</a>
</div>

<div class="subcontent">
  {include file=$subpageTplFile}
</div>
