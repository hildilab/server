

<!--
<h3 id="helpToggle" class="toggleNext">Help</h3>
<div>
  <ul>
    <li>I can put some help here...</li>
  </ul>
</div>
-->

{if isset($waitTplFile)}
<h3>
  Update
  <span class="help">The searching for Pfam domains is done in the background,<br/>while you can already see first results.<span class="hline"></span>If this says 'still searching...' for several minutes you may try to click the update-button below.</span>
</h3>	
<p><a id="hmmerStatusLink" href="index.php?{$params}">click to see if there were conserved amino acids via pfam domains found?</a></p>
{/if}


{if isset($update)}
<h3 id="adjustToggle" class="toggleNext">Adjust</h3>
<div class="formSettings" align="center">
  <form enctype="multipart/form-data" action="index.php?{$updateParams}" method="POST">
    {include file=helix_form_settings.tpl}
  </form>
</div>
{/if}

  <h3>Results</h3>	
  <div>
    {if isset($example)}
    <p>Example: {$example}, <a href="examples/{$example}.pdb">PDB</a></p>
    {/if}

    <p>
      To see detailed results scroll down or use the mouse and move over the amino acids in the image.
    </p>

    <div align="center">
      <map name="tt_map">
	{foreach from=$resultImagemap item=a}
	<area nohref="nohref" onmouseover="Tip('{include file=helix_result_infobox.tpl}')" onmouseout="UnTip()" shape="rect" coords="{$a.coords}" />
	{/foreach}
      </map>
      <img src="{$imageFile}" usemap="#tt_map" border="0" alt="Transmembran helices" />
    </div>

    {if isset($resultImagemap2)}
    <br/>
    <h4>helix from strucural data</h4>
    <div align="center">
      <map name="tt_map2">
	{foreach from=$resultImagemap2 item=a}
	<area nohref="nohref" onmouseover="Tip('{include file=helix_result_infobox.tpl}')" onmouseout="UnTip()"  shape="rect" coords="{$a.coords}" />
	{/foreach}
      </map>
      <img src="{$imageFile2}" usemap="#tt_map2" border="0" alt="Transmembran helices" />
    </div>
    {/if}

    {if isset($aResultImagemap)}
    {foreach from=$aResultImagemap key=c item=im}
    <br/>
    <h4>helix from strucural data, chain {$c}</h4>
    <div align="center">
      <map name="tt_map-{$c}">
	{foreach from=$im item=a}
	<area nohref="nohref" onmouseover="Tip('{include file=helix_result_infobox.tpl}')" onmouseout="UnTip()"  shape="rect" coords="{$a.coords}" />
	{/foreach}
      </map>
      <img src="{$aImageFile[$c]}" usemap="#tt_map-{$c}" border="0" alt="Transmembran helices" />
    </div>

    {/foreach}
    {/if}


  </div>

  
  <h3  id="legendToggle" class="toggleNext">Legend</h3>
  <div>
    <ul>
      <li>
	Contact colorcodes:
	<span class="legendAaPred" style="color:#ff4500;">A</span> helix contact,&nbsp;
	<span class="legendAaPred" style="color:#002BB8;">A</span> membrane contact
	<!--,&nbsp;<span class="legendAaPred" style="color:#1e90ff;">A</span> water contact.-->
      </li>
      {if isset($pfamDomains)}<li>Dots on the left mark conserved (Pfam) amino acid, bigger dots mean higher conservation. Different Pfam domains get a differently colored dot.</li>{/if}
      {if isset($example)}<li>dots on the right =&gt; red: real helix contact, green: real membran contact</li>{/if}
    </ul>
  </div>

  {if isset($pfamDomains)}
  <h3 id="pfamToggle" class="toggleNext">Pfam Domains</h3>		
  <ul>
    {foreach from=$pfamDomains item=name}
    <li><a href="http://pfam.sanger.ac.uk/family?entry={$name}" target="_blank">{$name}</a></li>
    {/foreach}
  </ul>
  {/if}

<!--
  <h3 id="paramsToggle" class="toggleNext">Used parameters/info</h3>		
  <div>
    <b>protein type:&nbsp;</b>{$matType}<br/>
    <b>located membran sections:&nbsp;</b>{$countMembranSections}<br/>
    <b>specificity:&nbsp;</b>{$optLevel}<br/>
  </div>
-->

  <h3 id="downloadsToggle" class="toggleNext">Downloads</h3>
  <dl>
    <dt><a href="{$resultFile}" target="_blank">Results textfile</a></dt>
    <dd>Contains the given <i>sequence</i> and three strings aligned to it containing the predicted  contact, the conservation status and the membrane helix section definition (either given by you or predicted by HMMTOP).</dd>
    
    {if isset($imageFileHighRes)}
    <dt><a href="{$imageFileHighRes}" target="_blank">High resolution image</a></dt>
    <dd>A high resolution version of the image above.</dd>
    {/if}

    <dt><a href="{$pymolFile}" target="_blank">PyMOL coloring script</a></dt>
    <dd>If you already have some 3d model viewable in <a href="http://pymol.sourceforge.net/">PyMOL</a>, then you can use this script to show the results from RHYTHM directly with your model. However you must take care that the indices of the sequence you uploaded to RHYTHM and those in your model map to the same residues. To use the script download it, load your model into PyMOL and issue the script via the <i>Run...</i> command.</dd>
  </dl>

  <ul>
    {if isset($resultFile2)}
    <li><a href="{$resultFile2}" target="_blank">Download results (helix from strucural data)</a></li>
    {/if}

    {if isset($pymolFile2)}
    <li><a href="{$pymolFile2}" target="_blank">Pymol coloring script (helix from strucural data)</a></li>
    {/if}

    {if isset($pymolFile3)}
    <li><a href="{$pymolFile3}" target="_blank">Pymol coloring script (contacts from strucural data)</a></li>
    {/if}


    {if isset($pymolFileAllchains)}
    <li><a href="{$pymolFile2}" target="_blank">Pymol coloring script (helix from strucural data, all chains)</a></li>
    {/if}

    {if isset($pymolFileCurchains)}
    <li><a href="{$pymolFileAllchains}" target="_blank">Pymol coloring script (contacts from strucural data, all chains)</a></li>
    {/if}

  </ul>		


  <h3 id="locToggle" class="toggleNext">Locations of helices:</h3>
  <div>
    {if $helixHmmtop}This membrane helix sections were predicted using <a href="http://www.enzim.hu/hmmtop/" target="_blank">HMMTOP</a>. Please be aware it's limitations.{/if}

    <div style="margin-left: 140px; font-size:140%;">
      {$helixLocations}
    </div>
  </div>

