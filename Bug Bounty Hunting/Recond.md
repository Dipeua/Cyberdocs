
# Reconnaissance

Installation

```sh
sudo apt install -y golang-go
# on .zshrc
export GOPATH="$HOME/go"
export PATH="$PATH:$GOPATH/bin"

# Install massdns
git clone https://github.com/blechschmidt/massdns
cd massdns
sudo apt install build-essential
make

# Install all Project Discovery tools
go install -v github.com/projectdiscovery/pdtm/cmd/pdtm@latest
pdtm -ia -ua
```

## Discovering Domains

**Find root domain for a particular target**

- Go to https://www.whoxy.com
- Enter the domain target (ex: sony.com) and look at the Company section
- Find ASN for a particular organisation

	- Go to https://bgp.he.net and search for organisation (ex: sony)

```sh
amass intel -org "SONY" -v
amass intel -asn "ASN_VALUE" -o sony_amass_asn.txt -v
```

## Discovering Subdomains

**Subdomain enumeration**

```sh
export $TARGET=sony.com
subfinder -silent -pc -all -recursive -active -d $TARGET -o sony_subfinder_subdomains.txt
```

```sh
amass enum -d $TARGET | grep -Eo "([a-zA-Z0-9.-]+\.)*sony\.com" | sort -u | tee -a sony_amass_subdomains.txt
```

https://github.com/trickest/resolvers

Subdomain Bruteforcing

```sh
ffuf -c -ic -u https://FUZZ.$TARGET/ -w /usr/share/seclists/Discovery/DNS/all-subdomains.txt:FUZZ -o sony_ffuf_subdomains.txt

gobuster dns -q --do $TARGET --wc -w /usr/share/seclists/Discovery/DNS/all-subdomains.txt -o sony_gobuster_subdomains

amass enum -d $TARGET -brute -w /usr/share/seclists/Discovery/DNS/all-subdomains.txt -r resolvers.txt -v

puredns bruteforce /usr/share/seclists/Discovery/DNS/all-subdomains.txt $TARGET -resolvers resolvers.txt

shuffledns -silent -d $TARGET -w /usr/share/seclists/Discovery/DNS/all-subdomains.txt -r resolvers.txt -mode bruteforce
```

Subdomain VHost Fuzzing

```sh
ffuf -c -ic -u https://$TARGET/ -H 'Host: FUZZ.$TARGET' -w /usr/share/seclists/Discovery/DNS/all-subdomains.txt:FUZZ -o sony_ffuf_vhost_subdomains.txt
```

Subdomain Resolving (resolve a list of subdomains)

```sh
shuffledns -silent -d $TARGET -list subdomains.txt -r resolvers.txt -mode resolve
```

## Port Scanning

Finding Origin IP Address of website behind CloudFlare

https://github.com/christophetd/CloudFlair

```sh
export CENSYS_API_ID=
export CENSYS_API_SECRET=

python3 cloudflaire.py $TARGET
```

```sh
naabu -silent -host $TARGET -p 1-65535 -ep 22 -s SYN -source-ip 8.8.8.8 -Pn -sD -sV -verify -o sony_naabu_portscan.txt
```

## Content Discovery
## Combining Tools

```sh
cat subdomains-out.txt | alterx -silent | dnsx -silent | naabu -top-ports 100 -ep 22 | httpx-pd -title -sc -cl -fr -location -o httpx.txt
```

Content dicovery

```sh
katana -u http://target.com -jc -jsl
cat open-ports.txt | katana -jsl
cat open-ports.txt | katana -H 'headers' -xhr -jsl -aff

katana -u http://target.com -H 'headers' -xhr -jsl -aff | httpx -ct -cl -sc
```

For API

```sh
chaos-client -d target.com -silent | grep api | alterx -silent | dnsx -silent | naabu -p 443,8443 -silent | tee -a recon.txt
```

```
urlfinder -d target.com
```