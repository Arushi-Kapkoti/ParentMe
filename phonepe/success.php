<?php
$am = $_POST['amount'];
echo "Transaction Status:".$_POST['code']."<br>";
echo "Transaction ID:".$_POST['transactionId']."<br>";
echo "Amount Transferred: Rs." . ($_POST['amount'] / 100) . " <br>";
echo "Reference ID:".$_POST['providerReferenceId']."<br>";
// print_r($_POST['code']);
echo "<h3> Close the Window </h3>";
?>