<%inherit file="base.mako" />

<h2>Form</h2>

<form action="form" method="post" enctype="multipart/form-data">
    
    <div>
        <input type="file" name="pdb_file" />
        <form:error name="pdb_file" />
    </div>
    
    <div>
        <input type="text" name="probe_radius" />
        <form:error name="probe_radius" />
        <form:iferror name="probe_radius">invalid probe radius</form:iferror>
    </div>
    
    <div>
        <input type="submit" name="submit" value="send" />
    </div>
    
</form>