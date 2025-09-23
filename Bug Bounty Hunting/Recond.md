
Install go

```sh
sudo apt install golang-go

# on .zshrc
export GOPATH="$HOME/go"
export PATH="$PATH:$GOPATH/bin"
```

Install massdns

```sh
git clone https://github.com/blechschmidt/massdns
cd massdns
sudo apt install build-essential
make
```

Install all Project Discovery tools

```
go install -v github.com/projectdiscovery/pdtm/cmd/pdtm@latest
```

Subdomain enumeration

```sh
$TARGET=web.com

subfinder -silent -d $TARGET -all -o subdomains-out.txt

# Subdomain Resolving (resolve a list of subdomains)
shuffledns -silent -d $TARGET -list subdomains-out.txt -r resolvers.txt -mode resolve

# Subdomain Bruteforcing
shuffledns -silent -d $TARGET -w wordlist.txt -r resolvers.txt -mode bruteforce
```

https://github.com/trickest/resolvers

```sh
cat subdomains-out.txt | alterx -silent | dnsx -silent
```

Port scan

```sh
cat subdomains-out.txt | alterx -silent | dnsx -silent | naabu -top-ports 100 -ep 22 -o open-ports.txt
```


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

