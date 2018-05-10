
{if isset($warnings) || isset($notes)}
<div class="messages">
    
    {if isset($warnings)}
    <div class="warnings">
      <ul>
        {foreach from=$warnings item=w}
        <li>{$w}</li>
        {/foreach}
      </ul>
    </div>
    {/if}
    
    {if isset($notes)}
    <div class="notes">
      <ul>
        {foreach from=$notes item=n}
        <li>{$n}</li>
        {/foreach}
      </ul>
    </div>
    {/if}

</div>
{/if}