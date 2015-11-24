<?php
	/*function getnews($u){
		include_once('simple_html_dom.php');
		$target_url = "http://news.okezone.com/kampus";
		$html = new simple_html_dom();
		$html->load_file($target_url);
		foreach($html->find('div[class=content-hardnews]') as $post)
		{
		echo $post."<br />";
		}
	}*/
include_once('simple_html_dom.php');
$target_url = "http://news.okezone.com/kampus";
$html = new simple_html_dom();
$html->load_file($target_url);
foreach($html->find('div[class=content-hardnews]') as $post)
{
echo $post."<br />";
}
?>
