<%inherit file="base.mako" />

<form action="form" method="post" enctype="multipart/form-data">
    <div id="content" class="content">
<!--       <script type="text/javascript">
	document.write("<div class='toggleNice' style='display:none;'>");
      </script> -->
      <h1>ELECTRON DENSITY - Webserver: </h1>
      <div id="teaser" align="center">
	<img src="/static/img/logo.jpg" width="300" height="300" alt="logo" />
	<!-- <img src="/static/img/logo.jpg" alt="example result" /> -->
      </div>
      <h2>Motivation</h2>
      <div class="contentblock">
	<div class="textblock">
	  <p>
	    
	    Nowadays, where one structure is following another, there
	    needs to be time to deal with them - particular as it is easy to get
	    evaluated electron density maps for instance by Uppsala Electron-Density
	    Server, linked to the Protein Data Bank. 
	    This webservice gives the opportunity to evaluate structures by the
	    electron density nearest to the raw data.
	    
	    <br>In contrast to the EDS (which alike provides
	    Electron Density Maps), our attention relys on density maps nearest to
	    the raw data (where no interpretation of programs has been
	    accomplished) to be possible to compare the experimental data
	    (structure factors) to the structure, given and often interpreted
	    by the crystallographers and thereby published in the Protein Data Bank.
	    
	    <br>The maps depend on the experimental data deposited in the
	    Protein Data Bank or loaded from the user themselves.
	    
	    <br>In addition to electron density maps there is the opportunity to evaluate
	    the density maps by the sfcheck-module of CCP4 and to generate a so called
	    total omit map. As well,  there is the possibility to convert microscopy
	    maps into other formats by mapman.
	    
	    
	    <!--It goes without saying that the reader, casual or not, should have
	    access to model coordinates, experimental data and electron-density maps!-->
	    
	    
	    <br/>
	  </p>
	  <p class="textblock"> 
	  </p>
	</div>
	<div class="spaceblock">
	  Summary
	</div>
      </div>
      <script type="text/javascript">
	document.write("</div>");
      </script>
    </div>
</form>