import streamlit as sl

sl.set_page_config(page_title="Contact Us", page_icon="images/Contact_Use.png", layout="wide")

sl.header("Contact Us")

with sl.form(key="contact_form"):
    email = sl.text_input("Email")
    message = sl.text_area("Message")
    button = sl.form_submit_button("Submit")
    if button:
        sl.success("Message sent successfully!")