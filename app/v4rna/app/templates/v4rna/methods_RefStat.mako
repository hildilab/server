<%inherit file="base.mako" />

<form action="form" method="post" enctype="multipart/form-data">
    
        <div id="content" class="content">
<!--             <script type="text/javascript">
                document.write("<div class='toggleNice' style='display:none;'>");
            </script> -->
	
            <div>
                <h1>Reference dataset and Statistics</h1>


<h2>Reference dataset</h2>
Voronoia4RNA includes a dataset of presently 1766 PDB structures. All structures are considered containing at least one RNA chain and being obtained 
with a resolution of 3.5 Angstrom or better. Structures solved by NMR are generally also included.
<br>To calculate reference values, the non-redundant dataset of the <a target="_blank" 
href='http://rna.bgsu.edu/nrlist/lists/20120623/Nonredundant_3,5A.html'>BGSU RNA Structural Bioinformatics Group</a> is used. This dataset contains 621 
structures of RNA and complexes with a resolution of at least 3.5 Angstrom.




<h2>Statistics</h2>


<script type="text/javascript">
function popup (url) {
 fenster = window.open(url, "Popupfenster", "width=4000,height=2000,resizable=yes");
 fenster.focus();
 return false;
}
</script>




<a target="_blank" onclick="return popup(href='static/img/pdp.png');"
   F1 = window.open('static/img/pdp.png','Fenster1','width=400,height=200,left=0,top=0'); return false;"><img src="static/img/pdp.png" width="400" height="200" border="0" alt="Vorschaubild"></a>
<a target="_blank" onclick='return popup(href="static/img/pdpr.png");'
   F1 = window.open('static/img/pdpr.png','Fenster1','width=400,height=200,left=0,top=0'); return false;"><img src="static/img/pdpr.png" width="400" height="200" border="0" alt="Vorschaubild"></a>
<a target="_blank" onclick='return popup(href="static/img/pdr2.png");'
   F1 = window.open('static/img/pdr2.png','Fenster1','width=400,height=200,left=0,top=0'); return false;"><img src="static/img/pdr2.png" width="400" height="200" border="0" alt="Vorschaubild"></a>
<font size='1'>(to increase, please click on the figure)</font>
<br>
<a>
    The figures depict the average packing densities of the protors (figure 1), the protors per residue (figure 2) or the interdependency between packing 
densities, structure resolution and size (figure 3). Only the buried atoms of the structures of the reference dataset were taken into account.
<!--    <br>Represented by the pictures and the statistics, the packing density over the whole dataset is around 0,7. Although the difference between the 
residues (within one protor) is very marginal. -->
</a>



            <script type="text/javascript">
                document.write("</div>");
            </script>
        </div>
</form>
