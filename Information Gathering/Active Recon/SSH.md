# SSH

Remote security audit against the target SSH service.

```sh
ssh-audit.py <FQDN/IP>
```

Log in to the SSH server using the SSH client.

```sh
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
