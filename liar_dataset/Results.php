<!DOCTYPE HTML>
<html>
	<head>
		<title>Results</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<link rel="stylesheet" href="assets/bootstrap/css/bootstrap.min.css" />
		<link rel="stylesheet" href="assets/css/main.css?version=1" />
		<noscript><link rel="stylesheet" href="assets/css/noscript.css" /></noscript>
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
								
								<!-- Input Field -->
								<p>
								RESULTS<br>
								<?php 
								
									$url = $_POST["link"];
									echo $url; 
								?>
								
								<p align="justify">
								<?php	

									echo shell_exec("py -3.9 crawl.py $url 2>&1");

								?>	
								</p>				
								<p></p>
								<ul class="actions">
								
								<li><a href="Homepage.php" class="button next">Try another</a></li>
								</ul>
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

	</body>
</html>


