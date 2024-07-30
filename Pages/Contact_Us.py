import streamlit as sl
from send_email import send_email

sl.set_page_config(page_title="Contact Us", page_icon="images/Contact_Use.png", layout="wide")

sl.header("Contact Us")

with sl.form(key="contact_form"):
    user_email = sl.text_input("Email")
    subject = sl.text_input("Subject")
    row_message = sl.text_area("Message")
    message = f"""\
Subject: {subject} 
From: {user_email}
{row_message}
"""
    button = sl.form_submit_button("Submit")
    if button:
        send_email(message, user_email)
        sl.success("Message sent successfully!")

