# Port Scanning

[[NMAP]]

Scanner de port windows

```sh
. .\Invoke-Portscan.ps1
Invoke-Portscan -Hosts 172.16.0.10 -TopPorts 50
```

Identifying HTTP methods using Nmap

```
nmap --script http-method -p80,443,8080 domain.com
```


masscan

```sh
sudo masscan -p80 192.168.45.0/24 --rate=10000 -e eth0 --router-ip 192.168.45.1
```