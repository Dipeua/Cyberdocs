Tourne sur le port TCP/UDP 111 et 32771 utiliser avec [[Information Gathering/Active/NFS|NFS]]
Utiliser pour mapper tout les `Open Network Computing Remote Prodecure Call`

Permet de voir quel port sont port ouvert localement sur le systeme (localhost)

```sh
nmap -sV -p 111 --script=rpc-grind,rpcinfo <FQDN/IP>
```


```
rpcinfo -p <FQDN/IP>
```

Interaction with the target using RPC.

```sh
rpcclient -U "" <FQDN/IP>
```

