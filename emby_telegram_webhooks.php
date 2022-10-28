<?php
//You should add var for post to telegram
$chat = "-XXXXXXXXX";
$bot_id = "botXXXXXXXXXXXXXX";
$url = "https://api.telegram.org/$bot_id/sendPhoto";
$emby_domain = "http://XXXXXXXXXXXXXXXXX";

//recieve webhooks
$data = $_POST['data'];
$unescaped_data = stripslashes($data);
$obj = json_decode($unescaped_data);

//get params from Emby event library.new
if  ($obj->Event == "library.new") {

	if  ($obj->Item->Type == "Episode") {
		$title = $obj->Title;
		$id = $obj->Item->SeriesId;
		$description = $obj->Description;
		if (isset($description)) {
			$photo = "$emby_domain/Items/$id/Images/Primary";
		} else {
			$photo = "https://emby.media/resources/shutterstock_1434923111.jpg";
		}
	}
	if  ($obj->Item->Type == "Movie") {
		$title = $obj->Title;
		$id = $obj->Item->Id;
		$description = $obj->Description;
		if (isset($description)) {
			$photo = "$emby_domain/Items/$id/Images/Primary";
		}else {
			$photo = "https://emby.media/resources/shutterstock_1434923111.jpg";
		}
  }

//form caption and post array
$caption = "New element:\n$title\n$description:\n$description";
$post_fields = array( 'chat_id' => $chat, 'photo' => $photo, 'caption' => $caption);

//cUrl to telegram
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($curl, CURLOPT_HEADER, false);
curl_setopt($curl, CURLOPT_POST, true);
curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, $post_fields);
$output = curl_exec($ch);
curl_close($ch);
}
?>
