import streamlit as sl
import pandas
import os

sl.set_page_config(page_title="CEO's Portfolio", page_icon="images/Kantech_favicon.png", layout="wide")

col1, col2 = sl.columns(2)

with col1:
    sl.image("images/21.png", use_column_width=True)

with col2:
    sl.title("Frederick Kwaku Kankam")
    content = """
    Hello, I am Fred, an enthusiastic Python programmer, a dedicated Computer Science student at the University of
     Ghana (UG) and founder of KanTech Labs. FMy journey in the world of technology began with a solid foundation at Cejose Wisdom International
     School, where I cultivated a love for learning and curiosity. This journey continued at Chemu Senior High Technical
      School, where I excelled in General Science, laying the groundwork for my future in tech.At the University of
      Ghana, I am immersed in a dynamic and rigorous Computer Science program that sharpens my analytical and
      problem-solving skills. My coursework and projects have allowed me to delve deeply into various aspects of
      computer science, including software development, data structures, algorithms, and machine learning.
      I am particularly proficient in Python, leveraging its versatility to create innovative solutions and streamline
       complex processes. My passion for innovation drives me to seek out and tackle real-world problems through
       technology. I am committed to continuous learning and staying updated with the latest industry trends and
       advancements. My goal is to contribute to impactful projects that push the boundaries of what technology can
       achieve. Whether it's developing scalable software, optimizing algorithms, or exploring new technological
       frontiers, I am eager to apply my skills in a meaningful way. In addition to my academic pursuits, I actively
       participate in tech communities and collaborative projects. This involvement not only enhances my technical
       expertise but also hones my teamwork and communication skills, essential for thriving in the tech industry.
       I am always open to new challenges and opportunities to collaborate with like-minded professionals who share my
       vision for leveraging technology to make a positive difference in the world. Thank you for considering my profile
       . I look forward to the possibility of contributing to your innovative and forward-thinking projects.
    """
    sl.info(content)

sl.text("Below you can find some of my projects:")

col3, empty_col, col4 = sl.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:7].iterrows():
        sl.header(row["title"])
        sl.write(row["description"])
        sl.image(F"images/{row['image']}")
        sl.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[6:].iterrows():
        sl.header(row["title"])
        sl.write(row["description"])
        sl.image(F"images/{row['image']}")
        sl.write(F"[Source Code]({row['url']})")
