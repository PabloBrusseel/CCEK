# ChromeCast Exploitation Kit
Controlling ChromeCasts though the command line. Made by [Brussec Security](https://brussec.com) with :heart:

## Requirements
* Python 3
* Curl
* Pip

## Installation

All you really need to do is install python and curl and clone this repository.
But just because I can, here are the commands:

```
sudo apt-get install python curl
git clone https://github.com/PabloBrusseel/CCEK.git
pip3 install requirements.txt
```

## Usage

```
CCEK.py -t <target> -a <action> -v <value>
```

### Supported actions/commands

- **play** : Play a Youtube video with ID specified in the value parameter
- **setName** : Set the device name to the value specified in the value parameter
- **scanWifi** : Scan nearby Wifi networks
- **reboot** : Reboot the device
- **factoryReset** : Resets the device to Factory Settings (USE WITH CARE)

### Examples

Change the device name of a ChromeCast
```
CCEK.py -t 192.168.0.43 -a setName -v "Pablo is my hero"
```

Play a video (Rick Roll)
```
CCEK.py -t 192.168.0.43 -a play -v dQw4w9WgXcQ
```

Reboot the ChromeCast
```
CCEK.py -t 192.168.0.43 -a reboot
```

## Contact
* __Twitter:__ [@pablobrusseel](https://twitter.com/pablobrusseel)
* __Website:__ [Brussec Security](https://brussec.com)

## Disclaimer
The idea for this tool came after some guy sent curl requests to publicly-exposed ChromeCasts on the internet to spread PewDiePie propaganda. As this is documented functionality, you can't actually call this an exploit. Although one could wonder why this is possible without a single form of authentication.

## Thanks to
Thank you to @terremoth for updating the code to Python 3.
