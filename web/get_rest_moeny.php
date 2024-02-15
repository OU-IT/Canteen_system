<?php

if (isset($_POST['uid']))
{
    // echo "ok";
    // echo $_POST['uid'];
    $uid = $_POST['uid'];
    $servername = "localhost"; //地址  
    $username = "root"; //名  
    $password = "root"; //密码  
    $dbname = "stu"; //库名
    $conn = new mysqli($servername, $username, $password, $dbname);
    if ($conn->connect_error) {  
        die("连接mysql出错");  
    }
    $sql = "select * from {$uid} order by id DESC limit 1;";

    $result = $conn->query($sql);
    $row = $result->fetch_assoc();
    $money = $row['money'];
    echo $money;
}

$conn->close(); 
?>