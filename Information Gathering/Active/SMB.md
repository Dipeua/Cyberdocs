Le SMB (Server Message Block) écoute par défaut sur les ports `139,445`

---

```
nbtscan -r 192.168.45.0/24
```

```
nmap -p 139,445 --script=smb-os-discovery <FQDN/IP>
```


---

Null session authentication on SMB.

```sh
smbclient -L //<FQDN/IP> -N
```

Connect to a specific SMB share.

```sh
smbclient //<FQDN/IP>/<share>
```

Enumerating SMB shares.

```
smbmap -H <FQDN/IP>
```

Interaction with the target using RPC.

```sh
rpcclient -U "" <FQDN/IP>
```

---

Username enumeration using Impacket scripts.

```
samrdump.py <FQDN/IP>
```

Enumerating SMB shares using null session authentication.

```
crackmapexec smb <FQDN/IP> --shares -u '' -p ''
```

SMB enumeration using enum4linux.

```
enum4linux-ng.py <FQDN/IP> -A
```

---
# Exploitation

**Samba Symlink Directory Traversal.** allow attacker to create a symbolic link to the `root /` partition from writeable share ultimately allowing for read access to the entire file systeme outsite of the share directory.

Lors que un partage a les permissions d'ecriture. et que le parametre `widelinks` definir sur `yes` soit present dans le fichier `smb.conf`

```
use auxiliary/admin/smb/samba_symlink_traversal
```

Apres  cela acceder au partge avec smbclient et on poura voir un nouveau dossier cree

---
Configuration for Windows pivot

```sh
sudo nano /etc/samba/smb.conf
...
min protocol = SMB2
```

```sh
sudo /etc/init.d/smbd restart
```