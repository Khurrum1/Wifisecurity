# Wifisecurity

**alldevices.py**
Discovers all Wi-Fi devices in the air.
Address2 in the WLAN header is the transmitter address. A unique set of transmitter addresses is created in order to get a unique set of Wi-Fi devices. 

**SSIDfinder.py**
Filters based on beacon frames and iterates through the DotElt list (tag parameters) to find the SSIDs

**uncoverssid.py**
Uncovers hidden SSIDs by monitoring probe responses from the same access point and probe responses contain the SSID, which will be uncovered
