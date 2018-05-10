<%inherit file="base.mako" />
<script language="javascript">
$(document).ready(function(){
    $("table6").hide()
    $("a#slideFade6").toggle(function(){
	$("table6").animate({ height: 'show', opacity: 'show' }, 'fast');
    },function(){
	$("table6").animate({ height: 'hide', opacity: 'hide' }, 'fast');
    });
    $("table1").hide()
    $("a#slideFade1").toggle(function(){
	$("table1").animate({ height: 'show', opacity: 'show' }, 'fast');
    },function(){
	$("table1").animate({ height: 'hide', opacity: 'hide' }, 'fast');
    });
});

</script>

<script language="javascript">
    $(document).ready(function() {
        $(".clear_btn").click( function(e){
            clear_form_elements( $(this).parent() );
        });
    });
    function clear_form_elements( $ele ) {
        $ele.find(':input').each(function() {
            switch(this.type) {
                case 'file':
                case 'text':
                case 'textarea':
                    $(this).val('');
                    break;
                case 'checkbox':
                case 'radio':
                    this.checked = false;
            }
        });
    }
</script>

<div id="content" class="content">
<!--            <script type="text/javascript">
                document.write("<div class='toggleNice' style='display:none;'>");
            </script> -->
    <h1>Voronoia for RNA: Search & Calculation</h1>
    <div class="subcontent">
        <div>
            <form action="tools/v4rna/generator/form" method="post" enctype="multipart/form-data">
                <br>
                <fieldset id="example_2">
                    <legend>Get packing density from precalculated molecule file:</legend>
                    <p style="text-indent:1.0em;">Enter PDB-Entry or search words from the PDB-Header <img src="static/img/helpbubble.png" alt="logo" title="e.g.: riboswitch, 3UCU ..."></img>
                        <input name="data_idpdb" type="text" size="45" maxlength="100" />
                        <form:error name="data_idpdb" />
                    </p>
<!--		    <input type="checkbox" id="zipped" name="zipped" value="zipped" ><label for="zipped">Download all results zipped (many results occure long time to zip).</label>
-->		
		    
                    <p><input type="submit" name="submit" value="submit" />

		    <a href="#" id="slideFade1">show/hide whole dataset</a><br>
		    <table1 border="0">
		    <a>
			% for element in dataset_list:
			    <a name="pdbfile" href="${h.url_for('tools/v4rna/generator/form', data_idpdb=element, data_pdb='', submit='submit')}">
				<%
				    context.write(element)
				%>
			    </a>
			% endfor
		    </a>
		    </table1>

                    </p>
		    
                </fieldset>
                <p>
                % if (liste):
		    Result (# 
		    <%
			context.write(anzahl)
                    %>
			):
		    <br>
<!--
		    % if (zipped):
			All results zipped for download: <a name="zipped"  style='padding-left: 15px' href="${h.url_for('tools/v4rna/generator/download', filename='zipped', task_id=1)}">results</a>
		    <br>
		    % endif
-->
                    <%
                        i=0
                        g=len(liste)
                    %>
                    <table border="0">
                        % if (headerlist[i]!=""):
                            <thead>
                                <td><b>Vol-File<img src="static/img/helpbubble.png" alt="logo" title="extends the original PDB-file by 
van der Waals volume, solvent excluded volume and indicates whether the atom is buried or exposed (for more information consult the FAQ)"></img></b></td>
                                <td><b>Header</b></td>
				<td><b>z-Score-RMS<img src="static/img/helpbubble.png" alt="logo" title="indicates how the packing density 
relates to reference values (for more information consult the FAQ)"></img></b></td>
                                <td><b>PDB-File<img src="static/img/helpbubble.png" alt="logo" title="a pre-filtered PDB-file (for more 
information consult the FAQ)"></img></b></td>
				<td><b>extended Vol-File<img src="static/img/helpbubble.png" alt="logo" title="Vol-file extended by packing 
density values and z-Score (for more information consult the FAQ)"></img></b></td>
				<td><b>Visualisation</b></td>
				<td><b>zipped Files<img src="static/img/helpbubble.png" alt="logo" title="contains Vol-, PDB- and extended Vol-File"></img></b></td>
                            </thead>
                        % endif
                        <tbody>
                    % while i!=g:
                        <tr>
                            <td>
                                
				<a name="pdbfile" href="${'staticpdb/'+liste[i]+'.pdb/'+liste[i]+'.pdb.vol'}">
				    <%
					context.write(liste[i])
				    %>
				</a>
                            </td>
			    <td>
                                <%
                                    context.write(headerlist[i])
                                %>
                            </td>
			    <td>
                                <%
                                    context.write(zscorelist[i])
                                %>
                            </td>
			    <td>
                                <%
                                    j=liste[i]
                                %>
                                % if (headerlist[i]!=""):
                                        <a name="pdbfile" href="${'staticpdb/'+liste[i]+'.pdb/'+liste[i]+'.pdb'}">pdb-file </a>
                                % endif
                            </td>
			    <td>
                                
				<a name="pdbfile" href="${'staticpdb/'+liste[i]+'.pdb/'+liste[i]+'.pdb.vol.extended.vol'}">
				    <%
					context.write(liste[i])
				    %>
				</a>
                            </td>
			    <td>
                                
				<!-- moin jo, der link hier zeigt nun zu provi -->
				<a name="pdbfile" target="_blank" href="${proviurl+'/static/html/voro.html?example_json_url='+environurl+'/staticpdb/'+liste[i]+'.pdb/'+liste[i]+'.provi'}">
				    <%
					context.write(liste[i])
				    %>
				</a>
                            </td>
			    <td>
                                 <a name="singlezip"  style='padding-left: 15px' href="${h.url_for('tools/v4rna/generator/download2', filename='singlezip', task_id=2, codefile=liste[i])}">
				    <%
					context.write(liste[i])
				    %>
				 </a>
				 <%
                                    i=i+1
                                %>
                            </td>
                        </tr>
                    % endwhile
                    </tbody>
                        <tfoot>
                            
                        </tfoot>
                    </table>
                % endif
                </p>
                <h4>OR</h4>
                <fieldset id="example_1">
                    <legend>Calculate the atomic packing density with self-loaded RNA-structure:</legend>
                    <p style="text-indent:1.0em;">Please load a PDB-file:
                        <input name="data_pdb" type="file" value="pdb_datei" size="20" maxlength="100000" accept="text/*" />
                        <form:error name="data_pdb" />
                        <input class="clear_btn" type="button" value="Clear" />
                    </p>
                    
                </fieldset>
                <form:error name="blub" />
                <br>
                <a href="${h.url_for('tools/v4rna/generator/old_tasks')}">previous calculation tasks</a>
                <p><input type="submit" name="submit" value="submit" /> <input type="reset" value="reset all" />
                <br>
                
                
            </form>
        </div>
    </div>
</div>

