import smtplib
import pickle

from email.message import EmailMessage

with open("Gmail.txt","rb") as file:
    gmail = pickle.load(file)
    
EMAIL_ADDRESS = gmail['username']
EMAIL_PASSWORD = gmail['password']


msg = EmailMessage()
msg['Subject'] = 'Checking smtplib'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'lxmnmrzn@gmail.com'

msg.set_content('This is a email check.' )


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
