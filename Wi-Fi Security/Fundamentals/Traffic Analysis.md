# Traffic Analysis

Before start analyzing wireless traffic, you have to

- Set up your wireless adapter
- Enable the monitor mode
- Try capturing from wlan0mon with wireshark

## Channel Hopping

Even if you can now sniff all of the packets being transmitted over the wireless medium, you are still restricted to one channel at a time. This is due to how wireless adapter internally de-modulate the received electromagnetic waves and can not be changed

The trick we can use is achieve and approximation is called `Channel Hopping`.

**Channel Hopping** refers to the technique of constantly switching the channel on which the wireless adapter operates.

> Obviously, while locked to a specific channel, the wireless adapter still can not receive frames sent on any others so this technique is mostly useful for **recon purposes** than to really capture data.

```sh
sudo airodumg-ng -w outputfile wlan0mon
```

This will create a file named `outputfile.cap` that you could open with Wireshark for frames dissection.

## Traffic decryption

**Enable traffic decryption on Wireshark**

Follow the step:

- `Edit -> Preferences` 
- Select `IEEE 802.11` from the left menu (under `Protocols section`)
- Check `Enable decryption` and add your key on `Decryption Keys.` 

_NB: The key here is the passphrase of the AP_


**The syntax to decrypt **WEP** packets :**

```sh
sudo airdecap -w <wep_key_in_hex> <.cap>
#sudo airdecap -w 00d34db33f wep_file.cap
```

**The syntax to decrypt **WPA** packets :**

```sh
sudo airdecap -p <wpa_passphrase> -e <SSID> <.cap>
#sudo airdecap -p password -e WIFIdipeua wpa_file.cap
```


Now try to open the produced -dec file with Wireshark 