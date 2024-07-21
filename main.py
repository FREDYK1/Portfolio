import streamlit as sl
import pandas

sl.set_page_config(layout="wide")

col1, col2 = sl.columns(2)

with col1:
    sl.image("images/21.png", width=450)

with col2:
    sl.title("Frederick Kwaku Kankam")
    content = """ 
    Hi, I am Fred! I am a Python programmer, and a Computer Science student in the University of Ghana(UG).
    I have a passion for innovation and solving real-life problems. I got my basic school education at Cejose Wisdom 
    International School.I had my secondary School Education at Chemu Senior High Technical School where I studied 
    General Science.
    """
    sl.info(content)

sl.text("Below you can find some of my projects:")

col3, col4 = sl.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        sl.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        sl.header(row["title"])