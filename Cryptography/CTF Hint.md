# CTF Hint

Les variables clés que vous devez connaître pour le RSA dans les CTF sont : `p, q, m, n, e, d, c`

- `p et q` sont des grands nombres premiers, `n` est le produit de `p et q`.

```sh
n = (p * q)
```

- La clé publique est `n et e`, la clé privée est `n et d`.

```sh
public_key = n & e
private_key = n & d
```

- `m` est utilisé pour représenter le message (en texte brut) et `c` représente le texte chiffré (texte crypté).

```sh
clear_text = m
cipher_text = c
```
