import smtplib
import ssl


def send_email(message, user_email):
    host = "smtp.gmail.com"
    port = 465
    password = "pytw rcev zcrl txbq"
    receiver_email = "frederickkankam7@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(receiver_email, password)
        server.sendmail(user_email, receiver_email, message)