Enumeration 

```sh
wpscan --url http://target.com/ --enumerate u,vp,p,t
```

Effectuer une attaque par brute-force

```sh
wpscan --url http://target.com/ --passwords rockyou.txt --usernames cmnatic
```

- `--plugins-detection {passive | aggressive}` WAF-Bypass