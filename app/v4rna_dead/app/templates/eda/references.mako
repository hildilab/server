<%inherit file="base.mako" />
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.6.2/jquery.min.js"></script>
<script language="javascript">
$(document).ready(function(){
    $("table1").hide()
    $("a#slideFade1").toggle(function(){
	$("table1").animate({ height: 'show', opacity: 'show' }, 'fast');
    },function(){
	$("table1").animate({ height: 'hide', opacity: 'hide' }, 'fast');
    });
    
    $("table2").hide()
    $("a#slideFade2").toggle(function(){
	$("table2").animate({ height: 'show', opacity: 'show' }, 'fast');
    },function(){
	$("table2").animate({ height: 'hide', opacity: 'hide' }, 'fast');
    });
    $("table3").hide()
    $("a#slideFade3").toggle(function(){
	$("table3").animate({ height: 'show', opacity: 'show' }, 'fast');
    },function(){
	$("table3").animate({ height: 'hide', opacity: 'hide' }, 'fast');
    });
    $("table4").hide()
    $("a#slideFade4").toggle(function(){
	$("table4").animate({ height: 'show', opacity: 'show' }, 'fast');
    },function(){
	$("table4").animate({ height: 'hide', opacity: 'hide' }, 'fast');
    });
    $("table5").hide()
    $("a#slideFade5").toggle(function(){
	$("table5").animate({ height: 'show', opacity: 'show' }, 'fast');
    },function(){
	$("table5").animate({ height: 'hide', opacity: 'hide' }, 'fast');
    });
    $("table6").hide()
    $("a#slideFade6").toggle(function(){
	$("table6").animate({ height: 'show', opacity: 'show' }, 'fast');
    },function(){
	$("table6").animate({ height: 'hide', opacity: 'hide' }, 'fast');
    });
	
});

</script>
        <div id="content" class="content">
<!--             <script type="text/javascript">
                document.write("<div class='toggleNice' style='display:none;'>");
            </script> -->
            <div>
                <h1>References</h1>
		    <h2>Generate Electron Density Maps</h2>
                    <li>
                        <div class="reference" id="ccp4">
                            <span class="title">The CCP4 Suite: Programs for Protein Crystallography</span>
                            <span class="authors">Collaborative Computational Project, Number 4</span>
                            <span class="magazine">Acta. Cryst.</span>
                            <span class="year">(1994)</span>
                            <span class="issue">D50, 760-763</span>
                        </div> 
                    </li>
                    <li>
                        <div class="reference" id="ccp4s">
                            <span class="title">Overview of the CCP4 suite and current developments</span>
                            <span class="authors">Winn M. D.</span>
                            <span class="magazine">Acta. Cryst.</span>
                            <span class="year">(2011)</span>
                            <span class="issue">D67, 235-242</span>
                        </div> 
                    </li>
                    <p>
                    <li style='padding-left:10px'> sigmaa references:
			      
                                <a href="#" id="slideFade1">show/hide</a></li>
				<ul>
                                <table1 border="0">
                                    <tr><td>
					<li>
					    <div class="reference" id="A42">
						<span class="title"></span>
						<span class="authors">Read, R.J.</span>
						<span class="magazine">Acta Cryst</span>
						<span class="year">(1986)</span>
						<span class="issue">A42, 140-149</span>
					    </div> 
					</li></td>
                                    </tr>
				    <tr><td>
					<li>
					    <div class="reference" id="20">
						<span class="title"></span>
						<span class="authors">Srinivasan, R.</span>
						<span class="magazine">Acta Cryst</span>
						<span class="year">(1966)</span>
						<span class="issue">20, 143-144</span>
					    </div> 
					</li></td>
                                    </tr>
				    <tr><td>
					<li>
					    <div class="reference" id="A38">
						<span class="title"></span>
						<span class="authors">Hauptman, H.</span>
						<span class="magazine">Acta Cryst</span>
						<span class="year">(1982)</span>
						<span class="issue">A38, 289-294</span>
					    </div> 
					</li></td>
                                    </tr>
				    <tr><td>
					<li>
					    <div class="reference" id="6">
						<span class="title"></span>
						<span class="authors">Luzzati, V.</span>
						<span class="magazine">Acta Cryst</span>
						<span class="year">(1953)</span>
						<span class="issue">6, 142-152</span>
					    </div> 
					</li></td>
                                    </tr>
				    <tr><td>
					<li>
					    <div class="reference" id="">
						<span class="title"></span>
						<span class="authors">Rogers, D in Computing Methods in Crystallography (Rollett, J.S.,ed.)</span>
						<span class="magazine">Pergamon Press</span>
						<span class="year">(1985)</span>
						<span class="issue">pp. 126-127</span>
					    </div> 
					</li></td>
                                    </tr>
				    <tr><td>
					<li>
					    <div class="reference" id="B26">
						<span class="title"></span>
						<span class="authors">Hendrickson, W.A. & Lattman, E.E.</span>
						<span class="magazine">Acta Cryst</span>
						<span class="year">(1970)</span>
						<span class="issue">B26, 136-143</span>
					    </div> 
					</li></td>
                                    </tr>
				    <tr><td>
					<li>
					    <div class="reference" id="A32">
						<span class="title"></span>
						<span class="authors">Bricogne, G.</span>
						<span class="magazine">Acta Cryst</span>
						<span class="year">(1976)</span>
						<span class="issue">A32, 832-847</span>
					    </div> 
					</li></td>
                                    </tr>
				    <tr><td>
					<li>
					    <div class="reference" id="12">
						<span class="title"></span>
						<span class="authors">Sim, G.A.</span>
						<span class="magazine">Acta Cryst</span>
						<span class="year">(1959)</span>
						<span class="issue">12, 813-815</span>
					    </div> 
					</li></td>
                                    </tr>
				    <tr><td>
					<li>
					    <div class="reference" id="13">
						<span class="title"></span>
						<span class="authors">Sim, G.A.</span>
						<span class="magazine">Acta Cryst</span>
						<span class="year">(1960)</span>
						<span class="issue">13, 511-512</span>
					    </div> 
					</li></td>
                                    </tr>
				    <tr><td>
					<li>
					    <div class="reference" id="A46">
						<span class="title"></span>
						<span class="authors">Read, R. J.</span>
						<span class="magazine">Acta Cryst</span>
						<span class="year">(1990)</span>
						<span class="issue">A46, 140-9</span>
					    </div> 
					</li></td>
                                    </tr>
				    <tr><td>
					<li>
					    <div class="reference" id="A46b">
						<span class="title"></span>
						<span class="authors">Read, R. J.</span>
						<span class="magazine">Acta Cryst</span>
						<span class="year">(1990)</span>
						<span class="issue">A46, 900-12.</span>
					    </div> 
					</li></td>
                                    </tr>
				    <tr> <td>
					<li>
					    <div class="reference" id="prep">
						<span class="title">manuscript in preparation</span>
						<span class="authors">Vellieux, F.M.D., Livnah, O., Dym, O., Read, R.J. & Sussman, J.L.</span>
						<span class="magazine"></span>
						<span class="year"></span>
						<span class="issue"></span>
					    </div> 
					</li></td>
                                    </tr>
                                </table1>
				</ul>
                    </p>
		    <p>
                     <li style='padding-left:10px'> sfall references:
			      
                                <a href="#" id="slideFade2">show/hide</a></li>
				<ul>
                                <table2 border="0">
                                    <tr><td>
					<li>
					    <div class="reference" id="A34">
						<span class="title"></span>
						<span class="authors">Agarwal, R.C.</span>
						<span class="magazine">Acta Cryst</span>
						<span class="year">(1978)</span>
						<span class="issue">A34, 791-809</span>
					    </div> 
					</li></td>
                                    </tr>
				    <tr><td>
					<li>
					    <div class="reference" id="1974">
						<span class="title">International Tables for X-ray Crystallography</span>
						<span class="authors"></span>
						<span class="magazine">Kynoch Press</span>
						<span class="year">(1974)</span>
						<span class="issue">Vol.IV</span>
					    </div> 
					</li></td>
                                    </tr>
				    <tr><td>
					<li>
					    <div class="reference" id="A33">
						<span class="title"></span>
						<span class="authors">Ten Eyck, L.F.</span>
						<span class="magazine">Acta Cryst</span>
						<span class="year">(1977)</span>
						<span class="issue">A33, 486</span>
					    </div> 
					</li></td>
                                    </tr>
				    <tr><td>
					<li>
					    <div class="reference" id="355">
						<span class="title"></span>
						<span class="authors">Bruenger, A.T.</span>
						<span class="magazine">Nature</span>
						<span class="year">(1992)</span>
						<span class="issue">355, 472-4</span>
					    </div> 
					</li></td>
                                    </tr>
				    <tr><td>
					<li>
					    <div class="reference" id="1995">
						<span class="title">International Tables for Crystallography</span>
						<span class="authors"></span>
						<span class="magazine">Kluwer</span>
						<span class="year">(1995)</span>
						<span class="issue">vol. C</span>
					    </div> 
					</li></td>
                                    </tr>
				    <tr><td>
					<li>
					    <div class="reference" id="">
						<span class="title">Refinement of protein structures</span>
						<span class="authors">Proceedings of the Daresbury Study Weekend 15-16 November (Compiled by P.S. Machin, J.W. Campbell and M. Elder)</span>
						<span class="magazine"></span>
						<span class="year">(1980)</span>
						<span class="issue"></span>
					    </div> 
					</li></td>
                                    </tr>
                                </table2>
				</ul>
		    </p>
		    <p>
		    <li style='padding-left:10px'> freerflag references:
			<a href="#" id="slideFade3">show/hide</a></li>
			<ul>
			<table3 border="0">
			    <tr><td>
				<li>
				    <div class="reference" id="355">
					<span class="title"></span>
					<span class="authors">A.T. Bruenger</span>
					<span class="magazine">Nature</span>
					<span class="year">(1992)</span>
					<span class="issue">355, 472-4</span>
				    </div> 
				</li></td>
			    </tr>
			    <tr> <td>
				<li>
				    <div class="reference" id="277">
					<span class="title">Free R Value: Cross-validation in crystallography</span>
					<span class="authors">A.T. Bruenger</span>
					<span class="magazine">Methods in Enzym</span>
					<span class="year"(1997)></span>
					<span class="issue">277, 366-396</span>
				    </div> 
				</li></td>
			    </tr>
			</table3>
			</ul>
		    </p>
		    
		    <p>
                    <li style='padding-left:10px'> fft references:
                                <a href="#" id="slideFade4">show/hide</a></li>
				<ul>
                                <table4 border="0">
                                    <tr><td>
					<li>
					    <div class="reference" id="p399">
						<span class="title">Crystallographic Computing Techniques</span>
						<span class="authors">A.Immirzi</span>
						<span class="magazine">ed. F.R.Ahmed, Munksgaard</span>
						<span class="year">(1966)</span>
						<span class="issue">p399</span>
					    </div> 
					</li></td>
                                    </tr>
				    <tr><td>
					<li>
					    <div class="reference" id="A29">
						<span class="title"></span>
						<span class="authors">L.F.Ten Eyck</span>
						<span class="magazine">Acta Cryst</span>
						<span class="year">(1973)</span>
						<span class="issue">A29, 183</span>
					    </div> 
					</li></td>
                                    </tr>
				    <tr><td>
					<li>
					    <div class="reference" id="21">
						<span class="title"></span>
						<span class="authors">R.J.Read and A.J.Schierbeek J.</span>
						<span class="magazine">Appl Cryst</span>
						<span class="year">(1988)</span>
						<span class="issue">21, 490-495</span>
					    </div> 
					</li></td>
                                    </tr>
				</table4>
				</ul>
                            </p>
		    <p>
                    <li style='padding-left:10px'> sfcheck references:
                                <a href="#" id="slideFade5">show/hide</a></li>
				<ul>
                                <table5 border="0">
                                    <tr><td>
					<li>
					    <div class="reference" id="d55">
						<span class="title">SFCHECK: a unified set of procedure for evaluating the quality of macromolecular structure-factor data and their agreement with atomic model.</span>
						<span class="authors">A.A.Vaguine, J.Richelle, S.J.Wodak.</span>
						<span class="magazine">Acta Cryst</span>
						<span class="year">(1999)</span>
						<span class="issue">D55, 191-205</span>
					    </div> 
					</li></td>
                                    </tr>
				</table4>
				</ul>
                            </p>
		<h2>Convert Electron Microscopy Maps</h2>
                    <li>
                        <div class="reference" id="mapman">
                            <span class="title">xdlMAPMAN and xdlDATAMAN - programs for reformatting, analysis and manipulation of biomacromolecular electron-density maps and reflection data sets</span>
                            <span class="authors">Kleywegt G.J., Jones T.A.</span>
                            <span class="magazine">Acta. Cryst.</span>
                            <span class="year">(1996)</span>
                            <span class="issue">D52, 826-828</span>
                        </div> 
                    </li>
		                        <p>
                    <li style='padding-left:10px'> more mapman references:
			      
                                <a href="#" id="slideFade6">show/hide</a></li>
				<ul>
                                <table6 border="0">
                                    <tr><td>
					<li>
					    <div class="reference" id="J5">
						<span class="title">Using known substructures in protein model building and crystallography</span>
						<span class="authors">T.A. Jones & S. Thirup</span>
						<span class="magazine">EMBO</span>
						<span class="year">(1986)</span>
						<span class="issue">J 5, 819-822</span>
					    </div> 
					</li></td>
                                    </tr>
				    <tr><td>
					<li>
					    <div class="reference" id="pp91">
						<span class="title">A, yaap, asap, @#*? A set of averaging programs</span>
						<span class="authors">T.A. Jones</span>
						<span class="magazine">In "Molecular Replacement", edited by E.J. Dodson, S. Gover and W. Wolf. SERC Daresbury Laboratory, Warrington</span>
						<span class="year">(1992)</span>
						<span class="issue">pp. 91-105 </span>
					    </div> 
					</li></td>
                                    </tr>
				    <tr><td>
					<li>
					    <div class="reference" id="pp59">
						<span class="title">Halloween ... Masks and Bones</span>
						<span class="authors">G.J. Kleywegt & T.A. Jones</span>
						<span class="magazine">In "From First Map to Final Model", edited by S. Bailey, R. Hubbard and D. Waller. SERC Daresbury Laboratory, Warrington</span>
						<span class="year">(1994)</span>
						<span class="issue">pp. 59-66</span>
					    </div> 
					</li></td>
                                    </tr>
				    <tr><td>
					<li>
					    <div class="reference" id="D52">
						<span class="title">xdlMAPMAN and xdlDATAMAN - programs for reformatting, analysis and manipulation of biomacromolecular electron-density maps and reflection data sets</span>
						<span class="authors">G.J. Kleywegt & T.A. Jones</span>
						<span class="magazine">Acta Cryst</span>
						<span class="year">(1996)</span>
						<span class="issue">D52, 826-828</span>
					    </div> 
					</li></td>
                                    </tr>
				    <tr><td>
					<li>
					    <div class="reference" id="pp32">
						<span class="title">Making the most of your search model</span>
						<span class="authors">G.J. Kleywegt</span>
						<span class="magazine">CCP4/ESF-EACBM Newsletter on Protein Crystallography 32, June 1996</span>
						<span class="year">(1996)</span>
						<span class="issue">pp. 32-36</span>
					    </div> 
					</li></td>
                                    </tr>
				    <tr><td>
					<li>
					    <div class="reference" id="5">
						<span class="title">Not your average density</span>
						<span class="authors">G.J. Kleywegt & R.J. Read</span>
						<span class="magazine">Structure</span>
						<span class="year">(1997)</span>
						<span class="issue">5, 1557-1569</span>
					    </div> 
					</li></td>
                                    </tr>
				    <tr><td>
					<li>
					    <div class="reference" id="d55941">
						<span class="title">Software for handling macromolecular envelopes</span>
						<span class="authors">G.J. Kleywegt & T.A. Jones</span>
						<span class="magazine">Acta Cryst</span>
						<span class="year">(1999)</span>
						<span class="issue">D55, 941-944</span>
					    </div> 
					</li></td>
                                    </tr>
				    <tr><td>
					<li>
					    <div class="reference" id="d551878">
						<span class="title">Experimental assessment of differences between related protein crystal structures</span>
						<span class="authors">G.J. Kleywegt</span>
						<span class="magazine">Acta Cryst</span>
						<span class="year">(1999)</span>
						<span class="issue">D55, 1878-1857</span>
					    </div> 
					</li></td>
                                    </tr>
				    <tr><td>
					<li>
					    <div class="reference" id="pp123">
						<span class="title">Density modification: theory and practice</span>
						<span class="authors">R.J. Read & G.J. Kleywegt</span>
						<span class="magazine">In: "Methods in Macromolecular Crystallography" (D Turk & L Johnson, Eds.), IOS Press, Amsterdam</span>
						<span class="year">(2001)</span>
						<span class="issue">pp. 123-135</span>
					    </div> 
					</li></td>
                                    </tr>
				    <tr><td>
					<li>
					    <div class="reference" id="ch171">
						<span class="title">Around O</span>
						<span class="authors">Kleywegt, G.J., Zou, J.Y., Kjeldgaard, M. & Jones, T.A.</span>
						<span class="magazine">In: "International Tables for Crystallography, Vol. F. Crystallography of Biological Macromolecules" (Rossmann, M.G. & Arnold, E., Editors)</span>
						<span class="year">(2001)</span>
						<span class="issue">Chapter 17.1, pp. 353-356, 366-367</span>
					    </div> 
					</li></td>
                                    </tr>
                                </table6>
				</ul>
		    
                    </p>
            </div>
        </div>