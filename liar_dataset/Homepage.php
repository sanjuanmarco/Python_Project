<?php 
	require_once "dbcreate.php";
	
?>

<!DOCTYPE HTML>
<html>
	<head>
		<title>SVM</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<link rel="stylesheet" href="assets/bootstrap/css/bootstrap.min.css" />
		<link rel="stylesheet" href="assets/css/main.css?version=1" />
		<noscript><link rel="stylesheet" href="assets/css/noscript.css" /></noscript>

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
			<div id="loader">
			</div>

		<!-- Wrapper -->
			<div id="wrapper">

				<!-- Header -->
				<header id="header" class="alt">
					<a class="logo"><span>Developed by</span> <strong>MS Team</strong></a>
					<nav>
						<a href="#menu">Menu</a>
					</nav>
				</header>

				<!-- Menu -->
				<nav id="menu">
					<ul class="links">
		                <li class="active"> <a href="Homepage.php">Home </a> </li>

		                <li> <a href="About.php">About Us</a> </li>

		                <li> <a href="Members.php">Developers</a> </li>
				
            		</ul>
				</nav>

				<!-- Banner -->
					<section id="banner" class="major">
						<div class="inner">
							<header class="major">
								<h1>SVM Fake News Detector</h1>
							</header>
							<p align="justify">SVM Fake News Detector is a web-based application that uses machine learning to aid users in determining whether articles and images are legitimate or fake. Just simply paste a link of an article or upload an image and this application will analyze its contents to provide users in determining if their inputs are fake or not.
							</p>
						
									<form id="myform" action="Results.php" method="post">
										<label style="color:white;" for="link">Insert valid URL</label>
								<p >
  										<input type="url" id="link" name="link" placeholder="https://sample.net" required>
								</p>				
								
										<ul class="actions">
										<li><input type="submit" name="sub" value="Check"></li>
										</ul>
									</form>
							
								
								
								
								
							
						</div>
					</section>

				<!-- Main -->
					<div id="main">
							<!-- About us -->
							<section>
								<div class="inner">
									
										<!-- Input Field -->
								
								<!-- IMAGE UPLOAD -->
								<p>
									<form id="myimage" action="ResultsImage.php" method="post" enctype="multipart/form-data">
  										<label style="color:white;"> Select image to upload </label>
								<p>
										<input type="file" name="file" id="file" multiple accept="image/x-png,image/jpeg" required>
								
								
										<ul class="actions">	
  										<li><input type="submit" value="upload" name="Submit"><li>
										</ul>
								</p>
									</form>
								</p>

								</div>
							</section>

							

							

				<!-- Footer -->
				<footer id="footer">
					<div class="inner">
						
						<ul class="copyright">
							<li>Copyright © 2021 MS Team - Template by:</li>
							<li> <a>PHPJabbers.com</a></li>
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
  					$("#myform").on("submit", function(){
    					$("#loader").fadeIn();
  					});//submit
				});//document ready
			</script>
			<script>
				$(document).ready(function(){
  					$("#myimage").on("submit", function(){
    					$("#loader").fadeIn();
  					});//submit
				});//document ready
			</script>

	</body>
</html>

