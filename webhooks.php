<?php
//You shoud add var for your server request , api key, text, warning and timeout for pop up
$server = "https://domain.emby.local";
$Text='Hello%20World';
$Header='warning';
$TimeoutMs='10000';
$api_key='XXXXXXXXXXXXXXXXXXX';

//function for send cUrl Post
function cUrlGetData($url, $post_fields = null, $headers = null) {

    $ch = curl_init();
    $timeout = 5;
    curl_setopt($ch, CURLOPT_URL, $url);

    if (!empty($post_fields)) {

        curl_setopt($ch, CURLOPT_POST, 1);
        curl_setopt($ch, CURLOPT_POSTFIELDS, $post_fields);
    }

    if (!empty($headers))
        curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);

    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 2);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 1);
    curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, $timeout);
    $data = curl_exec($ch);

    if (curl_errno($ch)) {

        echo 'Error:' . curl_error($ch);
    }

    curl_close($ch);
    return $data;
}

//recieve webhooks get session_id
$data = $_POST['data'];
$unescaped_data = stripslashes($data);
$obj = json_decode($unescaped_data);
$id = $obj->Session->Id;

//generate post for action playback.start
if  ($obj->Event == "playback.start") {

$url = "$server/emby/Sessions/$id/Message?Text=$Text&Header=$Header&TimeoutMs=$TimeoutMs&api_key=$api_key";
$post_fields = "Text=$Text&Header=$Header&TimeoutMs=$TimeoutMs&api_key=$api_key";
$headers = ["accept: */*"];
$dat = cUrlGetData($url, $post_fields, $headers);

}
?>
