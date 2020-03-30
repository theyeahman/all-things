#!/usr/bin/env python3

import email.message
import mimetypes
import os.path
import smtplib

def generate(sender, recipient, subject, body, attachment_path):
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    attachment_filename = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/',1)

    with open(attachment_path, 'rb') as ap:
        message.add_attachment(ap.read(), maintype=mime_type, subtype=mime_subtype, filename=attachment_filename )

    return message

def send(message):
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()

if __name__ == '__main__':
    from1 = 'automation@example.com'
    to1 = 'student-00-ce122bac9ef8@example.com'
    subject1 = 'Upload Completed - Online Fruit Store'
    body1 = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
    Attachment = '/tmp/processed.pdf'
    message = generate(from1,to1,subject1,body1,Attachment)
    send(message)
