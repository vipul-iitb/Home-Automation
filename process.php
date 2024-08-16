<html>
<?php
    $con=mysqli_connect("localhost","root","vipul1997*","home_auto");

    $username = $_POST['user'];
    $password = $_POST['pass'];
    $username = stripcslashes($username);
    $password = stripcslashes($password);
    $username =  mysqli_real_escape_string($con, $username);
    $password =  mysqli_real_escape_string($con, $password);

    $result = mysqli_query($con, "select * from login where username = '".$username."' and password = '".$password."'") or die ("Failed to que$

    $row = mysqli_fetch_array($result);

    if (!empty($row)) {
        echo "login succesfull";
        header("location:home.php");
    }
    else{ echo "failed to login"; }
?>

</html>

