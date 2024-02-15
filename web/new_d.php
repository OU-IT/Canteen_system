<?php 
class new_d{
    public function run($num){
        $servername = "localhost"; //地址  
        $username = "root"; //名  
        $password = "root"; //密码  
        $dbname = "dish"; //库名
        $conn = new mysqli($servername, $username, $password, $dbname);
        $sql = "CREATE TABLE s{$num} (d1 INT,d2 INT,d3 INT,d4 INT,date DATE);";
        mysqli_select_db( $conn, $dbname );
        mysqli_query($conn, $sql);
    }
}

?>