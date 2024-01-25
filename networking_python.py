Take this excel of ips, ping them, resolve them against dns, export finding

import pandas as pd
import openpyxl
import subprocess
import socket

file_path = "/Users/sgaruda/Desktop/ip_list.xlsx"
csv_reader = pd.read_excel(file_path)

def ping(ip):
    result = subprocess.run(['ping','-c', '4', ip], capture_output=True, text=True)
    print(result.stdout)

def reverse_dns_lookup(ip):
    try:
        print(socket.gethostbyaddr(ip))
    except socket.herror as e:
        print("Reverse DNS lookup failed")


for ip in csv_reader['ip']:
    ping(ip)
    reverse_dns_lookup(ip)


