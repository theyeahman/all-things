#!/usr/bin/env python3

import email.message
import mimetypes
import os.path
import smtplib
import psutil
import shutil

def generate(sender, recipient, subject, body):
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)
    return message

def send(message):
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()

class cpu_too_high(Error):
   """Raised when the CPU is too high """
   pass

def check_cpu():
    if psutil.cpu_percent() > 80:
        raise cpu_too_high

try:
    check_cpu()
except cpu_too_high:
    from1 = 'automation@example.com'
    to1 = 'student-00-ce122bac9ef8@example.com'
    subject1 = 'Error - CPU too high'
    body1 = 'Please check your system and resolve the issue as soon as possible.'
    message = generate(from1,to1,subject1,body1)
    send(message)
except:
    print('Unknown error')
