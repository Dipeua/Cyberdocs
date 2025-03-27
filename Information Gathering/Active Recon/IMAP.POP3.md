# IMAP/POP3

## POP3 (Post Office Protocol version 3)

Est un protocole utilisé pour télécharger les messages électroniques à partir d'un serveur. Le client de messagerie se connecte au serveur POP3 , s'authentifie, télécharge les nouveaux emails avant (éventuellement) de les supprimer.

POP3 écoute sur le port `110` par défaut.

Certaines commandes POP3 courantes sont :

- `USER <username>` identifie l'utilisateur
- `PASS <password>` fournit le mot de passe de l'utilisateur
- `STAT` demande le nombre de messages et la taille totale
- `LIST` répertorie tous les messages sur le serveur et leurs tailles
- `RETR <message_number>` récupère le message spécifié
- `DELE 1` : marque un message pour suppression

```sh
telnet <FQDN/IP> 110

AUTH
+OK
PLAIN
.

USER linda
+OK

PASS Pa$$123
+OK Logged in.

STAT
+OK 4 2216
#+OK nn mm 
# nn =  le nombre de messages électroniques dans la boîte de réception
# mm =  la taille de la boîte de réception en octets

LIST
+OK 4 messages:
1 690
2 589
3 483
4 454
.

RETR 4
+OK 454 octets
Return-path: <user@client.thm>
Envelope-to: linda@server.thm
Delivery-date: Thu, 12 Sep 2024 20:12:42 +0000
Received: from [10.11.81.126] (helo=client.thm)
        by example.thm with smtp (Exim 4.95)
        (envelope-from <user@client.thm>)
        id 1soqAj-0007li-39
        for linda@server.thm;
        Thu, 12 Sep 2024 20:12:42 +0000
From: user@client.thm
To: linda@server.thm
Subject: Your Flag

Hello!
Here's your flag:
THM{TELNET_RETR_EMAIL}
Enjoy your journey!
.


QUIT
+OK Logging out.
```

## IMAP (Internet Message Access Protocol) 

Plus sophistiqué que POP3 et permet de synchroniser votre courrier électronique sur plusieurs appareils (et clients de messagerie). 

IMAP nécessite que chaque commande soit précédée d'une chaîne aléatoire pour pouvoir suivre la réponse. Nous ajoutons donc `c1`, puis `c2`, et ainsi de suite.
IMAP envoie les informations de connexion en texte clair dans le reseaux.

IMAP écoute sur le port `143` par défaut.

Certaines commandes IMAP courantes sont :

- `LOGIN <username> <password>` authentifie l'utilisateur
- `SELECT <mailbox>` sélectionne le dossier de boîte aux lettres avec lequel travailler
- `FETCH <mail_number> <data_item_name>` Exemple fetch 3 body[] pour récupérer le message numéro 3, l'en-tête et le corps.
- `MOVE <sequence_set> <mailbox>` déplace les messages spécifiés vers une autre boîte aux lettres
- `COPY <sequence_set> <data_item_name>` copie les messages spécifiés dans une autre boîte aux lettres
- `LOGOUT` se déconnecte


```sh
telnet <FQDN/IP> 143

c1 LOGIN linda Pa$$123
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
