<!DOCTYPE html>  
<html>  
<head>  
    <title>充值</title>  
</head>  
<body>  
    <h1>充值</h1>  
  
    <form method="POST" action="">  
        <label for="input">请输入学号：</label>  
        <input type="text" name="uid" id="uid" required>  
        <br>

        <label for="input">请输入金额：</label>  
        <input type="text" name="moeny" id="moeny" required>  
        <br>

        <label for="input">请输入管理员密码：</label>  
        <input type="text" name="password" id="password" required>  
        <br>  
        <input type="submit" name="submit" value="确定">  
    </form>
<?php
$pw = "admin123";
if(isset($_POST['submit']))
{
    $password = $_POST['password'];
    if($pw == $password)
    {
        $uid = (int)$_POST['uid'];
        error_reporting(0);
        $num = $_POST['num'];
        $servername = "localhost"; //地址  
        $username = "root"; //名  
        $password = "root"; //密码  
        $dbname = "stu"; //库名
        $conn = new mysqli($servername, $username, $password, $dbname);

        if ($conn->connect_error) 
        {  
            die("连接mysql出错");  
        }

        $select_uid = "SELECT * FROM information_schema.TABLES WHERE TABLE_NAME = 's".$uid."'".";";
        $uid_result = $conn->query($select_uid);
        if ($uid_result->num_rows > 0)
        {
            $money = (float)$_POST['moeny'];
            $select_moeny_sql = "select * from s{$uid} order by id desc limit 1;";
            $moeny_result = $conn->query($select_moeny_sql);
            $row = $moeny_result->fetch_assoc();
            $moeny1 = $row['moeny'];
            $moeny2 = $moeny1 + $money;
            $add_moeny = "INSERT INTO s{$uid} (`money`,`use`,`date`) VALUES ($moeny2,$money,NOW())";
            mysqli_query($conn, $add_moeny);
            echo "学号：".$uid."成功充值".$money."元";
        }
        else
        {
            die("没有此学生");
        }
    }
    else
    {
        die("密码错误");
    }
}
?>