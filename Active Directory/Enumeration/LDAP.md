# LDAP (Lightweight Directory Access Protocol)

Dans l'authentification LDAP, l'application vérifie directement les identifients de l'utilisateur. 

L'application dispose d'une paire d'informations d'identification AD qu'elle peut utiliser d'abord pour interroger LDAP, puis vérifier les informations d'identification de l'utilisateur AD.


## Anonymous Bind

Interroger la racine du serveur LDAP pour obtenir ses informations de base en effectuent une liaison anonyme.

```sh
ldapsearch -x -H ldap://10.211.11.10 -s base
```

Rechercher tous les objets de type "person" dans le domaine LDAP `dc=home,dc=local` et liste d'utilisateurs définis dans le domaine `home.local`

```sh
ldapsearch -x -H ldap://10.211.11.10 -b "dc=home,dc=local" "(objectClass=person)"
```

## Pass-back Attack

Attaque menée contre les mécanismes d'authentification LDAP apres avoir obtenu un premier accès au réseau interne

Peuvent être effectuées lorsque nous accédons à la configuration d'un appareil où les paramètres LDAP sont spécifiés


## LDAP + PowerView

Cree une session sur la machine compromise pour l'effectuer a distance

```sh
$session = New-PSSession -ComputerName 192.168.1.1 -Credential username
Enter-PSSesion $session
```

Obtenir la liste des controleurs du domaine du reseau:

```sh
nltest /dclist:pwnlab.local
```