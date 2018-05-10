{addslashesRemoveNl}
<div class='infobox'>
  <span><big>{$a.aaName}&nbsp;{$a.aaId}{if $a.contact}&nbsp;-&nbsp;<b>{$a.contact}</b>{/if}<big></span>
  {if defined('DEBUG')}
  <hr/>
  <table>
    <tr>
      <th colspan='3'>Scores</th>
    </tr>
    <tr>
      <td>Helix</td>
      <td class='data'>{$a.helixScore|string_format:"%.2f"}</td>
    </tr>
    <tr>
      <td>Membrane</td>
      <td class='data'>{$a.membraneScore|string_format:"%.2f"}</td>
    </tr>
    <tr>
      <td>Water</td>
      <td class='data'>{$a.waterScore|string_format:"%.2f"}</td>
    </tr>
  </table>
  {/if}
  {if $a.pfamDom}
  <hr/>
  <table>
    <tr>
      <th colspan='3'>Pfam&nbsp;domains</th>
    </tr>
    {foreach from=$a.pfamDom key=dom item=type}
    <tr>
      <td>{$dom}</td>
      <td class='data'>
	{if defined('DEBUG')}
	({$type})
	{else}
	{if $type=='+'}
	(similarly&nbsp;conserved)
	{elseif is_upper($type)}
	(fully&nbsp;conserved)
	{elseif is_lower($type)}
	(highly&nbsp;conserved)
	{else}
	(conservation&nbsp;status&nbsp;unknown)
	{/if}
	{/if}
      </td>
    </tr>
    {/foreach}
  </table>
  {/if}
  {if $a.curated}
  <hr/>
  <table>
    <tr>
      <th colspan='3'>Curated data info</th>
    </tr>
    {foreach from=$a.curated key=k item=i}
    <tr>
      <td>{$k}</td>
      <td class='data'>
	{$i}
      </td>
    </tr>
    {/foreach}
  </table>
  {/if}
</div>
{/addslashesRemoveNl}
