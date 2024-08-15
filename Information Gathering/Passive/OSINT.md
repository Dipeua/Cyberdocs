Certificate transparency.

```sh
curl -s 'https://crt.sh/\?q\=<target-domain>\&output\=json' | jq .
```

Scan each IP address in a list using Shodan.

```sh
for i in $(cat ip-addresses.txt);do shodan host $i;done
```

---
Whois, le registraire de domaine

```c
whois <FQDN/IP>
```

- https://whois.icann.org
- https://www.namecheap.com

---
Netcraft
- https://searchdns.netcraft.com

---
Open Source Code
- https://github.com

```c
filename:KEYWORDS*
```

Use tools like to automate process
- https://github.com/michenriksen/gitrob
- https://github.com/michenriksen/gitleaks

---
Security Headers  Scanner
- https://securityheaders.com

---
Pastebin
- https://pastebin.com

---
Social Media Tools
- https://social-searcher.com

Site-Specific Tools
- https://digi.ninja/projects/twofi.php
- https://github.com/initstring/linkedin2username

---
Information Gathering Frameworks
- https://osintframework.com
- https://www.paterva.com/index.php
- `maltego`

---
Rechercher par GPS

```SH
51 deg 30' 51.90" N, 0 deg 5' 38.73" W => << 51°30'51.9"N 0°05'38.7"W >>
```

