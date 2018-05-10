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
            <h1>Electron Density Calculator - Results</h1>
            <div class="subcontent">
                <div>
                    Thanks for using our tool!<br>
                    The results will be send to you via e-mail after finishing.
                </div>
            </div>
            <script type="text/javascript">
                document.write("</div>");
            </script>