# DNS

Assign target to an environment variable.

```sh
export TARGET="domain.tld"
export PORT=443
```

Makes screenshots of all subdomains in the `subdomain.list` with Aquatone

```sh
cat subdomain.list | aquatone -out ./aquatone -screenshot-timeout 1000
```
## Subdomain Enumeration

- https://hackertarget.com/zone-transfer/

```sh
nslookup -type=any -query=AXFR $TARGET nameserver.target.domain
```

