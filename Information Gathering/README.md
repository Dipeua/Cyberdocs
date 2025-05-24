# Information Gathering

La collecte d'informations est la première étape de tout test d'intrusion. Elle consiste à simuler des attaquants externes sans disposer d'informations internes provenant de l'organisation ciblée.



## Port Scanning

[Nmap](./Nmap.md)

Scanner de port windows

```sh
. .\Invoke-Portscan.ps1
Invoke-Portscan -Hosts 172.16.0.10 -TopPorts 50
```

Identifying HTTP methods using Nmap

```sh
nmap --script http-method -p80,443,8080 domain.com
```

masscan

```sh
sudo masscan -p80 192.168.45.0/24 --rate=10000 -e eth0 --router-ip 192.168.45.1
```

Identifier tous les hôtes actifs de notre plage réseau cible

```sh
fping -agq CIDR
```