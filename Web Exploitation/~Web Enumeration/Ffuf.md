Directory Fuzzing

```sh
ffuf -w directory-list-2.3-small.txt:FUZZ -u http://SERVER_IP:PORT/FUZZ
```

Extension Fuzzing

```sh
ffuf -w web-extensions.txt:FUZZ -u http://SERVER_IP:PORT/indexFUZZ 
```

Page Fuzzing

```sh
ffuf -w directory-list-2.3-small.txt:FUZZ -u http://SERVER_IP:PORT/blog/FUZZ.php 
```

Recursive Fuzzing

```sh
ffuf -w directory-list-2.3-small.txt:FUZZ -u http://SERVER_IP:PORT/FUZZ -recursion -recursion-depth 1 -e .php -v 
```

# DNS Recon

Sub-domain Fuzzing

```sh
ffuf -w subdomains-top1million-5000.txt:FUZZ -u https://FUZZ.hackthebox.eu/ 
```

VHost Fuzzing

```sh
ffuf -w subdomains-top1million-5000.txt:FUZZ -u http://academy.htb:PORT/ -H 'Host: FUZZ.academy.htb' -fs xxx 
```

# Parameter Fuzzing

Fuzzing GET

```sh
ffuf -w burp-parameter-names.txt:FUZZ -u http://admin.academy.htb:PORT/admin/admin.php?FUZZ=key -fs xxx 
```

Fuzzing POST

```sh
ffuf -w burp-parameter-names.txt:FUZZ -u http://admin.academy.htb:PORT/admin/admin.php -X POST -d 'FUZZ=key' -H 'Content-Type: application/x-www-form-urlencoded' -fs xxx 
```

Value Fuzzing

```sh
ffuf -w ids.txt:FUZZ -u http://admin.academy.htb:PORT/admin/admin.php -X POST -d 'id=FUZZ' -H 'Content-Type: application/x-www-form-urlencoded' -fs xxx  
```

# Wordlists

Directory/Page Wordlist

```sh
/opt/secLists/Discovery/Web-Content/directory-list-2.3-small.txt  
```

Extensions Wordlist

```sh
/opt/secLists/Discovery/Web-Content/web-extensions.txt  
```

Domain Wordlist

```sh
/opt/secLists/Discovery/DNS/subdomains-top1million-5000.txt 
```

Parameters Wordlist

```sh
/opt/secLists/Discovery/Web-Content/burp-parameter-names.txt 
```

---
#Misc

Add DNS entry

```sh
sudo sh -c 'echo "SERVER_IP  academy.htb" >> /etc/hosts'  
```
