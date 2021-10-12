<?php
/* Database credentials. Assuming you are running MySQL
server with default setting (user 'root' with no password) */

 define('DB_SERVER', 'localhost');
 define('DB_USERNAME', 'root');
 define('DB_PASSWORD', '');
 define('DB_NAME', 'images');

/* Attempt to connect to MySQL database
   Create a database if none exists. */

$baselink = mysqli_connect(DB_SERVER, DB_USERNAME, DB_PASSWORD);

// Check connection
if($baselink === false){

    die("ERROR: Could not connect. " . mysqli_connect_error());

} else {

	$sqlCreateDB = "CREATE DATABASE IF NOT EXISTS ".DB_NAME;

    $sqlImage  = "CREATE TABLE IF NOT EXISTS images (

        image_id INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
        file_name VARCHAR(250) NOT NULL,
        upload_date datetime NOT NULL);";

    

    /*========= DATABASE CREATION =========*/

	if ($baselink->query($sqlCreateDB) === TRUE) {
  		#echo "Database ".DB_NAME." created successfully <br>";

	} else {
  		#echo "Error creating table: " . $link->error;
	}

	/*========= TABLE CREATION =========*/

	$baselink = mysqli_connect(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_NAME);


	if ($baselink->query($sqlImage) === TRUE) {
  		#echo "Table images created successfully <br>";
	} else {
  		#echo "Error creating table: " . $baselink->error."<br>";
	}

    
}
?>
