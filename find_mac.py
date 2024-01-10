Find MAC addresses with associated IP in a network

import scapy.all as scapy

def scan(ip):
  arp_request = scapy.arping(ip)
  print(arp_request)

scan("192.168.1.1/24")
