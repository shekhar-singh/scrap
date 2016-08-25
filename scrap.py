#!usr/bin/env python 

import requests
from bs4 import BeautifulSoup

url = requests.get("http://video9.in/english/")
soup=BeautifulSoup(url.text)
for link in soup.find_all("div",{"class": "updates"}):
    print link.text
