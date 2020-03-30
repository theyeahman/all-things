#!/usr/bin/env python3
import os
import requests
from collections import OrderedDict

def open_file(directory,file):
    dict_text = OrderedDict()
    keys = ["name","weight","description"]
    count = 0
    with open(os.path.join(directory,file)) as f:
        for line in f:
            if line.strip() != "":
                dict_text[keys[count]] = line.strip()
                if keys[count] == 'weight':
                    dict_text[keys[count]] = line[:-5]
                count += 1
        dict_text['image_name'] = file[:-4]+'.jpeg'

    return dict_text

def main():
    dir = "./supplier-data/descriptions/"
    dir_img = "./supplier-data/images/"
    url = "http://35.193.101.124/fruits/"
    for i in os.listdir(dir):
        if i[-3:] == "txt":
            comp_dict =  open_file(dir,i)
            requests.post(url, data=comp_dict)

if __name__ == '__main__':
    main()
