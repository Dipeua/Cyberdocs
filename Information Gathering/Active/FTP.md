Interact with the FTP service on the target.

```sh
ftp <FQDN/IP>
```

Interact with the FTP service on the target.

```
nc -nv <FQDN/IP> 21
```


Interact with the FTP service on the target

```
telnet <FQDN/IP> 21
```


Interact with the FTP service on the target using encrypted connection.

```SH
openssl s_client -connect <FQDN/IP>:21 -starttls ftp
```

Download all available files on the target FTP server.

```SH
wget -m --no-passive ftp://anonymous:anonymous@<target>
```