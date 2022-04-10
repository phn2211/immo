<?php

$myfile = fopen("flats.txt", "r") or die("Unable to open file!");
$mtime = filemtime('flats.txt');

?>
<!DOCTYPE html>
<html lang="de">
<head>
  <title>Anwesenheitsübersicht</title>
  <meta charset="utf-8">
  <meta http-equiv="refresh" content="300">	
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css">
  <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/js/bootstrap.bundle.min.js"></script>
  <style>
  .fakeimg {
    height: 200px;
    background: #aaa;
  }
  .alert {
    position: relative;
    padding: 0.75rem 1.25rem;
    margin-bottom: 1rem;
    border: 1px solid transparent;
    border-radius: 0.25rem;
  }
  .alert-IN, .alert-BreakIN {
    color: #155724;
    background-color: #d4edda;
    border-color: #c3e6cb;
  }
  .alert-BreakOUT {
    color: #1b1e21;
    background-color: #d6d8d9;
    border-color: #c6c8ca;
  }
  .alert-OUT {
    color: #721c24;
    background-color: #f8d7da;
    border-color: #f5c6cb;
  }
	  
  </style>
</head>
<body>
<!--
<div class="jumbotron text-center" style="margin-bottom:0">
  <h1>My First Bootstrap 4 Page</h1>
  <p>Resize this responsive page to see the effect!</p> 
</div>
-->
<nav class="navbar navbar-expand-sm bg-dark navbar-dark">
  <a class="navbar-brand" href="#">ebay Kleinanzeigen 1-Zimmer-Wohnungen <?php echo date ("d.m.Y H:i:s.", $mtime); ?></a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
    <span class="navbar-toggler-icon"></span>
  </button>
	<!--
  <div class="collapse navbar-collapse" id="collapsibleNavbar">
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" href="#">Link</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Link</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Link</a>
      </li>    
    </ul>
  </div>
  -->
</nav>

<div class="container" style="margin-top:30px">
  <div class="row">
	 <div class="col-md-12 col-xs-12">
<?php
$myfile = fopen("flats.txt", "r") or die("Unable to open file!");
echo '<table class="table table-responsive">';
echo '<thead><tr id="headline"><td>id</td><td>Datum</td><td>Ort</td><td>Preis</td><td>Titel</td><td>Beschreibung</td><td>Link</td></tr></thead>';  
while(!feof($myfile)) {
  $line = explode(';',fgets($myfile));
  $id = $line[0];
  $time_of_creation = $line[1];	
  $place = $line[2];
  $price = $line[3];
  $title = $line[4];
  $desc = $line[5];
  $link = $line[6];
  echo '<tr>';
  echo '<td>'.$id.'</td>';
  echo '<td>'.$time_of_creation.'</td>';
  echo '<td>'.$place.'</td>';
  echo '<td>'.$price.'</td>';
  echo '<td>'.$title.'</td>';
  echo '<td>'.$desc.'</td>';
  echo '<td>'.$link.'</td>';
  echo "</tr>"; 
	  
}

echo "</table>";
fclose($myfile);	  
?>
	</div>
  </div>
</div>
<!--
<div class="jumbotron text-center" style="margin-bottom:0">
  <p>Footer</p>
</div>
-->
<script>
/*	
$(document).ready(function() {
	$('tr').each(function() {
    	var ids = $('[id=' + this.id + ']');
   		if (ids.length > 1) {
          ids.not(':last').remove();
        }
	});
});	
*/
</script>

</body>
</html>