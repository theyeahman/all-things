#!/usr/bin/env python3
import os
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
styles = getSampleStyleSheet()
report = SimpleDocTemplate("/tmp/processed.pdf")

dir = "./supplier-data/descriptions/"

long_text = []
for i in os.listdir(dir):
    with open(os.path.join(dir,i)) as f:
        long_text.append('name: ' + f.readline().strip() + '<br/>')
        long_text.append('weight: ' + f.readline().strip() + '<br/>')
    long_text.append(' <br/>')

paragraph_fruit = "".join(long_text)
report_title = Paragraph("Supplied inventory", styles['h1'])
report_body = Paragraph(paragraph_fruit, styles['Normal'])
if __name__ == "__main__":
    report.build([report_title,report_body])
