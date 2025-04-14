# Bloodhound

**Bloodhound-Python**

Récupérer du butin a distance

```sh
bloodhound-python -c All -u Administrator -p 'Password' -d CONTROLLER.local -ns 10.10.x.x

bloodhound-python -c All -u michael -p 'NewPassword123' -dc administrator.htb -d administrator.htb -ns 10.10.11.42
```

**SharpHound**

Récupérer du butin en local

```sh
. .\SharpHound.ps1
Invoke-Bloodhound -CollectionMethod All -Domain CONTROLLER.local -ZipFileName loot.zip
```

Run the SharpHound C# ingestor

```sh
.\SharpHound.exe -c all --zipfilename CONTROLLER_bloodhound
```

