<style>
  .btn {
  background: #3498db;
  background-image: -webkit-linear-gradient(top, #3498db, #2980b9);
  background-image: -moz-linear-gradient(top, #3498db, #2980b9);
  background-image: -ms-linear-gradient(top, #3498db, #2980b9);
  background-image: -o-linear-gradient(top, #3498db, #2980b9);
  background-image: linear-gradient(to bottom, #3498db, #2980b9);
  -webkit-border-radius: 28;
  -moz-border-radius: 28;
  border-radius: 28px;
  font-family: Arial;
  color: #ffffff;
  font-size: 13px;
  padding: 10px 20px 10px 20px;
  text-decoration: none;
}

.btn:hover {
  background: #3cb0fd;
  background-image: -webkit-linear-gradient(top, #3cb0fd, #3498db);
  background-image: -moz-linear-gradient(top, #3cb0fd, #3498db);
  background-image: -ms-linear-gradient(top, #3cb0fd, #3498db);
  background-image: -o-linear-gradient(top, #3cb0fd, #3498db);
  background-image: linear-gradient(to bottom, #3cb0fd, #3498db);
  text-decoration: none;
}
</style>
<?php
$apiKey = "58a63b64-574d-417a-9214-066bee1e4caa";
$merchantId = "ATMOSTUAT";
$keyIndex=1;

$paymentData = array(
    'merchantId' => "ATMOSTUAT",
    'merchantTransactionId' => "MT7850590068188104",
    "merchantUserId"=>"MUID123",
    'amount' => 1000, // Amount in paisa (10 INR)
    'redirectUrl'=>"http://localhost/phonepe/success.php",
    'redirectMode'=>"POST",
    'callbackUrl'=>"http://localhost/phonepe/success.php",
    "merchantOrderId"=> "8556225",
    "mobileNumber"=>"9876543210",
    "message"=>"Payment of Rs. 10",
    "email"=>"test@gmail.com",
    "shortName"=>"Test",
    "paymentInstrument"=> array(    
    "type"=> "PAY_PAGE",
  )
);
$jsonencode = json_encode($paymentData);
$payloadMain = base64_encode($jsonencode);

$salt_index = 1; //key index 1
$payload = $payloadMain . "/pg/v1/pay" . $apiKey;
$sha256 = hash("sha256", $payload);
$final_x_header = $sha256 . '###' . $salt_index;
$request = json_encode(array('request'=>$payloadMain));

$curl = curl_init();
curl_setopt_array($curl, [
  CURLOPT_URL => "https://api-preprod.phonepe.com/apis/pg-sandbox/pg/v1/pay",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
   CURLOPT_POSTFIELDS => $request,
  CURLOPT_HTTPHEADER => [
    "Content-Type: application/json",
     "X-VERIFY: " . $final_x_header,
     "accept: application/json"
  ],
]);
 
$response = curl_exec($curl);
$err = curl_error($curl);
 
curl_close($curl);
 
if ($err) {
  echo "cURL Error #:" . $err;
} else {
   $res = json_decode($response);
 


if(isset($res->success) && $res->success=='1'){
$paymentCode=$res->code;
$paymentMsg=$res->message;
$payUrl=$res->data->instrumentResponse->redirectInfo->url;
 
// echo "<h3>Click on the following link to Pay by UPI</br></h3>";
// echo "</br><center><a class='btn' href='".$payUrl."'> Pay Now </a></center>";
header('Location:'.$payUrl) ;
}
}
?>