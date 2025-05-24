# PortMapper

Tourne sur le port TCP/UDP 111 et 32771 utiliser avec [NFS](./NFS.md)
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

**RID Cycling**

Interroger manuellement chaque RID utilisateur individuel

```sh
for i in $(seq 500 2000); do echo "queryuser $i" |rpcclient -U "" -N 10.211.11.10 2>/dev/null | grep -i "User Name"; done
```