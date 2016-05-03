<!DOCTYPE html>
 <html>
 <head>
 	<title>ECG Signal Analysis</title>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">

<!-- Optional theme -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap-theme.min.css" integrity="sha384-fLW2N01lMqjakBkx3l/M9EahuwpSfeNvV63J5ezn3uZzapT0u7EYsXMjQV+0En5r" crossorigin="anonymous">

<!-- Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js" integrity="sha384-0mSbJDEHialfmuBBQP6A4Qrprq5OVfW37PRR3j5ELqxss1yVqOtnepnHVP9aJ7xS" crossorigin="anonymous"></script>
   	
<script type="text/javascript">
     function myFunction() {
      data = <?php
      $str = file_get_contents('./jobs.json', true);
      echo $str;
      ?>
            document.getElementById('show').innerHTML +="<ul><li>Heart Rate:"+ data[0]["Heart Rate"]+"</li><li>:Cv"+ data[0]["cv"]+"</li><li>Mean:"+ data[0]["mean"]+"</li><li>Rms_Diff:"+ data[0]["rms_diff"]+"</li><li>Std_Dev:"+ data[0]["std_dev"]+"</li><li>Std_Dev_Diff:"+ data[0]["std_dev_diff"]+"</li><li>Variance:"+ data[0]["variance"]+"</li></ul>";
    }
 </script>
 </head>
 <body style="background-color: #9163B8">
 <center><h1 style="position: absolute;left: 630px;color: #371FD5">ECG(IOP)</h1></center> 
  <div style="position: absolute;
    left: 600px;
    top: 100px; color: #27B567">
    <h1>Upload File</h1><br>
  </div>
  <form method="POST" enctype="multipart/form-data" action="https://mecg.herokuapp.com/analyse">
      <div class = "input-group" style="position: absolute;
    left: 500px;
    top: 180px">
      <input type = "file" name="file" id = "inputfile"></br>      
      <button type = "submit" style="position: absolute;left: 400px;top: 1px" class = "btn btn-primary">Submit</button>
      </div>  
  </form>
  
  <div style="position: absolute;
    left: 600px;
    top: 220px; color: #27B567">
    <h1>Find If Cancer</h1><br>
  </div>
  <form method="post" action="https://indorp.herokuapp.com/upload">
      <div class = "input-group" style="position: absolute;
    left: 500px;
    top: 300px">
      <input type = "file"   id = "inputfile"></br>      
      <button type = "submit" style="position: absolute;left: 400px;top: 1px" class = "btn btn-primary">Submit</button>
      </div>  
  </form>      
 <div id="show" style="position: absolute; left: 320px; top: 360px; background-color: #FCFAFA; width: 900px; height: 250px; overflow: scroll">
 </div>
 </body>
 </html>