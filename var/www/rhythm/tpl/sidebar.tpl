<div class="leftcol">

  {include file='header.tpl'}

  <div class="navi">
    <a target="_self" {if $site == 'home'}class="active"{/if} href="./index.php?site=home">Home</a>
    <a target="_self" {if $site == 'helix'}class="active"{/if} href="./index.php?site=helix">Prediction calculate</a>
    <a target="_self" href="./index.php?site=methods">Methods</a>
    <div style="margin-left: 24px;">
      <a target="_self" {if $subsite == 'general'}class="active"{/if} href="./index.php?site=methods&sub=general">Overview/Workflow</a>
      <a target="_self" {if $subsite == 'learning'}class="active"{/if} href="./index.php?site=methods&sub=learning">Matrix prediction</a> 
      <a target="_self" {if $subsite == 'databases'}class="active"{/if} href="./index.php?site=methods&sub=databases">Pfam domains</a>
      <a target="_self" {if $subsite == 'prediction'}class="active"{/if} href="./index.php?site=methods&sub=prediction">Prediction</a>
    </div>
    <a target="_self" {if $site == 'references'}class="active"{/if} href="./index.php?site=references">References</a>
    <a target="_self" {if $site == 'FAQ'}class="active"{/if} href="./index.php?site=FAQ">FAQ</a>
  </div>

  <div style="margin-top: 24px;">&nbsp;</div>

  <div class="navi">
    <a target="_self" {if $site == 'links'}class="active"{/if} href="./index.php?site=links">Links/related Projects</a>
  </div>

</div>
