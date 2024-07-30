import smtplib, ssl


host = "smtp.gmail.com"

port = 465
user_name = "frederickkankam7@gmail.com"
password = "pytw rcev zcrl txbq"

receiver = "frederickkankam7@gmail.com"

subject = "Test Email"

message = """\
Subject: Trial Test Email
How are you doing today?
Bye!"""

context = ssl.create_default_context()

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(user_name, password)
    server.sendmail(user_name, receiver, message)
