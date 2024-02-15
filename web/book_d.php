<?php

class Book_d
{
    public function run($uid,$d1,$d2,$d3,$d4)
    {
        $uid = $_POST['uid'];
        $price = $_POST['price'];
        $servername = "localhost"; //地址  
        $username = "root"; //名  
        $password = "root"; //密码  
        $dbname = "dish"; //库名
        $conn = new mysqli($servername, $username, $password, $dbname);
        $sql = "INSERT INTO {$uid} (`d1`,`d2`,`d3`,`d4`,`date`) VALUES ($d1,$d2,$d3,$d4,NOW());";
        mysqli_select_db( $conn, $dbname );
        mysqli_query($conn, $sql);
    }
}


?>