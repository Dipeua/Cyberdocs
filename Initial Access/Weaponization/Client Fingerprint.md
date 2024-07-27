Client fingerprint

```sh
wget https://github.com/Valve/fingerprintjs2/archive/master.zip
```

```sh
cd fingerprintjs2
```

Creer un fichier `fingerprint2.html`

```html
<!DOCTYPE html>
<html>
<head>
	<title>Fingerprintjs2 test</title>
</head>
<body>
	<h1>Fingerprintjs2</h1>

	<p>Your browser fingerprint : <strong id="fp"></strong></p>
	<p><code id="time"></code></p>
	<p><code id="details"></code></p>

	<script src="fingerprintjs2.js"></script>
	<script type="text/javascript">
		var d1 = new Date();
		var options = {};
		Fingerprint2.get(options, function (components){
			var values = components.map(function (component){ return component.value })
			var murmur = Fingerprint2.x64hash128(values.join(''), 31)
			var d2 = new Date();
			var timeString = "Time took to calculate the fingerprint: " + (d2 - d1) + "ms";
			var details = "<strong>Detailed information: </strong><br/>";
			if(typeof window.console !== "undefined"){
				for(var index in components){
					var obj = components[index];
					var value = obj.value;
					if(value !== null){
						var line = obj.key + " = " + value.toString().substr(0, 150);
						details += line + "<br/>";
					}
				}
			}
			document.querySelector("#details").innerHTML = details;
			document.querySelector("#fp").innerHTML = murmur;
			document.querySelector("#time").innerHTML = timeString;
		});
	</script>
</body>
</html>
```

Coller un `User-Agent` sur ce site https://developers.whatismybrowser.com pour avoir plus d'informations.

Creer un fichier `fingerprint2server.html`

```html
<!DOCTYPE html>
<html>
<head>
	<title>Blank page</title>
</head>
<body>
	<h1>You have been give the finger!</h1>
	<script src="fingerprintjs2.js"></script>
	<script type="text/javascript">
		var d1 = new Date();
		var options = {};
		Fingerprint2.get(options, function (components){
			var values = components.map(function (component){ return component.value })
			var murmur = Fingerprint2.x64hash128(values.join(''), 31)
			var clientftp = "Client browser fingerprint: " + murmur + "\n\n";
			var d2 = new Date();
			var timeString = "Time took to calculate the fingerprint: " + (d2 - d1) + "ms\n\n";
			var details = "<strong>Detailed information: </strong><br/>";
			if(typeof window.console !== "undefined"){
				for(var index in components){
					var obj = components[index];
					var value = obj.value;
					if(value !== null){
						var line = obj.key + " = " + value.toString().substr(0, 150);
						details += line + "<br/>";
					}
				}
			}
			var xmlhttp = new XMLHttpRequest();
			xmlhttp.open("POST", "/fp/js.php");
			xmlhttp.setRequestHeader("Content-Type", "application/txt");
			xmlhttp.send(clientftp + timeString + details);
		});
	</script>
</body>
</html>
```

Creer un fichier `js.php`

```php
<?php
$data = "Client IP Address: " . $_SERVER['REMOTE_ADDR']. "\n";
$data .= file_get_contents('php://input');
$data .= "---------------------------------\n\n";
file_put_contents('/var/www/html/fp/fingerprint.txt', print_r($data, true), FILE_APPEND | LOCK_EX);
?>
```

```sh
sudo chown -R www-data:www-data fp
```

```sh
cat fingerprint2server.html # viste this page on client browser
```