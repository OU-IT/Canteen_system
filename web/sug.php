<!DOCTYPE html>  
<html>  
<head>  
    <title>提个建议</title>  
</head>  
<body>  
    <h1>提出你的宝贵建议:</h1>  
    <form action="" method="post">  
        <label for="suggestion">建议:</label>  
        <input type="text" name="suggestion" id="suggestion" required />  
        <br />  
        <input type="submit" name="submit" value="确定" />  
    </form>  
      
    <?php  
    if (isset($_POST['submit'])) {  
        $suggestion = $_POST['suggestion'];  

          
        // 打开文件以追加写入，如果文件不存在则创建它  
        $file = fopen('1.txt', 'a');  
          
        // 将建议写入文件  
        fwrite($file, $suggestion . PHP_EOL);  
          
        // 关闭文件  
        fclose($file);  
          
        echo '感谢您的宝贵建议!';  
    }  
    ?>  
</body>  
</html>