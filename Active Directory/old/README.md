Exigences du privilège d'attaque :

-   [[Active Directory/old/Enumaration/Enumeration#kerbrute|kerbrute]] - Aucun accès au domaine requis
-   [[Mimikatz#Pass The Ticket|Pass The Ticket]]- Accès en tant qu'utilisateur au domaine requis
-   [[Kerberoasting]] - Accès en tant qu'utilisateur requis
-   [[AS-REP Roasting]] - Accès en tant qu'utilisateur requis  

-   Ticket Argent - Hachage de service requis

-   Golden Ticket - Compromis de domaine complet (administrateur de domaine) requis
-   Clé squelette - Compromis de domaine complet (administrateur de domaine) requis

---

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