#!/usr/bin/env python
from getpass import getpass
import smtplib  # <1>

DEBUG = True  # set to false for production

smtp_user = 'pythonclass'

sender = 'jstrick@mindspring.com'
recipients = ['jstrickler@gmail.com']
msg = '''Subject: SMTP example
Hello hello?
Testing email from Python
'''

# Gr3@t$tud3nt

smtp_pwd = getpass("Enter SMTP server password:")

smtpserver = smtplib.SMTP("smtpcorp.com", 2525)  # <2>
smtpserver.login(smtp_user, smtp_pwd)  # <3>
smtpserver.set_debuglevel(DEBUG)  # <4>

try:
    smtpserver.sendmail(
        sender,
        recipients,
        msg
    )  # <5>
except smtplib.SMTPException as err:
    print("Unable to send mail:", err)
finally:
    smtpserver.quit()  # <6>
