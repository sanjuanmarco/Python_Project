<!DOCTYPE HTML>
<html>
	<head>
		<title>Results</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		
		<link rel="stylesheet" href="assets/bootstrap/css/bootstrap.min.css" />
		<link rel="stylesheet" href="assets/css/main.css?version=1" />
		<noscript><link rel="stylesheet" href="assets/css/noscript.css" /></noscript>

		<!-- For Columns -->
		<style>
		* {
  			box-sizing: border-box;
		}

		/* Create two equal columns that floats next to each other */
		.column {
  			float: left;
  			width: 50%;
			padding-right: 20px;
		}

		/* Clear floats after the columns */
		.row:after {
  			content: "";
  			display: table;
  			clear: both;
		}

		/* Responsive layout - makes the two columns stack on top of each other instead of next to each other */
		@media screen and (max-width: 600px) {
  		.column {
   			 width: 100%;
  		}
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
					<section id="banner2" class="major">
						<div class="inner">
							<div class="column">
								
								<!-- Input Field -->
								<p>
								<b>RESULTS</b><br>

								
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
								$res = exec("py -3.9 ocr.py $data 2>&1", $output, $var);
								$str = implode(" ",$output);
								if (strpos($str, "Probability score:") !== false) {
									$substring = substr($str, 0, strpos($str, 'stringmanip'));
									echo $substring;
								} else{
									$substring = substr($str, 0, strpos($str, 'stringmanip'));
									echo $substring;
								}
								?>
									<br> 
								
								<p>
								<!-- accuracy -->
								</p>				
								<p></p>
								<ul class="actions">
								
								<li><a href="Homepage.php" class="button">Try another</a> </li>
								</ul>
								</form>
								</p>
							</div>

								<div class="column">
								<!-- Input Field -->
								<b> STATEMENT </b><br>
								<p>
								<p align="justify">
								<?php
	
									function string_between_two_string($str, $starting_word, $ending_word){
										$subtring_start = strpos($str, $starting_word);
										//Adding the strating index of the strating word to 
										//its length would give its ending index
										$subtring_start += strlen($starting_word);  
										//Length of our required sub string
										$size = strpos($str, $ending_word, $subtring_start) - $subtring_start;  
										// Return the substring from the index substring_start of length size 
										return substr($str, $subtring_start, $size);  
									}
	  
									$statement = string_between_two_string($str, 'stringmanip', '<label');
	  
									echo $statement;

								
								
								?>
								</p>
								
								</p>
								</div>
								
								
								
							
						</div>
					</section>

				<section>
								<div class="inner">
									<div class="column" style="background-color:#242943;">
										<?php 
											if (strpos($str, "Probability score:") !== false) {
												$pre = "<label>";
												$ind = strpos($str, $pre) + strlen($pre);
												$search = substr($str, $ind);
												echo $search;
											} else {
												echo "<label>NO RELATED LINKS</label>";
											}
										

											
										?>
								
									</div>

									<div class="column" style="background-color:#242943;">
										<label>Disclaimer</label>
										<p align="justify">SVM Fake News Detector is a web-based application that uses machine learning to classify articles and images as factual or fake. 
									SVM Fake News Detector uses support vector machine (SVM) to effectively train and test data sets in order to categorize user inputs 
									based on the degree of accuracy it provides. This application relies on supervised learning (human-coded dataset) and focused web 
									crawling to allow for relative accuracy. It outputs an accuracy score along with several classifications that measure the likelihood 
									that the input has factual or false information.</p>
  									</div>
								</div>
									
							</section>

							<section>
							<div class="inner">
								<footer id="footer">
									
										<ul class="copyright">
										<li>Copyright © 2021 MS Team - Template by:</li>
										<li> <a>PHPJabbers.com</a></li>
										</ul>
									
								</footer>
							</div>
							</section>

		<!-- Scripts -->
			<script src="assets/js/jquery.min.js"></script>
			<script src="assets/bootstrap/js/bootstrap.bundle.min.js"></script>
			<script src="assets/js/jquery.scrolly.min.js"></script>
			<script src="assets/js/jquery.scrollex.min.js"></script>
			<script src="assets/js/browser.min.js"></script>
			<script src="assets/js/breakpoints.min.js"></script>
			<script src="assets/js/util.js"></script>
			<script src="assets/js/main.js"></script>

	</body>
</html>


