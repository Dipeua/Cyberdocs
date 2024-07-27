Convertir un nom d'hote en address IP

---
Optenir l'IPv4 & v6 d'un domaine

```sh
host domain.tld
host -t {mx | txt | ns | ...} domain.tld
```

Reverse Lookup Brute Force

```sh
for ip in $(seq 50 100); do host X.X.X.$ip; done | grep -v "not found"
```

DNS Zone Transfert

```sh
host -l domain.tld <nameserver>
```

Automatiser le DNS Zone Transfert `dns-axfr.sh`

```sh
#!/bin/bash
if [ -z "$1" ]; then
	echo "[*] Simple Zone transfer script"
	echo "[*] Usage : $0 <domain name> "
	exit 0
fi
for server in $(host -t ns $1 | cut -d " " -f4); do
	host -l $1 $server | grep "has address"
done
```

```sh
dnsrecon -d domain.com -t axfr
dnsrecon -a -w -g -d domain.com
```

```
dnsenum domain.com
```


```sh
fierce -dns google.com
```

```sh
nmap --script dns-brute --script-args dns-brute.domain=google.com
```

Subdomain brute forcing.

```sh
dnsenum --dnsserver <nameserver> --enum -p 0 -s 0 -o found_subdomains.txt -f ~/subdomains.list domain.tld
```

```sh
sublist3r -d domain.com
```

```
nslookup domain.tld
```

```
traceroute domain.tld
```

---
NS request to the specific nameserver.

```
dig ns <domain.tld> @<nameserver>
```

ANY request to the specific nameserver.

```
dig any <domain.tld> @<nameserver>
```

AXFR request to the specific nameserver.

```
dig axfr <domain.tld> @<nameserver>
```

```
dig axfr domain.com @NSZTM1.DIGI.NINJA | cut -d " " -f3
```
