<?php
include "book_d.php";
if (isset($_POST['uid']))
{
    // echo "ok";
    // echo $_POST['uid'];
    $uid = $_POST['uid'];
    $price = $_POST['price'];
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
    $d1 = (int)$_POST['d1'];
    $d2 = (int)$_POST['d2'];
    $d3 = (int)$_POST['d3'];
    $d4 = (int)$_POST['d4'];
    if ($price > $money)
    {
        echo "0"; //不够钱0
    }
    else
    {
        echo "1"; //够钱1
        //扣钱
        $use = (float)-1 * $price;
        $money1 = (float)$money - $price;
        $sql1 = "INSERT INTO {$uid} (`money`,`use`,`date`) VALUES ( $money1,$use,NOW() );";
        mysqli_query($conn, $sql1);
        $b = (new Book_d())->run($uid,$d1,$d2,$d3,$d4);
    }
}
else
{
    echo "...........";
}

$conn->close(); 
?>