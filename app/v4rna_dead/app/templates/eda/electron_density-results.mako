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
                    <form action="form" method="post" enctype="multipart/form-data">
                        <fieldset id="example_1"><legend>Download the files independent:</legend>
                            <p>
                                %if (file_status['inputpdb'] and file_status['inputcif']):
                                    The input files:<br>
                                    <a name="inputpdb"  style='padding-left: 15px' href="${h.url_for('/tools/eda/generator/download', filename='inputpdb', task_id=task_id)}">pdb-file</a><br>
                                    <a name="inputcif"  style='padding-left: 15px' href="${h.url_for('/tools/eda/generator/download', filename='inputcif', task_id=task_id)}">cif-file</a><br>
                                %elif (file_status['inputpdb']):
                                    The input file:<br>
                                    <a name="inputpdb"  style='padding-left: 15px' href="${h.url_for('/tools/eda/generator/download', filename='inputpdb', task_id=task_id)}">pdb-file</a><br>
                                %elif (file_status['inputcif']):
                                    The input file:<br>
                                    <a name="inputcif"  style='padding-left: 15px' href="${h.url_for('/tools/eda/generator/download', filename='inputcif', task_id=task_id)}">cif-file</a><br>
                                %elif (file_status['inputmtz']):
                                    The input file:<br>
                                    <a name="inputmtz"  style='padding-left: 15px' href="${h.url_for('/tools/eda/generator/download', filename='inputmtz', task_id=task_id)}">mtz-file</a><br>
                                %endif
                            </p>
                            <p>
                                %if (file_status['2maptm']):
                                    The output files:<br>
                                %elif (file_status['2mapsm']):
                                    The output files:<br>
                                %elif (file_status['1maptm']):
                                    The output files:<br>
                                %elif (file_status['1mapsm']):
                                    The output files:<br>
                                %elif (file_status['2maptc']):
                                    The output files:<br>
                                %elif (file_status['2mapsc']):
                                    The output files:<br>
                                %elif (file_status['1maptc']):
                                    The output files:<br>
                                %elif (file_status['1mapsc']):
                                    The output files:<br>
                                %elif (file_status['mtzfile']):
                                    The output files:<br>
                                %elif (file_status['sfcheckpdf']):
                                    The output files:<br>
                                %elif (file_status['2fobsfcalc']):
                                    The output files:<br>
                                %elif (file_status['2fobsfcalcc']):
                                    The output files:<br>
                                %elif (file_status['omitphases']):
                                    The output files:<br>
                                %endif
                                %if (file_status['2maptm']):
                                    <a name="2maptm" style='padding-left: 15px' href="${h.url_for('/tools/eda/generator/download', filename='2maptm', task_id=task_id)}">2fo-fc map with all atoms out of the pdb</a><br>
                                %endif
                                %if (file_status['2maptc']):
                                    <a name="2maptc" style='padding-left: 15px' href="${h.url_for('/tools/eda/generator/download', filename='2maptc', task_id=task_id)}">2fo-fc map with all atoms out of the pdb</a><br>
                                %endif
                                %if (file_status['2mapsm']):
                                    <a name="2mapsm" style='padding-left: 15px' href="${h.url_for('/tools/eda/generator/download', filename='2mapsm', task_id=task_id)}">2fo-fc map with all atoms around the asymmetric unit</a><br>
                                %endif
                                %if (file_status['2mapsc']):
                                    <a name="2mapsc" style='padding-left: 15px' href="${h.url_for('/tools/eda/generator/download', filename='2mapsc', task_id=task_id)}">2fo-fc map with all atoms around the asymmetric unit</a><br>
                                %endif
                                %if (file_status['1maptm']):
                                    <a name="1maptm" style='padding-left: 15px' href="${h.url_for('/tools/eda/generator/download', filename='1maptm', task_id=task_id)}">fo-fc map with all atoms out of the pdb</a><br>
                                %endif
                                %if (file_status['1maptc']):
                                    <a name="1maptc" style='padding-left: 15px' href="${h.url_for('/tools/eda/generator/download', filename='1maptc', task_id=task_id)}">fo-fc map with all atoms out of the pdb</a><br>
                                %endif
                                %if (file_status['1mapsm']):
                                    <a name="1mapsm" style='padding-left: 15px' href="${h.url_for('/tools/eda/generator/download', filename='1mapsm', task_id=task_id)}">fo-fc map with all atoms around the asymmetric unit</a><br>
                                %endif
                                %if (file_status['1mapsc']):
                                    <a name="1mapsc" style='padding-left: 15px' href="${h.url_for('/tools/eda/generator/download', filename='1mapsc', task_id=task_id)}">fo-fc map with all atoms around the asymmetric unit</a><br>
                                %endif
                                %if (file_status['mtzfile']):
                                    <a name="mtzfile" style='padding-left: 15px' href="${h.url_for('/tools/eda/generator/download', filename='mtzfile', task_id=task_id)}">generated mtz-file</a><br>
                                %endif
                                %if (file_status['sfcheckpdf']):
                                    <a name="sfcheckpdf" style='padding-left: 15px' href="${h.url_for('/tools/eda/generator/download', filename='sfcheckpdf', task_id=task_id)}">sfcheck-pdf</a><br>
                                %endif
                                %if (file_status['2fobsfcalc']):
                                    <a name="2fobsfcalc" style='padding-left: 15px' href="${h.url_for('/tools/eda/generator/download', filename='2fobsfcalc', task_id=task_id)}">Total OMIT map calculated with sfcheck</a><br>
                                %endif
                                %if (file_status['2fobsfcalcc']):
                                    <a name="2fobsfcalcc" style='padding-left: 15px' href="${h.url_for('/tools/eda/generator/download', filename='2fobsfcalcc', task_id=task_id)}">Total OMIT map calculated with sfcheck</a><br>
                                %endif
                                %if (file_status['omitphases']):
                                    <a name="omitphases" style='padding-left: 15px' href="${h.url_for('/tools/eda/generator/download', filename='omitphases', task_id=task_id)}">OMIT Phases (Fp,Ph,FOM)</a><br>
                                %endif
                            </p>
                            <p>
                                Log and Debug Files:
                                <a href="#" id="slideFade">show/hide</a><br>
                                <table border="0">
                                    <tr>
                                        %if (file_status['log']):
                                        <tr>
                                            <td><a name="log" href="${h.url_for('/tools/eda/generator/download', filename='log', task_id=task_id)}">log-File</a></td>
                                        %endif
                                        %if (file_status['debug']):
                                            <td><a name="debug" href="${h.url_for('/tools/eda/generator/download', filename='debug', task_id=task_id)}">debug-File</a></td>
                                        %endif
                                    </tr>
                                    <tr>
                                        %if (file_status['logcm']):
                                            <td><a name="logcm" href="${h.url_for('/tools/eda/generator/download', filename='logcm', task_id=task_id)}">log-File: cif to mtz</a></td>
                                        %endif
                                        %if (file_status['debugcm']):
                                            <td><a name="debugcm" href="${h.url_for('/tools/eda/generator/download', filename='debugcm', task_id=task_id)}">debug-File: cif to mtz</a></td>
                                        %endif
                                    </tr>
                                    <tr>
                                        %if (file_status['logfc']):
                                            <td><a name="logfc" href="${h.url_for('/tools/eda/generator/download', filename='logfc', task_id=task_id)}">log-File: fourier calculation</a></td>
                                        %endif
                                        %if (file_status['debugfc']):
                                            <td><a name="debugfc" href="${h.url_for('/tools/eda/generator/download', filename='debugfc', task_id=task_id)}">debug-File: fourier calculation</a></td>
                                        %endif
                                    </tr>
                                    <tr>
                                        %if (file_status['log1s']):
                                            <td><a name="log1s" href="${h.url_for('/tools/eda/generator/download', filename='log1s', task_id=task_id)}">log-File: run-fft_nf1-as</a></td>
                                        %endif
                                        %if (file_status['debug1s']):
                                            <td><a name="debug1s" href="${h.url_for('/tools/eda/generator/download', filename='debug1s', task_id=task_id)}">debug-File: run-fft_nf1-as</a></td>
                                        %endif
                                    </tr>
                                    <tr>
                                        %if (file_status['log1t']):
                                            <td><a name="log1t" href="${h.url_for('/tools/eda/generator/download', filename='log1t', task_id=task_id)}">log-File: run-fft_nf1-at</a></td>
                                        %endif
                                        %if (file_status['debug1t']):
                                            <td><a name="debug1t" href="${h.url_for('/tools/eda/generator/download', filename='debug1t', task_id=task_id)}">debug-File: run-fft_nf1-at</a></td>
                                        %endif
                                    </tr>
                                    <tr>
                                        %if (file_status['log2s']):
                                            <td><a name="log2s" href="${h.url_for('/tools/eda/generator/download', filename='log2s', task_id=task_id)}">log-File: log_run-fft_nf2-as</a></td>
                                        %endif
                                        %if (file_status['debug2s']):
                                            <td><a name="debug2s" href="${h.url_for('/tools/eda/generator/download', filename='debug2s', task_id=task_id)}">debug-File: log_run-fft_nf2-as</a></td>
                                        %endif
                                    </tr>
                                    <tr>
                                        %if (file_status['log2t']):
                                            <td><a name="log2t" href="${h.url_for('/tools/eda/generator/download', filename='log2t', task_id=task_id)}">log-File: log_run-fft_nf2-at</a></td>
                                        %endif
                                        %if (file_status['debug2t']):
                                            <td><a name="debug2t" href="${h.url_for('/tools/eda/generator/download', filename='debug2t', task_id=task_id)}">debug-File: log_run-fft_nf2-at</a></td>
                                        %endif
                                    </tr>
                                    
                                    <tr>
                                        %if (file_status['logsfextra']):
                                            <td><a name="logsfextra" href="${h.url_for('/tools/eda/generator/download', filename='logsfextra', task_id=task_id)}">extra log-File from sfcheck additional to the pdf </a></td>
                                        %endif
                                        %if (file_status['logsf']):
                                            <td><a name="logsf" href="${h.url_for('/tools/eda/generator/download', filename='logsf', task_id=task_id)}">log-File: sfcheck-validation</a></td>
                                        %endif
                                        %if (file_status['debugsf']):
                                            <td><a name="debugsf" href="${h.url_for('/tools/eda/generator/download', filename='debugsf', task_id=task_id)}">debug-File: sfcheck-validation</a></td>
                                        %endif
                                    </tr>
                                    <tr>
                                        %if (file_status['logomit']):
                                            <td><a name="logomit" href="${h.url_for('/tools/eda/generator/download', filename='logomit', task_id=task_id)}">log-File: generate a sfcheck-omit map</a></td>
                                        %endif
                                        %if (file_status['debugomit']):
                                            <td><a name="debugomit" href="${h.url_for('/tools/eda/generator/download', filename='debugomit', task_id=task_id)}">debug-File: generate a sfcheck-omit map</a></td>
                                        %endif
                                    </tr>
                                </table>
                            </p>
                        <br>
                        All files compressed into zip format:
                        <p><a name="allzip"  style='padding-left: 300px' href="${h.url_for('/tools/eda/generator/download', filename='allzip', task_id=task_id)}">download all</a></p>
                        </fieldset>
                    </form>
                </div>
            </div>
            <script type="text/javascript">
                document.write("</div>");
            </script>