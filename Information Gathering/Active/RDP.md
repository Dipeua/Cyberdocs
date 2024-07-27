Check the security settings of the RDP service.

```c
rdp-sec-check.pl <FQDN/IP>
```

Log in to the RDP server from Linux.

```c
xfreerdp /u:<user> /p:"<password>" /v:<FQDN/IP>
```

Log in to the WinRM server.

```sh
evil-winrm -i <FQDN/IP> -u <user> -p <password>
```

Execute command using the WMI service.

```sh
wmiexec.py <user>:"<password>"@<FQDN/IP> "<system command>"
```