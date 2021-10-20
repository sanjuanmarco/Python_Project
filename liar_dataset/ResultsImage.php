<!DOCTYPE HTML>
<html>
	<head>
		<title>Confirmation</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<link rel="stylesheet" href="assets/bootstrap/css/bootstrap.min.css" />
		<link rel="stylesheet" href="assets/css/main.css?version=1" />
		<noscript><link rel="stylesheet" href="assets/css/noscript.css" /></noscript>

		<!-- Loadin Screen -->
		<style type="text/css">
		#loader {
  			display: none;
  			position: fixed;
  			top: 0;
  			left: 0;
  			right: 0;
  			bottom: 0;
  			width: 100%;
  			background: rgba(0,0,0,1) url(images/request.gif) no-repeat center center;
  			z-index: 10000;
		}
		</style>

	</head>
	<body class="is-preload">

		<!-- Wrapper -->
			<div id="wrapper">

				<!-- Header -->
				<header id="header" class="alt">
				<a href="Homepage.php" class="logo"><strong>Home</strong></a>
					<nav>
						<a href="#menu">Menu</a>
					</nav>
				</header>

				<!-- Menu -->
				<nav id="menu">
					<ul class="links">
		                <li> <a href="Homepage.php">Home </a> </li>

		                <li> <a href="About.php">About Us</a> </li>

		                <li> <a href="Members.php">Developers</a> </li>
				
            		</ul>
				</nav>

				<!-- Banner -->
					<section id="banner" class="major">
						<div class="inner">
							<p><b>Please confirm if the text is the same as seen on the image.<br>
							Results will be based on the translated text.</b>
							</p>

								<!-- Input Field -->
								<p align="justify">
								<?php
								include 'config.php';
								$file = $_FILES['file'];
								$statusMsg = '';
								$targetDir ='uploads/';
								$fileName = $file['name'];
								$tempName = $file["tmp_name"];
								$updatedFileName = str_replace(' ','-', $fileName);
								$path = $targetDir.$updatedFileName;
								$fileType = pathinfo($path, PATHINFO_EXTENSION);
								
								if(isset($_POST["Submit"]) && !empty($_FILES["file"]["name"])){
									// Allow certain file formats
									$allowTypes = array('jpg','png','jpeg','gif','pdf');
									if (!file_exists($path)) {
										if(in_array($fileType, $allowTypes)){
												// Upload file to server
											if(move_uploaded_file($tempName, $path)){
												// Insert image file name into database
												// $insert = $link->query("INSERT into images (file_name, uploaded_on) VALUES ('".$fileName."', NOW())");
												$sql = "INSERT INTO images ($updatedFileName, upload_date) VALUES (?,?)";
												if($stmt = mysqli_prepare($link, $sql)){
													// Bind variables to the prepared statement as parameters
													mysqli_stmt_bind_param($stmt, "ss",$param_img_id, $param_upload_date);										
													// Set parameters
													$param_img_id = $fileName;
													$param_upload_date = date('m.d.y');
													// Attempt to execute the prepared statement
													if(mysqli_stmt_execute($stmt)){
														// Redirect to login page
													} else{
														echo "Something went wrong. Please try again later.";
													}
										
													// Close statement
													mysqli_stmt_close($stmt);
												}
											}else{
												$statusMsg = "Sorry, there was an error uploading your file.";
											}
										}else{
											$statusMsg = "Sorry, only JPG, JPEG, PNG, GIF, & PDF files are allowed to upload.";
										}
									}
								}else{
									$statusMsg = 'Please select a file to upload.';
								}

								echo $statusMsg; 

								$data = $path;
								echo shell_exec("py -3.9 ocr.py $data 2>&1");
								?>
									<br> 
								
								<p>
								<!-- accuracy -->
								</p>				
								<p></p>
								<ul class="actions">
								
								<li><a href="Homepage.php" class="button">Try another</a> <a id="confirm" name="butt" href="ImageConfirm.php" class="button">Confirm</a></li>
								</ul>
								</form>
								</p>
								
								
								
							
						</div>
					</section>

				<!-- Main -->
					<div id="main">
							<!-- About us -->
							<section>
								<div class="inner">
									<header class="major">
										<h2>Disclaimer</h2>
									</header>
									<p align="justify">SVM Fake News Detector is a web-based application that uses machine learning to classify articles and images as factual or fake. 
									SVM Fake News Detector uses support vector machine (SVM) to effectively train and test data sets in order to categorize user inputs 
									based on the degree of accuracy it provides. This application relies on supervised learning (human-coded dataset) and focused web 
									crawling to allow for relative accuracy. It outputs an accuracy score along with several classifications that measure the likelihood 
									that the input has factual or false information.</p>
									<ul class="actions">
										<li><a href="About.php" class="button next">Read more</a></li>
									</ul>
								</div>
							</section>

							

							

				<!-- Footer -->
				<footer id="footer">
					<div class="inner">
						
						<ul class="copyright">
							<li>Copyright © 2021 MS Team - Template by:</li>
							<li> <a href="https://www.phpjabbers.com/">PHPJabbers.com</a></li>
						</ul>
					</div>
				</footer>

			</div>

		<!-- Scripts -->
			<script src="assets/js/jquery.min.js"></script>
			<script src="assets/bootstrap/js/bootstrap.bundle.min.js"></script>
			<script src="assets/js/jquery.scrolly.min.js"></script>
			<script src="assets/js/jquery.scrollex.min.js"></script>
			<script src="assets/js/browser.min.js"></script>
			<script src="assets/js/breakpoints.min.js"></script>
			<script src="assets/js/util.js"></script>
			<script src="assets/js/main.js"></script>
			<script>
				$(document).ready(function(){
  					$("#confirm").on("button", function(){
    					$("#loader").fadeIn();
  					});//submit
				});//document ready
			</script>

	</body>
</html>


