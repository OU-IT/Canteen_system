<!DOCTYPE html>  
<html>  
<head>  
    <title>添加学生</title>  
</head>  
<body>  
    <h1>添加学生</h1>  
    
    <?php  
    include 'UptoBaidu.php';
    include 'new_d.php';
    #error_reporting(0);
    $num = $_POST['num'];
    $servername = "localhost"; //地址  
    $username = "root"; //名  
    $password = "root"; //密码  
    $dbname = "stu"; //库名
    $conn = new mysqli($servername, $username, $password, $dbname);
    if ($conn->connect_error) {  
        die("连接mysql出错");  
    }
    $sql = "SELECT * FROM information_schema.TABLES WHERE TABLE_NAME = 's".$num."'".";";  //查是否已经存在
    $result = $conn->query($sql);
    if ($result->num_rows > 0)
    {
        die("学生已存在");
    }
    else
    {// 检查是否有文件上传  
        if (isset($_FILES['file'])) 
        {  
            $file = $_FILES['file'];  
    
            // 检查文件类型是否为 JPG  
            $fileType = $file['type'];  
            if ($fileType == 'image/jpeg') 
            {  
                // 指定上传目录  
                $uploadDir = 'face/';    
    
                
                $fileName = 's' . $num . '.jpg';  

                $id = 's' . $num;

                $rtn = (new upbd())->run($file['tmp_name'],$id); //调用百度API

                $dertn = json_decode($rtn,true);

    
                // 移动上传的文件到目标目录  
                $targetPath = $uploadDir . $fileName;  

                if($dertn['error_code'] == 0)
                {
                    if (move_uploaded_file($file['tmp_name'], $targetPath)) 
                    {  
                        echo "上传成功！";
                        echo $num;  
                    
                        $sql1 = "CREATE TABLE s{$num} (
                            `id` INT UNSIGNED AUTO_INCREMENT,
                            `money` FLOAT,  
                            `use` FLOAT,  
                            `date` DATE,
                            PRIMARY KEY (id));";
                        $sql2 = "INSERT INTO s{$num} (`money`,`use`,`date`) VALUES (0,0,NOW());";
                        mysqli_select_db( $conn, $dbname );
                        mysqli_query($conn, $sql1);
                        mysqli_query($conn, $sql2);
                        $new_d = (new new_d())->run($num);


                    } 
                    else 
                    {  
                        echo "上传失败！";  
                    }
                }
                else
                {
                    echo "上传失败！";  
                }
            } 
            else 
            {  
                echo "只允许上传 JPG 格式的图片！";  
            }  
        }
    }
    $conn->close();
    ?>  
    <form method="POST" enctype="multipart/form-data" action="">  
        <h1>输入学号(确定后无法修改)</h1>
        <input type="text" name="num" id="num" required />  
        <br />
        <label for="file">请选择文件(only JPG):</label>  
        <input type="file" name="file" id="file" required>  
        <br>  
        <input type="submit" value="上传">  
    </form>  
</body>  
</html>