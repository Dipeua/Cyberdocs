# WHOIS and DNS 

Assign target to an environment variable.

```sh
export TARGET="domain.tld"
export PORT=443
```

## DNS Enumeration

WHOIS lookup for the target.

```sh
whois $TARGET
```

Reverse Lookup Brute Force

```sh
for ip in $(seq 50 100); do host X.X.X.$ip; done | grep -v "not found"
```

Identify the ANY record for the target IP address.

```sh
nslookup -query=ANY $TARGET
nslookup -query=PTR <IP>
```

Identify the record for the target IP address and [DNS Zone Transfert](../../Programming/dns-axfr.sh)

```sh
dig $TARGET @<nameserver>
dig any $TARGET @<nameserver>
dig -x <IP> @<nameserver/IP>

# AXFR request to the specific nameserver. 
dig axfr $TARGET @<nameserver>
dig axfr $TARGET @NSZTM1.DIGI.NINJA | cut -d " " -f3
```

## Passive Subdomain Enumeration

- https://www.virustotal.com/gui/home/search

**Project Sonar**

est un projet de recherche en sécurité qui mène des enquêtes sur Internet auprès de divers services et protocoles afin de recueillir des informations sur l'exposition aux vulnérabilités à l'échelle mondiale. Les informations collectées sont rendues publiques pour faciliter la recherche en sécurité.

```sh 
# Tous les sous-domaines pour un domaine donné.
curl -s https://sonar.omnisint.io/subdomains/$TARGET | jq -r '.[]' | sort -u 
    
# Tous les TLD trouvés pour un domaine donné.
curl -s https://sonar.omnisint.io/tlds/$TARGET | jq -r '.[]' | sort -u      

# Tous les résultats sur tous les TLD pour un domaine donné.
curl -s https://sonar.omnisint.io/all/$TARGET | jq -r '.[]' | sort -u       

# Reverse DNS lookup on IP address
curl -s https://sonar.omnisint.io/reverse/{ip}        

# Reverse DNS lookup of a CIDR range
curl -s https://sonar.omnisint.io/reverse/{ip}/{mask} 
```

**Certificate Transparency.**

Les certificats SSL/TLS constituent une autre source d'informations intéressante pour extraire des sous-domaines. La principale raison est la transparence des certificats (CT), un projet qui exige que chaque certificat SSL/TLS émis par une autorité de certification (AC) soit publié dans un journal accessible au public.

- https://search.censys.io/
- https://crt.sh

```sh
# Transparence des certificats.
curl -s "https://crt.sh/?q=${TARGET}&output=json" | jq -r '.[] | "\(.name_value)\n\(.common_name)"' | sort -u > "${TARGET}_crt.sh.txt"
```

```sh
openssl s_client -ign_eof 2>/dev/null <<<$'HEAD / HTTP/1.0\r\n\r' -connect "${TARGET}:${PORT}" | openssl x509 -noout -text -in - | grep 'DNS' | sed -e 's|DNS:|\n|g' -e 's|^\*.*||g' | tr -d ',' | sort -u
```

## Automating Passive Subdomain Enumeration

**theHarvester**

```sh
# Collecter des informations à partir de ces sources.
cat sources.txt | while read source; do theHarvester -d "${TARGET}" -b $source -f "${source}_${TARGET}";done

# Extraire tous les sous-domaines trouvés et les trier
cat *.json | jq -r '.hosts[]' 2>/dev/null | cut -d':' -f 1 | sort -u > "${TARGET}_theHarvester.txt"

# Fusionner tous les fichiers
cat $TARGET_*.txt | sort -u > $TARGET_subdomains_passive.txt
```

**Other**

```sh
dnsrecon -d $TARGET -t axfr -a -w -g
dnsenum --dnsserver <nameserver> --enum -p 0 -s 0 -o found_subdomains.txt -f ~/subdomains.list $TARGET

fierce -dns $TARGET
```

La recherche IP inversée pour trouver d'autres serveurs partageant les mêmes adresses IP:

- https://viewdns.info
- https://threatintelligenceplatform.com/


## Identification des infrastructures

**Passive**

- https://sitereport.netcraft.com - Fournir des informations sur les serveurs sans même interagir avec eux
- http://web.archive.org/

Inspecter les URL enregistrées par Wayback Machine et rechercher des mots-clés spécifiques

```sh
waybackurls -dates https://target.com > waybackurls.txt
```

**Active**

```sh
# Identification de la technologie.
whatweb -a 3 https://$TARGET -v

# Empreintes digitales WAF.
wafw00f -v https://$TARGET

# Obtenir rapidement un aperçu des surfaces d'attaque HTTP en analysant une liste de ports configurables, en visitant le site web avec un navigateur Chrome sans interface utilisateur et en effectuant une capture d'écran.
cat subdomain.list | aquatone -out ./aquatone -screenshot-timeout 1000
```

## Active Subdomain Enumeration

**Transferts de zone**

- https://hackertarget.com/zone-transfer/

```sh
# Identification des serveurs de noms
nslookup -type=NS $TARGET

# Transfert de zone à l'aide de Nslookup sur le domaine cible et son serveur de noms.
nslookup -type=any -query=AXFR $TARGET <nameserver>
```

> Si nous parvenons à effectuer un transfert de zone réussi pour un domaine, il n'est pas nécessaire de continuer à énumérer ce domaine particulier car cela extraira toutes les informations disponibles.



