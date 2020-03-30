
#! /usr/bin/env python3
import os
import requests
import json


def open_file(file):
    dict_text = {}
    keys = ["name","weight","description"]
    count = 0
    with open(file) as f:
        for line in f:
            dict_text[keys[count]] = line.strip()
            if keys[count] == 'weight':
                dict_text[keys[count]] = line[:-5]
            count += 1
    print(dict_text)
    return dict_text

def main():
    dir = "./supplier-data/descriptions/"
    for i in os.listdir(dir):
        if i[-3:] == "txt":
            comp_dict =  open_file(os.path.join(dir,i))

if __name__ == '__main__':
    main()
