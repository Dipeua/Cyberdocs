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
