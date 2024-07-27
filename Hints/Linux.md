Convertir les fins de ligne DOS en Unix pour pouvoir les executer

```bash
dos2unix ./EDBID.py

# ou
sed -i 's/\r//' ./EDBID.py
```

Equivalance de `ipconfig /all` sur linux

```c
nmcli dev show
```

CentOS utilise un wrapper toujours activé autour du pare-feu IPTables appelé "firewalld".
Ouvrire un port sur le firewalld (parfeu) de CentOS

```sh
firewall-cmd --zone=public --add-port {port}/tcp
```

Active le X11 sur le serveur distant

```sh
root@metasploitable:/etc/ssh# cat sshd_config | grep -i x11for
X11Forwarding yes

# Connect and start browser on remote server
ssh msfadmin@192.168.45.129 -X /usr/bin/firefox
```