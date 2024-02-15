<?php
class Sample {
    const API_KEY = "usB297au143OeqjZ8sxulz3l";
    const SECRET_KEY = "Fwreu4mHHdQY9qdA3XwTgHr5s3dPkUgp";

    public function run($file) {  
        $curl = curl_init();  
        curl_setopt_array($curl, array(  
            CURLOPT_URL => "https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/add?access_token={$this->getAccessToken()}",  
            CURLOPT_TIMEOUT => 30,  
            CURLOPT_RETURNTRANSFER => true,  
            CURLOPT_SSL_VERIFYPEER  => false,  
            CURLOPT_SSL_VERIFYHOST  => false,  
            CURLOPT_CUSTOMREQUEST => 'POST',   
            CURLOPT_POSTFIELDS => "{\"group_id\":\"1\",\"image\":\"{$this->getFileContentAsBase64($file)}\",\"image_type\":\"BASE64\",\"user_id\":\"s4\"}",  
            CURLOPT_HTTPHEADER => array(  
                'Content-Type: application/json'  
            ),  
        ));  
        $response = curl_exec($curl);  
        curl_close($curl);  
        echo "{\"group_id\":\"1\",\"image\":\"{$this->getFileContentAsBase64($file)}\",\"image_type\":\"BASE64\",\"user_id\":\"s4\"}";
        return $response;  
    }  
      
    public function getFileContentAsBase64($path){  
        return urldecode(urlencode(base64_encode(file_get_contents($path))));  
    }
    

    private function getAccessToken(){
        $curl = curl_init();
        $postData = array(
            'grant_type' => 'client_credentials',
            'client_id' => self::API_KEY,
            'client_secret' => self::SECRET_KEY
        );
        curl_setopt_array($curl, array(
            CURLOPT_URL => 'https://aip.baidubce.com/oauth/2.0/token',
            CURLOPT_CUSTOMREQUEST => 'POST',
            CURLOPT_SSL_VERIFYPEER  => false,
            CURLOPT_SSL_VERIFYHOST  => false,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_POSTFIELDS => http_build_query($postData)
        ));
        $response = curl_exec($curl);
        curl_close($curl);
        $rtn = json_decode($response);
        return $rtn->access_token;
    }
}

$rtn = (new Sample())->run('q.jpg');
print_r($rtn);