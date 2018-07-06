<%inherit file="base.mako" />

<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.6.2/jquery.min.js"></script>
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
<script language="javascript">
$(document).ready(function(){
    $("table1").hide()
    $("a#slideFade1").toggle(function(){
	$("table1").animate({ height: 'show', opacity: 'show' }, 'fast');
    },function(){
	$("table1").animate({ height: 'hide', opacity: 'hide' }, 'fast');
    });
	
});

</script>
        <div id="content" class="content">
<!--            <script type="text/javascript">
                document.write("<div class='toggleNice' style='display:none;'>");
            </script> -->
            <h1>EM Converter</h1>
            <div class="subcontent">
                <div>
                    <form action="form" method="post" enctype="multipart/form-data">
                        <fieldset id="example_1">
                            <legend>Load the file independent: </legend>
                            <a href="#" id="slideFade1">supported input formats</a></li>
                        <ul>
                        <table1 border="0">
                            PROTEIN, FFT-Y, TENEYCK2, CCP4, X-PLOR, OLDEZD, MASK,
                            NEWEZD, BINXPLOR, BRICK, DSN6, 3DMATRIX, TNT, PHASES, FSMASK,
                            BRIX, XPLOR, CNS, EZD, EM08, OMAP, MPI, AMBER
                        </table1>
                        </ul>
                            <p style="text-indent:1.0em;">Please choose a EM-file:<br>
                                <input name="data" type="file" value="pdb_datei" size="50" maxlength="100000" accept="text/*" />
                                <form:error name="data" />
                            </p>
                            <input class="clear_btn" type="button" value="Clear" />
                        </fieldset>
                        <form:error name="blub" />
                        <br>
                        <h3>Required information:</h3>
                        <fieldset id="example_3"> 	<legend>Outputmap:</legend>
                            <form:error name="maptype" />
                            <p>
                                <select name="maptype" size="5">
                                    <option value='CCP4' selected="selected">CCP4</option>
                                    <option value='MAP'>MAP</option>
                                    <option value='OLDEZD'>OLDEZD</option>
                                    <option value='MASK'>MASK</option>
                                    <option value='NEWEZD'>NEWEZD</option>
                                    <option value='ENVELOPE'>ENVELOPE</option>
                                    <option value='X-PLOR'>X-PLOR</option>
                                    <option value='DSN6'>DSN6</option>
                                    <option value='BRIX'>BRIX</option>
                                    <option value='XPLOR'>XPLOR</option>
                                    <option value='CNS'>CNS</option>
                                    <option value='EZD'>EZD</option>
                                    <option value='AMORE'>AMORE</option>
                                    <option value='OMAP'>OMAP</option>
                                    <option value='TURBO'>TURBO</option>
                                    <option value='MP'>MP</option>
                                </select>
                            </p>
                            <input class="clear_btn" type="button" value="Clear" />
                        </fieldset>
                        <p><input type="submit" name="submit" value="submit" /> <input type="reset" value="reset all" /></p>
                    </form>
                </div>
            </div>
        </div>