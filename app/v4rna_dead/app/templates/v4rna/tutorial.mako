<%inherit file="base.mako" />

<form action="form" method="post" enctype="multipart/form-data">
    
        <div id="content" class="content">
<!--             <script type="text/javascript">
                document.write("<div class='toggleNice' style='display:none;'>");
            </script> -->
	
            <div>
                <h1>Viewer Tutorial</h1>
<script type="text/javascript">
function popup (url) {
 fenster = window.open(url, "Popupfenster", "width=4000,height=2000,resizable=yes");
 fenster.focus();
 return false;
}
</script>
<table>
    <tr>
	<td>
	    <a target="_blank" onclick="return popup(href='static/img/screenshot.png');" F1 = window.open('static/img/screenshot.png','Fenster1','width=100%'); return 
false;"><img src="static/img/screenshot.png" width="100%" border="0" alt="Vorschaubild"></a>
	    <br> click to increase the picture
	</td>
	<td>
	    <a>On startup Provi shows the desired structure in the "ribbon and aromatic" style, coloured according to the packing densities. Internal cavities are represented as simple balls. </a>
	    <br>
	    <a>In three widgets the visualization styles for general settings, cavities and packing densities can be altered. </a><br><br>
	</td>
    </tr>
    <tr>
	<td>
	    <a target="_blank" onclick="return popup(href='static/img/general.png');" F1 = window.open('static/img/general.png','Fenster1','width=50%'); return false;"><img 
src="static/img/general.png" width="50%" border="0" alt="Vorschaubild"><br><br>
	</td>
	<td>
	    <a>In the first widget you can find the general controls: style, selections and center options</a>
	</td>
    </tr>
    <tr>
	<td>
	    <a target="_blank" onclick="return popup(href='static/img/cavity.png');" F1 = window.open('static/img/cavity.png','Fenster1','width=50%'); return false;"><img 
src="static/img/cavity.png" width="50%" border="0" alt="Vorschaubild"><br><br>
	</td>
	<td>
	    <a>The second widget holds the controls for the visualization of the cavities. there are two different ways to represent the cavities.As simple balls (blue checkbox), which is the most 
proper way to look at all cavities of a structure. </a>
	    <br><br>
	</td>
    </tr>
    <tr>
	<td>
	    <a target="_blank" onclick="return popup(href='static/img/cavityeinzeln.png');" F1 = window.open('static/img/cavityeinzeln.png','Fenster1','width=100%'); return 
false;"><img src="static/img/cavityeinzeln.png" width="100%" border="0" alt="Vorschaubild"><br><br>
	</td>
	<td>
	    <a>To inspect a specific cavity are more detailed view is provided where the exact shape is shown (red checkbox). The green checkbox selects the atoms that are neighbouring the cavity. </a>
	    <br><br>
	</td>
    </tr>
    <tr>
	<td>
	    <a target="_blank" onclick="return popup(href='static/img/Pcking.png');" F1 = window.open('static/img/Pcking.png','Fenster1','width=50%'); return false;"><img 
src="static/img/Pcking.png" width="50%" border="0" alt="Vorschaubild"><br><br>
	</td>
	<td>
	    <a>In the third widget the different visualization modes for the packing densities are located. You can choose whether the packing range occurring in the file or a user-defined range is used 
and what colour scheme is used.</a>
	    <br><br>
	</td>
    </tr>
    <tr>
	<td>
	    <a target="_blank" onclick="return popup(href='static/img/cpk.png');" F1 = window.open('static/img/cpk.png','Fenster1','width=100%'); return false;"><img 
src="static/img/cpk.png" width="100%" border="0" alt="Vorschaubild"><br><br>
	</td>
	<td>
	    <a>To get an atom wise representation of the packing density a detailed representation style like cpk should be selected.</a>
	</td>
    </tr>
</table>
            <script type="text/javascript">
                document.write("</div>");
            </script>
        </div>
</form>
