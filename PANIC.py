#!/usr/bin/env python3

import time
import socket
from generated_tlv import *

# UDP Setup
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

SQUIM_PORT = 11000

def send_tlv_packet(packet):
    sock.sendto(packet.to_bytes(), ('255.255.255.255', SQUIM_PORT))

for _ in range(5):
    send_tlv_packet(TLVPacketPanic())
    time.sleep(.1)
