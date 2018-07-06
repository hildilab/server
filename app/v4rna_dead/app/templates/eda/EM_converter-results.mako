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
 <!--<script type="text/javascript">
  document.write("<div class='toggleNice' style='display:none;'>");
 </script> -->
 <h1>EM Converter - Results</h1>
 <div class="subcontent">
  <div>
   <form action="form" method="post" enctype="multipart/form-data">
    <fieldset id="example_1"><legend>Download the files independent:</legend>
     <p>
      %if (file_status['ccp4']):
       The output maps:<br>
      %elif (file_status['map']):
       The output maps:<br>
      %elif (file_status['oldezd']):
       The output maps:<br>
      %elif (file_status['mask']):
       The output maps:<br>
      %elif (file_status['newezd']):
       The output maps:<br>
      %elif (file_status['envelope']):
       The output maps:<br>
      %elif (file_status['x-plor']):
       The output maps:<br>
      %elif (file_status['dsn6']):
       The output maps:<br>
      %elif (file_status['brix']):
       The output maps:<br>
      %elif (file_status['xplor']):
       The output maps:<br>
      %elif (file_status['cns']):
       The output maps:<br>
      %elif (file_status['ezd']):
       The output maps:<br>
      %elif (file_status['amore']):
       The output maps:<br>
      %elif (file_status['omap']):
       The output maps:<br>
      %elif (file_status['turbo']):
       The output maps:<br>
      %elif (file_status['mp']):
       The output maps:<br>
      %endif
      %if (file_status['ccp4']):
       <a name="ccp4" href="${h.url_for('/tools/eda/converter/download', filename='ccp4', task_id=task_id)}">The ccp4 file</a><br>
      %endif
      %if (file_status['map']):
       <a name="map" href="${h.url_for('/tools/eda/converter/download', filename='map', task_id=task_id)}">The map file</a><br>
      %endif
      %if (file_status['oldezd']):
       <a name="oldezd" href="${h.url_for('/tools/eda/converter/download', filename='oldezd', task_id=task_id)}">The oldezed file</a><br>
      %endif
      %if (file_status['mask']):
       <a name="mask" href="${h.url_for('/tools/eda/converter/download', filename='mask', task_id=task_id)}">The mask file</a><br>
      %endif
      %if (file_status['newezd']):
       <a name="newezd" href="${h.url_for('/tools/eda/converter/download', filename='newezd', task_id=task_id)}">The newezd file</a><br>
      %endif
      %if (file_status['envelope']):
       <a name="envelope" href="${h.url_for('/tools/eda/converter/download', filename='envelope', task_id=task_id)}">The envelope file</a><br>
      %endif
      %if (file_status['x-plor']):
       <a name="x-plor" href="${h.url_for('/tools/eda/converter/download', filename='x-plor', task_id=task_id)}">The x-plor file</a><br>
      %endif
      %if (file_status['dsn6']):
       <a name="dsn6" href="${h.url_for('/tools/eda/converter/download', filename='dsn6', task_id=task_id)}">The dsn6 file</a><br>
      %endif
      %if (file_status['brix']):
       <a name="brix" href="${h.url_for('/tools/eda/converter/download', filename='brix', task_id=task_id)}">The brix file</a><br>
      %endif
      %if (file_status['xplor']):
       <a name="xplor" href="${h.url_for('/tools/eda/converter/download', filename='xplor', task_id=task_id)}">The xplor file</a><br>
      %endif
      %if (file_status['cns']):
       <a name="cns" href="${h.url_for('/tools/eda/converter/download', filename='cns', task_id=task_id)}">The cns file</a><br>
      %endif
      %if (file_status['ezd']):
       <a name="ezd" href="${h.url_for('/tools/eda/converter/download', filename='ezd', task_id=task_id)}">The ezd file</a><br>
      %endif
      %if (file_status['amore']):
       <a name="amore" href="${h.url_for('/tools/eda/converter/download', filename='amore', task_id=task_id)}">The amore file</a><br>
      %endif
      %if (file_status['omap']):
       <a name="omap" href="${h.url_for('/tools/eda/converter/download', filename='omap', task_id=task_id)}">The omap file</a><br>
      %endif
      %if (file_status['turbo']):
       <a name="turbo" href="${h.url_for('/tools/eda/converter/download', filename='turbo', task_id=task_id)}">The turbo file</a><br>
      %endif
      %if (file_status['mp']):
       <a name="mp" href="${h.url_for('/tools/eda/converter/download', filename='mp', task_id=task_id)}">The mp file</a><br>
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
     <a name="allzip" href="${h.url_for('/tools/eda/converter/download', filename='allzip', task_id=task_id)}">download all</a><br>
    </fieldset>
   </form>
  </div>
 </div>
</div>