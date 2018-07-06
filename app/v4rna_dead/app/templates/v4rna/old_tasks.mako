<%inherit file="base.mako" />
<form action="form" method="post" enctype="multipart/form-data">
    <div id="content" class="content">
<!--       <script type="text/javascript">
	document.write("<div class='toggleNice' style='display:none;'>");
      </script> -->
<h1>Task List</h1>

<ul>
    % for t in task_list:
    <li><a href='${h.url_for('tools/v4rna/generator/task', task_id=t)}'>
	<%
		i=0
	%>
	% while i != (len(task_list)):	
		% if zeit[i][0]!=t:
			<%
				i=i+1
			%>
		% else:
			<%
				context.write(zeit[i][1])
				break
			%>
		% endif
	% endwhile
</a></li>
    % endfor
</ul>
    </div>
</form>
