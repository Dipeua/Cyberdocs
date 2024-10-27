Le SMTP (Simple Mail Transfer Protocol ) est utilisé pour communiquer avec un serveur de messagerie pour envoyé des e-mails. il écoute sur le port `25` par défaut.

SMTP utilise du texte clair, où toutes les commandes sont envoyées sans cryptage

Nous utiliserons `telnet` pour nous connecter à un serveur SMTP et agir comme un client de messagerie

Une fois connectés, nous émettons:
- `helo hostname`puis commençons à taper notre email.
- Après `helo`, nous émettons `mail from:`, `rcpt to:`pour indiquer l'expéditeur et le destinataire.
- Lorsque nous envoyons notre message électronique, nous émettons la commande `data`et tapons notre message. 
- Nous émettons `<CR><LF>.<CR><LF>`(ou `Enter . Enter`). 

Le serveur SMTP met désormais le message en file d'attente.

---

```c
telnet <FQDN/IP> 25
Trying MACHINE_IP...
Connected to MACHINE_IP.
Escape character is '^]'.
220 bento.localdomain ESMTP Postfix (Ubuntu)

HELO telnet
250 bento.localdomain

MAIL FROM: <send@gmail.com>
250 2.1.0 Ok

RCPT TO: <recipient@gmail.com>
250 2.1.5 Ok

DATA
354 End data with .

From: send@gmail.com
To: recipient@gmail.com
SUBJECT: Sending email with Telnet

Hello Frank,
I am just writing to say hi!             
.

250 2.0.0 Ok: queued as C3E7F45F06
QUIT

221 2.0.0 Bye
Connection closed by foreign host.
```

Enumerate which options `verbs` are enabled on the mail server

```sh
nmap --script=smtp-commands -p 25 <IP>
```

Enumerer les utilisateur manuellement

```sh
RCPT TO: <user@domain.com>
EXPN <username>
VRFY <username.
```

Enumaration users

```sh
smtp-user-enum -M VRFY -U usernames.txt -t 192.168.45.130
```

```
use auxiliary/scanner/smtp/smtp_enum
```

Script to automate enumaration `vrfy.py`

```python
import socket
import sys

if len(sys.argv) != 2:
	print "Usage: vrfy.py <username>"
	sys.exit(0)
	
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = s.connect(('192.168.45.130', 25))

banner = s.recv(1024)
print banner

s.send('VRFY ' + sys.argv[1] + '\r\n')
result = s.recv(1024)
print result

s.close()
```

