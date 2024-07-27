**POP3 (Post Office Protocol version 3)** est un protocole utilisé pour télécharger les messages électroniques à partir d'un serveur. Le client de messagerie se connecte au serveur POP3 , s'authentifie, télécharge les nouveaux emails avant (éventuellement) de les supprimer.

POP3 écoute sur le port `110` par défaut.

```sh
telnet <FQDN/IP> 110

USER {username}
+OK frank

PASS {password}
+OK 1 messages (179) octets

STAT
+OK 1 179
+OK nn mm 
# nn =  le nombre de messages électroniques dans la boîte de réception
# mm =  la taille de la boîte de réception en octets

LIST # fourni une liste de nouveaux messages sur le serveur
+OK 1 messages (179) octets
1 179

RETR 1 #  récupére le premier message de la liste
+OK

QUIT
```

---
**IMAP (Internet Message Access Protocol)** plus sophistiqué que POP3 et permet de synchroniser votre courrier électronique sur plusieurs appareils (et clients de messagerie). 

IMAP nécessite que chaque commande soit précédée d'une chaîne aléatoire pour pouvoir suivre la réponse. Nous ajoutons donc `c1`, puis `c2`, et ainsi de suite.
IMAP envoie les informations de connexion en texte clair dans le reseaux.

IMAP écoute sur le port `143` par défaut.

```sh
telnet <FQDN/IP> 110

c1 LOGIN {username} {password}
#...
c1 OK LOGIN Ok.

c2 LIST "" "*" # répertorié les dossiers de courrier
* LIST (\HasNoChildren) "." "INBOX.Trash"
* LIST (\HasNoChildren) "." "INBOX.Drafts"
* LIST (\HasNoChildren) "." "INBOX.Templates"
* LIST (\HasNoChildren) "." "INBOX.Sent"
* LIST (\Unmarked \HasChildren) "." "INBOX"
c2 OK LIST completed
c3 EXAMINE INBOX # vérifier les nouveaux messages dans la boîte de réception
* FLAGS (\Draft \Answered \Flagged \Deleted \Seen \Recent)
* OK [PERMANENTFLAGS ()] No permanent flags permitted
* 0 EXISTS
* 0 RECENT
* OK [UIDVALIDITY 631694851] Ok
* OK [MYRIGHTS "acdilrsw"] ACL
c3 OK [READ-ONLY] Ok

c4 LOGOUT
```

---
Connect to the POP3s service.

```sh
openssl s_client -connect <FQDN/IP>:pop3s
```

Log in to the IMAPS service using cURL.

```sh
curl -k 'imaps://<FQDN/IP>' --user <user>:<password>
```

Connect to the IMAPS service.

```sh
openssl s_client -connect <FQDN/IP>:imaps
```
