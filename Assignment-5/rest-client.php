<?php
	if isset($_GET["action"])&&isset($_GET["id"])&&isset($_GET["action"]=="get_info"){
		$info=file_get_contents('http://localhost/rest-api.php?action=get_info&id=' . $_GET["id"]);
		echo $info;
		$info=json_decode($info,true);
		echo $info;
	}
?>
