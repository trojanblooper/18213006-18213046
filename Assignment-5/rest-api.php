<?php
	function get_info_by_id($id){
		mysql_connect('localhost','root','');
		mysql_select_db('test');
		$a=mysql_query('SELECT * FROM Table1 WHERE Id='.$id);
		$b=mysql_fetch_array($a,MYSQL_ASSOC);		
		$info=array();
		$info=$b;
		return $info;
	}
	if (isset($_GET["action"])){
		switch($_GET["action"]){
			case "get_info";
			if (isset($_GET["id"]))
				$value=get_info_by_id($_GET["id"]);
			else
				$value='ERROR';
			break;
		}
	}
	exit (json_encode($value));
?>

