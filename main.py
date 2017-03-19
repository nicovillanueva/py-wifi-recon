#!/usr/bin/env python3

from wifi import Cell
from wifi.exceptions import InterfaceError
import time
import argparse

# dict de cells unicas, cada una con su ssid, maximo dBm y timestamp de cuando fue captada
known_networks = {}
# {'aa:bb:cc': {'dbm': -90, 'ssid': 'pitos', 'timestamp': 1010101}, 'dd:ee:ff': {'dbm': -1, 'ssid': 'tetas', 'timestamp': 2020202}}

def get_timestamp():
    return int(time.time())

def register_networks(nets, timestamp):
    for network in nets:
        if (network.address in known_networks and network.signal > known_networks.get(network.address)['dBm']) \
        or network.address not in known_networks:
            prev_signal = known_networks.get(network.address)['dBm'] if network.address in known_networks else 'unknown'
            print('updating network: {} ({}) from {} to {} at {}'.format(network.address, network.ssid, prev_signal, network.signal, timestamp))
            known_networks[network.address] = {'dBm': network.signal, 'timestamp': timestamp, 'ssid': network.ssid}
        else:
            # print("noop")
            pass

def main(interface):
    try:
        while True:
            try:
                networks = Cell.all(interface)
            except InterfaceError:
                print('error reading interface {}. will try again.'.format(interface))
                continue
            ts = get_timestamp()
            register_networks(networks, ts)
    except KeyboardInterrupt:
        print('quitting')
    print(known_networks)

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--interface', required=True, type=str, help='Interface to use to scan. NOT in monitor mode.')
args = parser.parse_args()

if __name__ == '__main__':
    main(args.interface)
