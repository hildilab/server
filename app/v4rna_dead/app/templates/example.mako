<form action="form" method="post">
    <input type="text" name="text" />
    <form:error name="text" />
    
    <input type="text" name="integer" />
    <form:error name="integer" />
    <form:iferror name="integer">Integer error message</form:iferror>
    
    <input type="submit" value="send" />
</form>