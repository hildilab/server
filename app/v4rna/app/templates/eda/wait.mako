<%inherit file="base.mako" />
<div id="content" class="content">
<h1>Wait</h1>
<input type="button" value="Reload Page" onClick="window.location.href=window.location.href" />
<meta http-equiv="refresh" content="3" />
<pre>
<!--${state}-->
Please wait.
</pre>
</div>