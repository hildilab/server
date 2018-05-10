<%inherit file="base.mako" />

<h2>Wait</h2>
<input type="button" value="Reload Page" onClick="window.location.href=window.location.href" />

<pre>
${state}
</pre>