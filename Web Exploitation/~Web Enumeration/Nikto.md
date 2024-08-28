Analyse un host avec nmap et nikto

```c
nmap -p80 172.16.0.1 -oG - | nikto -h -
```

Analyse de plusieurs ports

```sh
nikto -h 10.10.10.1 -p 80,8000,8080
```

Utiliser un plugin

```sh
nikto -h 10.10.10.1 -Plugin <plugin-name>
```