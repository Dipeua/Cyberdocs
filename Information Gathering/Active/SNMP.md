Le SNMP (Simple Network Management Protocol) est un protocole de gestion de réseau qui permet de superviser et de gérer les équipements réseau, tels que les routeurs, les commutateurs, les serveurs, etc. 

Il permet de collecter des informations sur l'état et les performances du réseau, de configurer à distance les équipements, de détecter et de résoudre les problèmes de manière proactive.

**Les chaînes de communauté** par défaut du fabricant sont `manager`, `public`et `private`.

Dans les versions SNMP 1 et 2c, l'accès est contrôlé à l'aide d'une chaîne de communauté en texte brut, et si nous connaissons le nom, nous pouvons y accéder.

Le serveur SMTP écoute sur le port 161 par défaut.

---
Enumerate which `community` is enabled on the server

```sh
nmap -sU -p 161 --script=snmp-brute <IP>
```


Bruteforcing community strings of the SNMP service.

```sh
onesixtyone -c dict.txt <FQDN/IP>
```

Querying OIDs using snmpwalk.

```sh
snmpwalk -v 2c -c <community string> <FQDN/IP>
```

Bruteforcing SNMP service OIDs.

```c
braa <community string>@<FQDN/IP>:.1.*
```

---
Afficher les programmes installer ou disponible sur la machine

```sh
snmpwalk -v 2c -c <community string> <FQDN/IP> hrSWInstalledName
```

---
Enumerating the entire MIB Tree

```sh
snmpwalk -c public -v1 -t 10 <FQDN/IP> 
```

Enumerating Windows users

```sh
snmpwalk -c public -v1 <FQDN/IP> 1.3.6.1.4.1.77.1.2.25
```

Enumerating running windows processes

```sh
snmpwalk -c public -v1 <FQDN/IP> 1.3.6.1.2.1.25.4.2.1.2
```

Enumerating open TCP ports

```sh
snmpwalk -c public -v1 <FQDN/IP> 1.3.6.1.2.1.6.13.1.3
```

Enumerating installed software

```sh
snmpwalk -c public -v1 <FQDN/IP> 1.3.6.1.2.1.25.3.1.2
```

Rechercher ceci

```
snmpwalk -v 2c -c public 10.129.42.253 1.3.6.1.2.1.1.5.0
```