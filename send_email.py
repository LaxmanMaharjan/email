import smtplib
import os
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

msg = EmailMessage()
msg['Subject'] = 'Checking smtplib FROM GITHUB'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'lxmnmrzn@gmail.com'

msg.set_content('This is a email check.')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS.decode(), EMAIL_PASSWORD.decode())
    smtp.send_message(msg)
