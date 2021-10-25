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
                                <?php 
								
									$statement = $_POST["link"];
								?>

								
								<p align="justify">
								<?php	

									$res = exec("py -3.9 statement.py $statement 2>&1", $output, $var);
									$str = implode(" ",$output);
									
									$substring = substr($str, 0, strpos($str, 'stringmanip'));
									echo $substring;


								?>	
								</p>				
								<p></p>
								<ul class="actions">
								
								<li><a href="Homepage.php" class="button">Try another</a></li>
								</ul>
								</p>
								</div>

								<div class="column">

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
								</div>
								
								
								
							
						</div>
					</section>

				<section>
								<div class="inner">
									<div class="column" style="background-color:#242943;">
										
										<?php 
								
											$pre = "<label>";
											$ind = strpos($str, $pre) + strlen($pre);
											$search = substr($str, $ind);
											echo $search;
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


