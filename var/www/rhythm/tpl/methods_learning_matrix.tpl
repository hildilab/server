
<h4>Propensity matrix: {$a.name}</h4>

<table class="propMatrix">

  <tr>
    <th></th>
    {foreach from=$a.colNames item=colName}
    <th>{$colName}</th>
    {/foreach}
    <th></th>
  </tr>
  
  {foreach from=$a.propMatrix key=rowName item=row name=row}
  <tr>
    <th>{$rowName}</th>
    {foreach from=$row item=data name=col}
    {if in_array($smarty.foreach.col.index,$a.mark)}
    {if $smarty.foreach.row.first}
    <td class="{$data|getScoreClass} mark markTop">{$data|string_format:"%.2f"}</td>
    {elseif $smarty.foreach.row.last}
    <td class="{$data|getScoreClass} mark markBottom">{$data|string_format:"%.2f"}</td>
    {else}
    <td class="{$data|getScoreClass} mark">{$data|string_format:"%.2f"}</td>
    {/if}
    {else}
    <td class="{$data|getScoreClass}">{$data|string_format:"%.2f"}</td>
    {/if}
    {/foreach}
    <th>{$rowName}</th>
  </tr>
  {/foreach}
  
  <tr>
    <th></th>
    {foreach from=$a.colNames item=colName}
    <th>{$colName}</th>
    {/foreach}
    <th></th>
  </tr>

</table>
