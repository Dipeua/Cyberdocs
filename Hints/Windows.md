Afficher une boite de dialogue

```c
mshta javascript:alert("Tu t'es fait hacker");close()
```

Démarrer un cmd en tant que notre nouvelle administrateur utiliser pour les comptes a haut privilege (POWERSHELL)

```c
Start-Process powershell 'Start-Process cmd.exe -Verb RunAs' -Credential {user}
```

Demarrer le cmd en tant que autre utilisateur du systeme (CMD)

```c
net user {username} /active:yes
runas /user:{username} cmd.exe
```

Cree et ajouter un utilisateur a un groupe admin et a WinRm

```c
net user USERNAME PASSWORD /add
net localgroup Administrators USERNAME /add
net localgroup "Remote Management Users" USERNAME /add
```


Ouvrir un port dans le pare-feu pour permettre l'établissement de la connexion directe(Proxy SOCKS direct):

```c
netsh advfirewall firewall add rule name="NAME" dir=in action=allow protocol=tcp localport=PORT
```


```c
rdesktop ... -g 1024x768 -x 0x80
```

```sh
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser
```