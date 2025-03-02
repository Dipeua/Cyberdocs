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
```

Identify the record for the target IP address and [DNS Zone Transfert](../../Programming/dns-axfr.sh)

```sh
dig $TARGET @<nameserver>
dig any $TARGET @<nameserver>

# AXFR request to the specific nameserver. 
dig axfr $TARGET @<nameserver>
dig axfr $TARGET @NSZTM1.DIGI.NINJA | cut -d " " -f3
```

## Subdomain Enumeration

- https://censys.io
- https://crt.sh


```sh 
# All subdomains for a given domain
curl -s https://sonar.omnisint.io/subdomains/$TARGET | jq -r '.[]' | sort -u 
    
# All tlds found for a given domain
curl -s https://sonar.omnisint.io/tlds/$TARGET | jq -r '.[]' | sort -u      

# All results across all tlds for a given domain
curl -s https://sonar.omnisint.io/all/$TARGET | jq -r '.[]' | sort -u       

# Reverse DNS lookup on IP address
curl -s https://sonar.omnisint.io/reverse/{ip}        

# Reverse DNS lookup of a CIDR range
curl -s https://sonar.omnisint.io/reverse/{ip}/{mask} 
```

**Certificate Transparency.**

```sh
curl -s "https://crt.sh/?q=${TARGET}&output=json" | jq -r '.[] | "\(.name_value)\n\(.common_name)"' | sort -u > "${TARGET}_crt.sh.txt"
```

```sh
openssl s_client -ign_eof 2>/dev/null <<<$'HEAD / HTTP/1.0\r\n\r' -connect "${TARGET}:${PORT}" | openssl x509 -noout -text -in - | grep 'DNS' | sed -e 's|DNS:|\n|g' -e 's|^\*.*||g' | tr -d ',' | sort -u
```

## Automating Subdomain Enumeration


```sh
cat sources.txt | while read source; do theHarvester -d "${TARGET}" -b $source -f "${source}_${TARGET}";done

cat *.json | jq -r '.hosts[]' 2>/dev/null | cut -d':' -f 1 | sort -u > "${TARGET}_theHarvester.txt"

cat $TARGET_*.txt | sort -u > $TARGET_subdomains_passive.txt
```

Content of `sources.txt`

```
anubis
baidu
bevigil
binaryedge
bing
bingapi
bufferoverun
brave
censys
certspotter
criminalip
crtsh
dnsdumpster
duckduckgo
fullhunt
github-code
hackertarget
hunter
hunterhow
intelx
netlas
onyphe
otx
pentesttools
projectdiscovery
rapiddns
rocketreach
securityTrails
sitedossier
subdomaincenter
subdomainfinderc99
threatminer
tomba
urlscan
virustotal
yahoo
zoomeye

sublist3r
threatcrowd
trello
vhost
```

```sh
dnsrecon -d $TARGET -t axfr -a -w -g
dnsenum --dnsserver <nameserver> --enum -p 0 -s 0 -o found_subdomains.txt -f ~/subdomains.list $TARGET

fierce -dns $TARGET
```

La recherche IP inversée pour trouver d'autres serveurs partageant les mêmes adresses IP:

- https://viewdns.info
- https://threatintelligenceplatform.com/
- https://search.censys.io/


