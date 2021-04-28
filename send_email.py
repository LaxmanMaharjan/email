import smtplib
import os
import pandas as pd

from email.message import EmailMessage

data = pd.read_csv("emails.csv")

email_list = data.Email.tolist()

EMAIL_ADDRESS = os.environ['EMAIL_ADDRESS']
EMAIL_PASSWORD = os.environ['EMAIL_PASSWORD']

msg = EmailMessage()
msg['Subject'] = 'Checking smtplib FROM GITHUB'
msg['From'] = EMAIL_ADDRESS
msg['To'] = ", ".join(email_list)

msg.set_content('This is a email checking from github.')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
