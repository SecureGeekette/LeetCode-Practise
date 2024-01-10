Script to find subdomains - iterating through a probable word list

import requests

def get_requests(url):
  try:
    requests.get(url)
    print("Found subdomain: " + url)
  except requests.exceptions.ConnectionError:
    pass 
    
with open("subdomains-wodlist.txt", "r") as f:
  for line in f:
    line = line.strip()
    find_url = "https://" + line + ".google.com"
    get_requests(find_url)
      
