## LDAP avec powerview

Cree une session sur la machine compromise pour l'effectuer a distance

```c
$session = New-PSSession -ComputerName 192.168.1.1 -Credential username
Enter-PSSesion $session
```

Obtenir la liste des controleurs du domaine du reseau:

```c
nltest /dclist:pwnlab.local
```