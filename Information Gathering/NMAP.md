[[Information Gathering/README|Retour]]


> [!NOTE] Basic Scan

Analyse réseau ICMP (Sweeping)

```sh
nmap -sn 192.168.45.0/24
#nmap -sn 192.168.45.1-254
```

Analyses TCP (**`scan connecter`**) **`SYN | SYN-ACK | ACK`**

```sh
nmap <FQDN/IP> -sT
```

```sh
nc -v -z -w 1 <FQDN/IP> 80
```

Analyses UDP (**`sans état`**)

```sh
sudo nmap <FQDN/IP> -sU --top-ports 20 
sudo nmap <FQDN/IP> -sU -F -v --top-ports 20
```

```sh
nc -u -v -z -w 1 <FQDN/IP> 80
```

SYN Scan (**`scan furtif`**) peut contourner les anciens IDS **`SYN | SYN-ACK`**

```sh
sudo nmap <FQDN/IP> -sS
```

> [!NOTE] Advanced Scan
> D'autre types d'analyse furtifs utiliser pour contourner certaine pare-feu.

Analyse TCP NULL **`<none>`**

```sh
sudo nmap <FQDN/IP> -sN
```

Analyse TCP FIN **`FIN`**

```sh
sudo nmap <FQDN/IP> -sF
```

Analyse de Noël TCP ou Xmas **`FIN, PSH, URG`**

```sh
sudo nmap <FQDN/IP> -sX
```


> [!NOTE] Identify Firewall rules
> Les analyses `ACK` et `Window` exposent les règles du pare-feu, et non les services.


Analyse TCP ACK **`ACK`**
Ce type d'analyse peut être utile s'il existe un pare-feu devant la cible et est plus adapté pour découvrir les ensembles de règles et la configuration du pare-feu.
Le resultat de ce scan affiche les ports qui ne sont pas bloquer par le pare-feu

```sh
sudo nmap <FQDN/IP> -sA
```

Analyse Window **`ACK`**
Le resultat de ce scan affiche les ports qui ne sont pas bloquer par le pare-feu. Les ports peuvent afficher `closed` mais elles sont en realiter ouvert. 

```sh
sudo nmap <FQDN/IP> -sW
```

Analyse personnalisée

```sh
sudo nmap --scanflags RSTSYNFIN
```

---
# NSE
Le NSE est particulièrement utile pour la reconnaissance, l'étendue de la bibliothèque de scripts. Certaines catégories utiles incluent :

- `safe`:- N'affectera pas la cible
- `intrusive`:- Pas sûr : susceptible d'affecter la cible  
- `vuln`:- Rechercher les vulnérabilités
- `exploit`:- Tentative d'exploiter une vulnérabilité
- `auth`:- Tentative de contourner l'authentification pour les services en cours d'exécution 
- `brute`:- Tentative de force brute des informations d'identification pour l'exécution des services
- `discovery`:- Tentative d'interroger les services en cours d'exécution pour obtenir des informations supplémentaires sur le réseau 

Une liste plus exhaustive peut être trouvée [ici](https://nmap.org/book/nse-usage.html) 

Pour exécuter un script spécifique :

```sh
sudo nmap <FQDN/IP> --script=<script-name>
sudo nmap <FQDN/IP> --script=<script-name>,<script-name>
#sudo nmap 192.168.45.130 --script=vuln
```

Certains scripts nécessitent des arguments

```sh
nmap -p 80 --script <script-name> --script-args <script-name>.<arg-name>='<value>'

#nmap -p 80 --script http-put --script-args http-put.url='/dav/shell.php',http-put.file='./shell.php'
```

Une liste complète des scripts et de leurs arguments correspondants (ainsi que des exemples de cas d'utilisation) peuvent être trouvés [ici](https://nmap.org/nsedoc/) 

Afficher le menu d'aide d'un script particulier

```sh
nmap --script-help <script-name>
```

---
# Firewall evasion 

Il existe une variété d'autres commutateurs utiles pour contourner le pare-feu disponible [ici](https://nmap.org/book/man-bypass-firewalls-ids.html) 
- `-f`, `-ff` utilisé pour fragmenter les paquets (les diviser en morceaux plus petits), ce qui rend moins probable que les paquets soient détectés par un pare-feu ou un IDS.

- `--mtu <number>` agit comme `-f` mais offre plus de contrôle sur la taille des paquets. Accepte une taille maximale d'unité de transmission à utiliser pour les paquets envoyés qui doit être un multiple de 8.

- `--scan-delay <time>ms` utilisé pour ajouter un délai entre les paquets envoyés. Ceci est très utile si le réseau est instable, mais également pour éviter les déclencheurs de pare-feu/ IDS temporels qui pourraient être en place.

- `--badsum` ceci est utilisé pour générer une somme de contrôle invalide pour les paquets. Toute véritable pile TCP /IP abandonnerait ce paquet, cependant, les pare-feu peuvent potentiellement répondre automatiquement, sans prendre la peine de vérifier la somme de contrôle du paquet. A ce titre, ce commutateur peut être utilisé pour déterminer la présence d'un pare-feu/ IDS .

- `--data-length NUM` augmenter la taille de vos paquets pour les rendre inoffensifs


Spoofing IP Source

```sh
sudo nmap -D 10.10.0.1,10.10.0.2,RND,RND,<MY-IP> <FQDN/IP>
```


> [!NOTE] Idle scanning
> L'analyse zombie, nécessite un système inactif connecté au réseau avec lequel vous pouvez communiquer

Analyse zombie

The Idle scan is a stealth technique that involves the presence of a zombie (host that is not sending or receiving any packets thus) in the target network.

Find a zombie that assigns IP ID both incrementally and globally

```sh
sudo nmap -O -v -n 192.168.45.0/24
```

```
use auxiliary/scanner/ip/ipidseq
```

if **`IP ID Sequence Generation: Incremental`**, thus a good zombie


```sh
sudo nmap -Pn -sI zombie:port <FQDN/IP> -v -p 55
```

We are able to scan the target host without sending a single packet from our orinal IP adress

---

Contrôler le débit des paquets: garantit que votre scanner n'envoie pas plus de dix paquets par seconde

```
nmap <FQDN/IP> --min-rate=10
```

Contrôler la parallélisation des sondages: Nmap à maintien au moins 512 sondes en parallèle ; ces 512 sondes sont liées à la découverte d'hôtes et aux ports ouverts.

```
nmap <FQDN/IP> --min-parallelism=512
```

