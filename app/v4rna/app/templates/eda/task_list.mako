<%inherit file="base.mako" />

<h2>Task List</h2>

<ul>
    % for t in task_list:
    <li><a href='${h.url_for('/tools/eda/task', task_id=t)}'>${t}</a></li>
    % endfor
</ul>