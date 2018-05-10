

<h3 id="helpToggle" class="toggleNext">Help</h3>
<div class="formSettings">
  <ul>
    <li>There is a context sensitive help available. Move your mouse pointer over the <span class="help">some help...</span> icons to see it.</li>
    <li>Some parts of a page can be hidden. E.g. click on the <img style="background: #333377; padding: 2px; vertical-align: middle;" src="./img/opened.png"> icon in the heading above to hide this help and then on the appeared <img style="background: #333377; padding: 2px; vertical-align: middle;" src="./img/closed.png"> icon to show it again.</li>
    <li>Quick how to: You need to give some <b>sequence input</b> either directly as sequence or by uploading a file in fasta format. All options under <b>settings</b> are all explained via context sensitive help. They also can be adjusted directly when viewing the results.</li>
  </ul>
</div>


<div align="center">

  <form enctype="multipart/form-data" action="index.php?site=helix" method="POST">
    <fieldset>
      <legend>
	sequence input
      </legend> 
      <table>
	<tr>
	  <td>	
	    Enter a sequence:
	    <span class="help">NOT in fasta format, just a plain string.<br/>Will be filtered for non amino acid characters.</span>
	    <br/>
	    <input type="button" onclick="$('seq').value=exampleSeqChannel; $('mat').value='channel';" value="Example (channel)" />
	    <br/>
	    <input type="button" onclick="$('seq').value=exampleSeqCoil; $('mat').value='coil';" value="Ex. (membrane-coil)" />
	  </td>
	  <td>
	    <textarea name="seq" id="seq" cols="40" rows="5"></textarea>
	  </td>
	  <td>
	    &nbsp;or
	  </td>
	</tr>
	<tr>
	  <td>
	    Upload Fasta File:
	    <span class="help">Only the first sequence will be used</span>
	  </td>
	  <td>
	    <input name="userfile" type="file" size="25" />
	  </td>
	  <td>
	    {if isset($examples)}&nbsp;or{/if}
	  </td>
	</tr>
	
	{if isset($examples)}
	<tr>
	  <td>
	    <label for="example">
	      Select an example:
	    </label>
	  </td>
	  <td>
	    <select name="example" id="example" size="1">
	      <option value=""></option>
	      {foreach from=$examples item=ex}
	      <option value="{$ex}">{$ex}</option>
	      {/foreach}
	    </select>
	  </td>
	  <td>
	  </td>
	</tr>
	{/if}
      </table>
    </fieldset>

    <fieldset>
      <legend>
	settings
	<span class="help">you will be able to adjust these values after submitting while viewing results</span>
      </legend> 
      {include file=helix_form_settings.tpl}
    </fieldset>

  </form>
</div>
