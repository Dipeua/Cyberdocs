# MySQL

Login to the MySQL server.

```sh
mysql -u <user> -p<password> -h <FQDN/IP>
```

Énumération de MySQL

```sh
nmap --script=mysql-enum <FQDN/IP>
```

```sh
use auxiliary/admin/mysql/mysql_sql
```

Exploiter MySQL

Extraire des hachages de mots de passe 

```sh
use auxiliary/scanner/mysql/mysql_schemadump
```

```sh
use auxiliary/scanner/mysql/mysql_hashdump
```

