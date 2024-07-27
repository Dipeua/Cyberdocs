#kerbrute

Enumérer les utilisateurs valides en abusant de la pré-authentification Kerberos.

```sh
kerbrute userenum names.txt --dc 192.168.75.152 -d homelab.local
```

#BloodHound

#DNS 
Transfert de zone DNS pour lister tous les enregistrements :

```c
nslookup.exe
server <dc-ip>
ls -d domain.local
```