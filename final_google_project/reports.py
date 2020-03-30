#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import os

keys = ["name","weight"]
dir = "./supplier-data/descriptions/"
report = SimpleDocTemplate("/tmp/report.pdf")
long_text = []
for i in os.listdir(dir):
    with open(os.path.join(dir,i)) as f:
        count = 0
        for line in f:
            while count < 2:
                long_text.append(keys[count]+': ' + line)
                count += 1
    long_text.append(' \n')

print(long_text)

# combine array into one string and then make the report
