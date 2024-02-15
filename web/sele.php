<!DOCTYPE html>  
<html>  
<head>  
    <title>查询</title>  
</head>  
<body>  
    <h1>查询</h1>  
  
    <form method="POST" action="">  
        <label for="input">请输入学号：</label>  
        <input type="text" name="input" id="input" required>  
        <br>  
        <input type="submit" name="submit" value="查询">  
    </form> 
    <?php  
    error_reporting(0);
    //检提交  
    if (isset($_POST['submit'])) {  
        //值  
        $inputValue = (int)$_POST['input'];  
        if (is_int($inputValue)) {  
            //连接  
            $servername = "localhost"; //地址  
            $username = "root"; //名  
            $password = "root"; //密码  
            $dbname = "stu"; //库名
  
            $conn = new mysqli($servername, $username, $password, $dbname);  
  
            //是否成功  
            if ($conn->connect_error) {  
                die("连接mysql出错");  
            }  
  
            //查询语句  
            $sql = "SELECT * FROM "."s".$inputValue.";";  
            

            //结果
            $result = $conn->query($sql);   
            if ($result->num_rows > 0) {  
                //输出结果  
                while ($row = $result->fetch_assoc()) {  
                    echo "余额: " . $row["money"] . "-------支出/收入: " . $row["use"] ."--------日期:".$row["date"]. "<br>";  
                }  
            } 
  
            //连接  
            $conn->close();  
        }
    }  
    ?>  
  
 
</body>  
</html>