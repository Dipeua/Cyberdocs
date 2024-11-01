**Bloodhound-Python**

Récupérer du butin a distance

```sh
bloodhound-python -dc <DC> -gc <GC> -d <DOMAIN -c All -u <user>
```

```sh
bloodhound-python -c All -u Administrator -p 'Password' -d CONTROLLER.local -ns 10.10.x.x
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

