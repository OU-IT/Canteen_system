<!DOCTYPE html>  
<html>  
<head>  
    <title>welcome</title>  
</head>  
<body>  
    <h1>菜单:</h1>  
    <form action="" method="post">  
        <input type="submit" name="button" value="充值" />  
        <input type="submit" name="button" value="查询" />  
        <input type="submit" name="button" value="添加学生" />  
        <input type="submit" name="button" value="建议" />  
    </form>  
      
    <?php  
    if (isset($_POST['button'])) {  
        $button = $_POST['button'];  
          
        switch ($button) {  
            case '充值':  
                header('Location: chong.php');  
                break;  
            case '查询':  
                header('Location: sele.php');  
                break;  
            case '添加学生':  
                header('Location: new.php');  
                break;  
            case '建议':  
                header('Location: sug.php');  
                break;  
            default:   
                break;  
        }  
        exit;
    }  
    ?>  
</body>  
</html>