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
<!--            <script type="text/javascript">
                document.write("<div class='toggleNice' style='display:none;'>");
            </script> -->
            <h1>Voronoia for RNA Calculation - Results</h1>
            <div class="subcontent">
                <div>
                    <form action="form" method="post" enctype="multipart/form-data">
                        <fieldset id="example_1"><legend>Download the files:</legend>
                            <p>
                                %if (file_status['volfile']):
                                    The vol file:<br>
                                    <a name="volfile"  style='padding-left: 15px' href="${h.url_for('tools/v4rna/generator/download', filename='volfile', task_id=task_id)}">vol-file</a><br>
                                %endif
                            </p>
                            <p>
                                %if (file_status['exvol']):
                                    The vol file:<br>
                                    <a name="exvol"  style='padding-left: 15px' href="${h.url_for('tools/v4rna/generator/download', filename='exvol', task_id=task_id)}">extended vol-file</a><br>
                                %endif
                            </p>
                            <p>
                                %if (file_status['provi']):
                                    Visualization:<br>
                                    <a name="provi" target="_blank" href="${proviurl+'/static/html/voro.html?example_json_url='+environurl+'/staticjob/'+provipath}">Visualization</a><br>
                                %endif
                            </p>

                            <p>
                                %if (file_status['info']):
                                    The info file:<br>
                                    <a name="info"  style='padding-left: 15px' href="${h.url_for('tools/v4rna/generator/download', filename='info', task_id=task_id)}">info-file</a><br>
                                %endif
                            </p>
                            <p>
                                %if (file_status['stdout']):
                                    The error file:<br>
                                    <a name="stdout"  style='padding-left: 15px' href="${h.url_for('tools/v4rna/generator/download', filename='stdout', task_id=task_id)}">error-file</a><br>
                                %endif
                            </p>
                            <p>
                                %if (file_status['stderr']):
                                    The error file:<br>
                                    <a name="stderr"  style='padding-left: 15px' href="${h.url_for('tools/v4rna/generator/download', filename='stderr', task_id=task_id)}">error-file</a><br>
                                %endif
                            </p>
                        <br>
           <!--             All files compressed into zip format:
                        <p><a name="allzip"  style='padding-left: 300px' href="${h.url_for('tools/v4rna/generator/download', filename='allzip', task_id=task_id)}">download all</a></p>
                        -->
                        </fieldset>
                    </form>
                </div>
            </div>
            <script type="text/javascript">
                document.write("</div>");
            </script>
