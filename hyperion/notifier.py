"""Sends email notifications.
"""


import smtplib

from hyperion import config


def send(to_address, subject, message):
    USERNAME = config['DEFAULT']['gmail_username']
    PASSWORD = config['DEFAULT']['gmail_password']
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(USERNAME, PASSWORD)

    contents = "\r\n".join([
        'From: %s' % USERNAME,
        'To: %s' % to_address,
        'Subject: Hyperion: %s' % subject,
        '',
        message
    ])

    server.sendmail(USERNAME, to_address, contents)
    server.close()