## Python scanner

### Requerimientos

1. Python 3
2. Acceso `sudo`
2. 'wifi'

Instalarlo con `pip3 install -r requirements.txt` o `pip3 install wifi`  
Recomendado usar `virtualenv`

### Correr

    sudo python3 main.py -i wlan1

### Ejemplo

    sudo python3 main.py -i wlan1
    updating network: 38:60:77:A4:68:A1 (The Beardhouse) from unknown to -42 at 1489958375
    updating network: 60:31:97:4D:92:73 (WiFi-Arnet-7ecc) from unknown to -87 at 1489958375
    updating network: 8C:10:D4:93:FF:E6 (Telecentro-ffe0) from unknown to -87 at 1489958375
    updating network: 8C:10:D4:93:FF:E6 (Telecentro-ffe0) from -87 to -78 at 1489958380
    updating network: 8C:10:D4:90:5E:76 (Telecentro-5e70) from unknown to -95 at 1489958380
    updating network: 5C:F4:AB:BE:9B:B0 (Los Incas) from unknown to -62 at 1489958380
    updating network: 8C:10:D4:89:5C:86 (telecentro-5c80) from unknown to -81 at 1489958380
    updating network: A4:5D:A1:6D:3B:E9 (JBArnet) from unknown to -75 at 1489958380
    updating network: D8:97:BA:06:36:C2 (ca54ea) from unknown to -80 at 1489958380
    updating network: 60:02:92:60:34:2E (c46cea) from unknown to -90 at 1489958380
    updating network: 8C:10:D4:8A:80:BE (Telecentro-80b8) from unknown to -76 at 1489958380
    updating network: D8:97:BA:11:6B:45 (ce1dcc) from unknown to -81 at 1489958380
    updating network: C8:3D:D4:1F:BE:A0 (Fibertel WiFi638 2.4GHz) from unknown to -90 at 1489958380
    updating network: 8C:10:D4:8E:BF:1E (JOSENET) from unknown to -95 at 1489958380
    updating network: 20:CF:30:04:12:04 (Telecentro-F794) from unknown to -83 at 1489958380
    updating network: 8C:10:D4:90:40:A6 (Telecentro-40a0) from unknown to -84 at 1489958380
    updating network: 60:31:97:4D:92:73 (WiFi-Arnet-7ecc) from -87 to -85 at 1489958381
    updating network: D8:97:BA:06:36:C2 (ca54ea) from -80 to -79 at 1489958381
    updating network: C8:3D:D4:1F:BE:A0 (Fibertel WiFi638 2.4GHz) from -90 to -89 at 1489958381
    updating network: 8C:10:D4:8E:BF:1E (JOSENET) from -95 to -82 at 1489958381
    updating network: 8C:10:D4:89:5C:86 (telecentro-5c80) from -81 to -79 at 1489958382
    updating network: 60:02:92:60:34:2E (c46cea) from -90 to -83 at 1489958382
    updating network: 8C:10:D4:90:5E:76 (Telecentro-5e70) from -95 to -92 at 1489958385
    updating network: E0:69:95:66:16:F5 (telebeta) from unknown to -93 at 1489958385
    updating network: 8C:10:D4:89:5C:86 (telecentro-5c80) from -79 to -78 at 1489958386
    updating network: D8:97:BA:06:36:C2 (ca54ea) from -79 to -69 at 1489958386
    updating network: E0:69:95:66:16:F5 (telebeta) from -93 to -83 at 1489958388
    updating network: FA:8F:CA:60:9D:91 () from unknown to -83 at 1489958388
    updating network: FA:8F:CA:57:E9:F9 () from unknown to -84 at 1489958388
    updating network: 8C:10:D4:90:40:A6 (Telecentro-40a0) from -84 to -83 at 1489958390
    updating network: 60:31:97:4D:92:73 (WiFi-Arnet-7ecc) from -85 to -76 at 1489958392
    updating network: 60:02:92:60:34:2E (c46cea) from -83 to -82 at 1489958392
    updating network: C8:3D:D4:1F:BE:A0 (Fibertel WiFi638 2.4GHz) from -89 to -83 at 1489958392
    updating network: FA:8F:CA:9C:C7:40 () from unknown to -87 at 1489958392
    ^Cquitting
    {'38:60:77:A4:68:A1': {'dBm': -42, 'timestamp': 1489958375, 'ssid': 'The Beardhouse'}, '60:31:97:4D:92:73': {'dBm': -76, 'timestamp': 1489958392, 'ssid': 'WiFi-Arnet-7ecc'}, '8C:10:D4:93:FF:E6': {'dBm': -78, 'timestamp': 1489958380, 'ssid': 'Telecentro-ffe0'}, '8C:10:D4:90:5E:76': {'dBm': -92, 'timestamp': 1489958385, 'ssid': 'Telecentro-5e70'}, '5C:F4:AB:BE:9B:B0': {'dBm': -62, 'timestamp': 1489958380, 'ssid': 'Los Incas'}, '8C:10:D4:89:5C:86': {'dBm': -78, 'timestamp': 1489958386, 'ssid': 'telecentro-5c80'}, 'A4:5D:A1:6D:3B:E9': {'dBm': -75, 'timestamp': 1489958380, 'ssid': 'JBArnet'}, 'D8:97:BA:06:36:C2': {'dBm': -69, 'timestamp': 1489958386, 'ssid': 'ca54ea'}, '60:02:92:60:34:2E': {'dBm': -82, 'timestamp': 1489958392, 'ssid': 'c46cea'}, '8C:10:D4:8A:80:BE': {'dBm': -76, 'timestamp': 1489958380, 'ssid': 'Telecentro-80b8'}, 'D8:97:BA:11:6B:45': {'dBm': -81, 'timestamp': 1489958380, 'ssid': 'ce1dcc'}, 'C8:3D:D4:1F:BE:A0': {'dBm': -83, 'timestamp': 1489958392, 'ssid': 'Fibertel WiFi638 2.4GHz'}, '8C:10:D4:8E:BF:1E': {'dBm': -82, 'timestamp': 1489958381, 'ssid': 'JOSENET'}, '20:CF:30:04:12:04': {'dBm': -83, 'timestamp': 1489958380, 'ssid': 'Telecentro-F794'}, '8C:10:D4:90:40:A6': {'dBm': -83, 'timestamp': 1489958390, 'ssid': 'Telecentro-40a0'}, 'E0:69:95:66:16:F5': {'dBm': -83, 'timestamp': 1489958388, 'ssid': 'telebeta'}, 'FA:8F:CA:60:9D:91': {'dBm': -83, 'timestamp': 1489958388, 'ssid': ''}, 'FA:8F:CA:57:E9:F9': {'dBm': -84, 'timestamp': 1489958388, 'ssid': ''}, 'FA:8F:CA:9C:C7:40': {'dBm': -87, 'timestamp': 1489958392, 'ssid': ''}}
