import socket

rawSocket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))

rawSocket.bind(("wlan1mon", 0x0003))

ap_list = set()

# TODO: No funca.
# El byte 26 no es \x80, aparentemente

while True :
    pkt = rawSocket.recvfrom(2048)[0]
    if pkt[26] == "\x80":
        if pkt[36:42] not in ap_list  and ord(pkt[63]) > 0:
            ap_list.add(pkt[36:42])
            print("SSID: {}  AP MAC: {}".format(pkt[64:64 +ord(pkt[63])], pkt[36:42].encode('hex')))
    else:
        print('nope')
        print(pkt[26])
