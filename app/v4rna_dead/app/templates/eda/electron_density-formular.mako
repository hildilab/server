<%inherit file="base.mako" />


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
    <h1>Electron Density Calculation</h1>
    <div class="subcontent">
        <div>
            <form action="form" method="post" enctype="multipart/form-data">
                <h3>Required:</h3>
                <fieldset id="example_1">
                    <legend>Load the files independent:</legend>
                    <p style="text-indent:1.0em;">Please choose a sf.cif-file or a mtz-file:
                        <input name="data_cif" type="file" value="cif_datei" size="20" maxlength="100000" accept="text/*" />
                        <form:error name="data_cif" />
                        <input class="clear_btn" type="button" value="Clear" />
                    </p>
                    <p style="text-indent:1.0em;">Please choose a pdb-file: 
                        <input name="data_pdb" type="file" value="pdb_datei" size="20" maxlength="100000" accept="text/*" />
                        <form:error name="data_pdb" />
                        <input class="clear_btn" type="button" value="Clear" />
                    </p>
                </fieldset>
                <h4>OR</h4>
                <fieldset id="example_2">
                    <legend>Get the files from the PDB:</legend>
                    <p style="text-indent:1.0em;">Enter PDB-Entry <img src="/static/img/helpbubble.png" alt="logo" title="e.g.: 3DQB"></img>
                        <input name="data_idpdb" type="text" value="from_pdb" size="10" maxlength="10" />
                        <form:error name="data_idpdb" />
                    </p>
                </fieldset>
                <form:error name="blub" />
                <br>
                <p><input type="submit" name="submit" value="submit" /> <input type="reset" value="reset all" /></p>
                <br>
                <br>
                <h3>Optional:</h3>
                <fieldset id="example_5">
                    <legend>Validation:</legend>
                        <input type="checkbox" id="sfcheck" name="sfcheck" value="sfcheck" checked="checked"><label for="sfcheck" >sfcheck </label><img src="/static/img/helpbubble.png" alt="logo" title="A program for assessing the agreement between the atomic model and X-ray data"></img>
                        <form:error name="sfcheck" />
                        <input type="checkbox" id="omit" name="omit" value="omit" checked="checked"><label for="omit" >omit map by sfcheck (time intensive: >10 min)</label><img src="/static/img/helpbubble.png" alt="logo" title="An omit map is a way to reduce the model bias in the electron density calculated with model phases."></img>
                        <form:error name="omit" />
                </fieldset>
                <fieldset id="example_3">
                    <legend>Outputmaps:</legend>
                    <form:error name="maptype" />
                    <input type="hidden" name="topic" value="maptypes" />
                        <table border="0">
                            <tr>
                                <td>2fo-fc Map: <img src="/static/img/helpbubble.png" alt="logo" title="A sigmaa weighted map to guide the construction of a new model"></img></td>
                                <td><input type="checkbox" id="maptype_2fofc_as" name="subtopics" value="tfofc_as" checked="checked"><label for="maptype_2fofc_as"> around asymmetric unit</label></td>
                                <td><input type="checkbox" id="maptype_2fofc_al" name="subtopics" value="tfofc_al" checked="checked"><label for="maptype_2fofc_al"> around all atoms in PDB</label></td>
                            </tr>
                            <tr>
                                <td>fo-fc Map: <img src="/static/img/helpbubble.png" alt="logo" title="Difference map to identify errors in a model"></img></td>
                                <td><input type="checkbox" id="maptype_fofc_as" name="subtopics" value="fofc_as" checked="checked"><label for="maptype_fofc_as"> around asymmetric unit</label></td>
                                <td><input type="checkbox" id="maptype_fofc_al" name="subtopics" value="fofc_al" checked="checked"><label for="maptype_fofc_al"> around all atoms in PDB</label></td>
                            </tr>
                        </table>
                        <form:error name="subtopics" />
                </fieldset>
                <fieldset id="example_4">
                    <legend>Extension of the maps:</legend>
                        <input type="radio" id="mapext_map" name="mapext" value="dotmap"><label for="mapext_map"> save as .map (e.g. for <a href="http://biop.ox.ac.uk/coot/" target="_blank">COOT</a>)</label><br>
                        <input type="radio" id="mapext_ccp4" name="mapext" value="dotccp4"><label for="mapext_ccp4"> save as .ccp4 (e.g. for <a href="http://www.pymol.org/" target="_blank">PYMOL</a>)</label><br>
                        <form:error name="mapext" />
                </fieldset>
                <p><input type="submit" name="submit" value="submit" /> <input type="reset" value="reset all" /></p>
            </form>
        </div>
    </div>
</div>
