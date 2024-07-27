# Tcpdump

Ecouter sur un port

```sh
sudo tcpdump port 110 -A
```

Filter un fichier `.pcap` de wireshark

```sh
sudo tcpdump -n -r file.pcap
sudo tcpdump -n src host <IP> -r file.pcap
sudo tcpdump -n dst host <IP> -r file.pcap
sudo tcpdump -n port <PORT> -r file.pcap
```

---
# Wireshark

Structure d'un hash`AS-REQ` l'hors d'une `Pre-Auth`

```
$krb5pa${etype}${username}${domain}${cipher}
```

---
# IPTable

Configurer un pare-feu pour répondre avec un paquet RST TCP

```sh
sudo iptables -I INPUT -p tcp --dport <port> -j REJECT --reject-with tcp-reset
```

