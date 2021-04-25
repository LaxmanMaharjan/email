import smtplib

from email.message import EmailMessage


msg = EmailMessage()
msg['Subject'] = 'Checking smtplib'
msg['From'] = 'kce074bct020@gmail.com'
msg['To'] = 'lxmnmrzn@gmail.com'

msg.set_content('This is a email check.')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login("kce074bct020@gmail.com", "khwopacollege9849")
    smtp.send_message(msg)
