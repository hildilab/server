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
        <div id="content" class="content">
<!--            <script type="text/javascript">
                document.write("<div class='toggleNice' style='display:none;'>");
            </script> -->
            <h1>Brix to MAP Converter</h1>
            <div class="subcontent">
                <div>
                    <form action="form" method="post" enctype="multipart/form-data">
                        <fieldset id="example_1">
                            <legend>Load the file independent:</legend>
                            <p style="text-indent:1.0em;">Please choose a brix-file:<br>
                                <input name="data" type="file" value="pdb_datei" size="50" maxlength="100000" accept="text/*" />
                                <form:error name="data" />
                            </p>
                            <input class="clear_btn" type="button" value="Clear" />
                        </fieldset>
                        <br>
                        <p><input type="submit" name="submit" value="submit" /> <input type="reset" value="reset all" /></p>
                    </form>
                </div>
            </div>
        </div>