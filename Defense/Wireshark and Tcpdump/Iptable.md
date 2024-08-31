Configurer un pare-feu pour répondre avec un paquet RST TCP

```sh
sudo iptables -I INPUT -p tcp --dport <port> -j REJECT --reject-with tcp-reset
```

