<?php
session_start(); 
?>
<html>
<head>
<title>User Login</title>
</head>
<body bgcolor=green>
<?php
if($_SESSION["name"]) {
?>
<center>
<h1>
Welcome <?php echo $_SESSION["name"]; ?>. Click here to <a href="logout.php"
tite="Logout">Logout. 
</h1>
</center>
<?php
}else echo "<h1>Please login first .</h1>";
?>
</body>
</html>
