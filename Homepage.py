import streamlit as lit
import time

img_1 = "/content/MTC logo.png"
img_2 = "/content/ESL_logo.png"

pages = {
    "MTC ESL Treasure Hunt": "MTC ESL Treasure Hunt",
    "The Challenge": "The Challenge",
    "The Resources": "The Resources",
    "MTC ESL GenAI Global Summit": "MTC ESL GenAI Global Summit",
}

for page_name, page_title in pages.items():
    if lit.sidebar.button(page_title, key=page_name):
        lit.session_state.page = page_name

page = getattr(lit.session_state, "page", list(pages.keys())[0])

lit.title(pages[page])

if page == "MTC ESL Treasure Hunt":
    lit.image(img_1, use_column_width=False, width=200)
    lit.subheader("Welcome to MTC's Emirati Sign Language Challenge! :wave:")
    lit.write("If you signed up as Player 1, go to the 'Challenge' page.")
    lit.write("If you signed up as Player 2, go to the 'Resources' page.")
    lit.write("If you'd like to learn more about the MTC ESL Generative AI Competition, click on that option in the sidebar!")

if page == "The Challenge":
    lit.write("Your partner has the resources that they need to help you. Work with them to choose the right options to each of the following 10 questions. Immediately after you are done, inform an MTC Council member.")
    lit.subheader("Some Things To Keep In Mind :wink:")
    lit.write("1. You get only **one** chance to play this game. :exclamation:")
    lit.write("2. The **faster** you are, the greater your chance of **winning** is! :medal:")
    lit.write("3. Only click 'Begin' **after you have informed an MTC council member** that you're going to begin. :stopwatch:")
    lit.write("4. We mainly focus on **Education, Environment, Professions, Sports, and Landmarks** :eyes:")
    lit.write("")

if page == "The Resources":
    lit.subheader("Guidelines")
    lit.markdown("[Here's the link to the UAE Sign Language Dictionary.](https://zho.gov.ae/en/Sign-Language-Dictionary/UAE-Sign-Language-Categories)")
    lit.write("Use it to help your partner answer all 10 questions correctly.")
    lit.subheader("Some Things To Keep In Mind :wink:")
    lit.write("1. You get only **one** chance to play this game. :exclamation:")
    lit.write("2. The **faster** you are, the greater your chance of **winning** is! :medal:")
    lit.write("3. Only click 'Begin' **after you have informed an MTC council member** that you're going to begin. :stopwatch:")
    lit.write("4. We mainly focus on **Education, Environment, Professions, Sports, and Landmarks** :eyes:")

if page == "MTC ESL GenAI Global Summit":
    lit.write("")
    lit.image(img_2, use_column_width=False, width=300)
    lit.write("Microsoft Tech Club is organizing the Emirati Sign Language (ESL) Generative AI Summit, which is a part of the International Conference on Computational Intelligence and Network Systems (CINS 2023).")
    lit.markdown("[Click here to find out more and register!](https://esl.pythonanywhere.com/)")
