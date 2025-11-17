## WHOIS

WHOIS lookup for the target.

```sh
whois target.com
```

Reverse Lookup Brute Force

```sh
for ip in $(seq 50 100); do host X.X.X.$ip; done | grep -v "not found"
```

## DNS Enumeration

Identify records for the target

```sh
nslookup -query=[A, AAAA, PTR, MX, TXT, ANY, NS] target.com

dig [A, AAAA, PTR, MX, TXT, ANY] target.com @<nameserver/IP>
dig -x <IP> @<nameserver/IP>
```

```sh
# AXFR request to the specific nameserver. 
dig axfr target.com @<nameserver>
dig axfr target.com @NSZTM1.DIGI.NINJA | cut -d " " -f3
```

## Passive Subdomain Enumeration

- [VirusTotal](https://www.virustotal.com/gui/home/search)
- Project Sonar

```sh 
# Tous les sous-domaines pour un domaine donné.
curl -s https://sonar.omnisint.io/subdomains/target.com | jq -r '.[]' | sort -u 

# Tous les TLD trouvés pour un domaine donné.
curl -s https://sonar.omnisint.io/tlds/target.com | jq -r '.[]' | sort -u      

# Tous les résultats sur tous les TLD pour un domaine donné.
curl -s https://sonar.omnisint.io/all/target.com | jq -r '.[]' | sort -u       

# Reverse DNS lookup on IP address
curl -s https://sonar.omnisint.io/reverse/{ip}        

# Reverse DNS lookup of a CIDR range
curl -s https://sonar.omnisint.io/reverse/{ip}/{mask} 
```

**Certificate Transparency.**

Les certificats SSL/TLS constituent une autre source d'informations intéressante pour extraire des sous-domaines. 

- https://search.censys.io/
- https://crt.sh

```sh
# Transparence des certificats.
curl -s "https://crt.sh/?q=target.com&output=json" | jq -r '.[] | "\(.name_value)\n\(.common_name)"' | sort -u > "crt.sh_ouput.txt"
```

```sh
openssl s_client -ign_eof 2>/dev/null <<<$'HEAD / HTTP/1.0\r\n\r' -connect "target.com" | openssl x509 -noout -text -in - | grep 'DNS' | sed -e 's|DNS:|\n|g' -e 's|^\*.*||g' | tr -d ',' | sort -u
```

**theHarvester**

```sh
export TARGET=target.com

# Collecter des informations à partir de ces sources.
cat sources.txt | while read source; do theHarvester -d "${TARGET}" -b $source -f "${source}_${TARGET}";done

# Extraire tous les sous-domaines trouvés et les trier
cat *.json | jq -r '.hosts[]' 2>/dev/null | cut -d':' -f 1 | sort -u > "${TARGET}_theHarvester.txt"

# Fusionner tous les fichiers
cat $TARGET_*.txt | sort -u > $TARGET_subdomains_passive.txt
```

La recherche IP inversée pour trouver d'autres serveurs partageant les mêmes adresses IP:

- [View DNS](https://viewdns.info)
- [Threati Intelligence Platform](https://threatintelligenceplatform.com/)
## Identification des infrastructures Passive

- [Netcraft](https://sitereport.netcraft.com)
- [WayBackMachine](http://web.archive.org/)

Inspecter les URL enregistrées par [Wayback Machine]([https://github.com/tomnomnom/waybackurls](https://github.com/tomnomnom/waybackurls)) et rechercher des mots-clés spécifiques

```sh
waybackurls -dates https://target.com > waybackurls_output.txt
```

## Active Subdomain Enumeration

- [Transferts de zone](https://hackertarget.com/zone-transfer/)
- [HackerTarget]([https://hackertarget.com/zone-transfer/](https://hackertarget.com/zone-transfer/))

```sh
# Identification des serveurs de noms
nslookup -type=NS target.com

# Transfert de zone à l'aide de Nslookup sur le domaine cible et son serveur de noms.
nslookup -type=any -query=AXFR target.com <nameserver>
```

> Si nous parvenons à effectuer un transfert de zone réussi pour un domaine, il n'est pas nécessaire de continuer à énumérer ce domaine particulier car cela extraira toutes les informations disponibles.

## Identification des infrastructures Active

```sh
# Identification de la technologie.
whatweb -a 3 https://target.com -v

# Empreintes digitales WAF.
wafw00f -v https://target.com
```

[Aquatone]([https://github.com/michenriksen/aquatone](https://github.com/michenriksen/aquatone)) effectuer des captures d'écran pour une liste de sous-domains

```sh
cat subdomains_output.txt | aquatone -out ./aquatone -screenshot-timeout 1000
```
