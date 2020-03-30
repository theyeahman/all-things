#!/usr/bin/env python3
import requests
import os

dir = "./supplier-data/images/"
url = "http://localhost/upload/"
for i in os.listdir(dir):
    if i[-4:] == 'jpeg':
        with open(os.path.join(dir,i), 'rb') as opened:
            r = requests.post(url, files={'file': opened})
