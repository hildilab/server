<%inherit file="base.mako" />
<div id="content" class="content">
<h1>Wait or go ahead</h1>
<input type="button" value="Reload Page" onClick="window.location.href=window.location.href" />
<pre>
<!--${state}-->
The calculations are still running.
Please wait, see the results afterwards <a href="${h.url_for('tools/v4rna/generator/old_tasks')}">here</a> or under *Search & Calculate* --> previous 
calculation tasks.
<!--Your task-id is: ${task_id}-->
</pre>
</div>
