
Remote security audit against the target SSH service.

```
ssh-audit.py <FQDN/IP>
```

Log in to the SSH server using the SSH client.

```
ssh <user>@<FQDN/IP>
```

Log in to the SSH server using private key.

```sh
ssh -i private.key <user>@<FQDN/IP>
```

Enforce password-based authentication.

```sh
ssh <user>@<FQDN/IP> -o PreferredAuthentications=password
```
