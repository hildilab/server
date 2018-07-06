<%inherit file="base.mako" />
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.6.2/jquery.min.js"></script>
<script language="javascript">
$(document).ready(function(){
    $("table").hide()
    $("a#slideFade").toggle(function(){
        $("table").animate({ height: 'show', opacity: 'show' }, 'fast');
    },function(){
        $("table").animate({ height: 'hide', opacity: 'hide' }, 'fast');
    })
});
</script>  
        <div id="content" class="content">
<!--             <script type="text/javascript">
                document.write("<div class='toggleNice' style='display:none;'>");
            </script> -->
            <h1>Brix to MAP Converter - Results</h1>
            <div class="subcontent">
                <div>
                    <form action="form" method="post" enctype="multipart/form-data">
                        <fieldset id="example_1"><legend>Download the files independent:</legend>
                            <p>
                                %if (file_status['map']):
                                    The output map:<br>
                                %endif
                                %if (file_status['map']):
                                    <a name="map" href="${h.url_for('/tools/eda/converter/download', filename='map', task_id=task_id)}">The map file</a><br>
                                %endif
                            </p>
                            <p>
                                Log and Debug Files:
                                <a href="#" id="slideFade">show/hide</a><br>
                                <table border="0">
                                    <tr>
                                        %if (file_status['log']):
                                            <td><a name="log" href="${h.url_for('/tools/eda/converter/download', filename='log', task_id=task_id)}">log-File</a></td>
                                        %endif
                                        %if (file_status['debug']):
                                            <td><a name="debug" href="${h.url_for('/tools/eda/converter/download', filename='debug', task_id=task_id)}">debug-File</a></td>
                                        %endif
                                    </tr>
                                </table>
                            </p>
                        <br>
                        <p><a name="allzip" href="${h.url_for('/tools/eda/converter/download', filename='allzip', task_id=task_id)}">download all</a></p>
                        </fieldset>
                    </form>
                </div>
            </div>
        </div>