NFS (Network File System) écoute par défaut sur le port `2049` fonctionne avec [PortMapper (rpcbind)](./PortMapper%20(rpcbind).md)


```sh
sudo nmap --script nfs-ls,nfs-statfs,nfs-showmount <FQDN/IP> -p 111
```

---
Show available NFS shares.

```sh
showmount -e <FQDN/IP>
```

#Utilisation

Mount the specific NFS share.umount ./target-NFS

```sh
mount -t nfs <FQDN/IP>:/<share> /mnt/target-NFS/ -o nolock
```

Unmount the specific NFS share.

```sh
umount /mnt/target-NFS
```
