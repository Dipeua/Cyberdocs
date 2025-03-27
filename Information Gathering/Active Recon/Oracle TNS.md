# Oracle TNS

Perform a variety of scans to gather information about the Oracle database services and its components.

```sh
./odat.py all -s <FQDN/IP>
```

Log in to the Oracle database.

```sh
sqlplus <user>/<pass>@<FQDN/IP>/<db>
```

Upload a file with Oracle RDBMS.

```sh
./odat.py utlfile -s <FQDN/IP> -d <db> -U <user> -P <pass> --sysdba --putFile C:\\insert\\path file.txt ./file.txt
```
