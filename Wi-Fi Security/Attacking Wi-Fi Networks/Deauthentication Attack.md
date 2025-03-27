# Deauthentication Attack

Deauthentication attacks force the victim to actually disconnect from the network. if you abuse this technique, chances are that your attack will be noticed! So keep this mind during your penetration testing in a real-world.

```sh
sudo aireplay-ng -0 10 -c <client_mac> -a <bssid> wlan0mon
```

With this simple technique we able to gather the data frames and we can also repeat the process to gather even more data frames.

You can collect a minor amount of IVs with deauthentication.