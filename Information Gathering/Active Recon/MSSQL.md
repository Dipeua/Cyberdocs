# MSSQL

Log in to the MSSQL server using Windows authentication.

```sh
mssqlclient.py <user>@<FQDN/IP> -windows-auth
```

Activer `xp_cmdshell`

```sh
EXECUTE sp_configure 'show advanced options',1
EXECUTE sp_configure 'xp_cmdshell',1
RECONFIGURE
EXEC xp_cmdshell whoami;
```
