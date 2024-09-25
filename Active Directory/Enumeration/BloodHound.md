Récupérer du butin a distance avec BloudHound

```sh
bloodHound-python -c All -u Administrator -p 'Password' -d pwnlab.local -ns 10.10.x.x
```

Récupérer du butin avec SharpHound

```sh
. .\SharpHound.ps1
Invoke-Bloodhound -CollectionMethod All -Domain CONTROLLER.local -ZipFileName loot.zip
```


