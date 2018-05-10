<%inherit file="base.mako" />
<div id="content" class="content">
    <h2>Error</h2>
    <pre>
        <br>  
        <h4><p style="text-indent:60px;">${fehler}</p></h4>
        Please send a <a href="mailto:mailto:peter.hildebrand@charite.de?subject=%B5ERROR%20EDW%D5&%20${job}%C2&%20${session}">mail</a> with the job- and the session-id.
        If possible, please also send the input files.
        <br>
        job-id = ${job}
        session-id = ${session}
    </pre>
</div>
