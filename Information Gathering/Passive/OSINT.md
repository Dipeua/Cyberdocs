[Online Ressouces](./Online%20Ressouces.md)

Scan each IP address in a list using Shodan.

```sh
for i in $(cat ip-addresses.txt);do shodan host $i;done
```

Use tools like to automate process
- https://github.com/michenriksen/gitrob
- https://github.com/michenriksen/gitleaks
- maltego
- https://github.com/initstring/linkedin2username


Rechercher par GPS

```sh
# 51 deg 30' 51.90" N, 0 deg 5' 38.73" W
# NB: deg = "°" and , = " "

51°30'51.9"N 0°05'38.7"W
```

## Infrastructure Identification

- [NetCraft](https://sitereport.netcraft.com/)

Pay special attention to the latest IPs used. Sometimes we can spot the actual IP address from the webserver before it was placed behind a load balancer, WAF, or IDS, allowing us to connect directly to it if the configuration allows it

- [Wayback Machine](http://web.archive.org/)

Used to find older versions of a website at a point in time