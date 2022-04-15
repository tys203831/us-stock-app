import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Website", page_icon=":wave:", layout="wide")

# --HEADER SECTION---
with st.container():
    st.subheader('Hi, I am Yong Sheng :smile:')
    st.title("A first try on streamlit website building")
    st.write("I am passionate to write python code to get more data.")
    st.write("[Learn more here:](https://tanyongsheng.xyz)")

# --- LOAD ASSET ---
def load_lottieurl(url):
    image = requests.get(url)
    if image.status_code !=200:
        return None
    return image.json()

lottie_coding = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_tno6cg2w.json")

# ---- BODY SECTION ------
with st.container():
    st.write("----")
    #--- CREATE 2 COLUMNS ----
    left_column, right_column = st.columns(2)
    #--- ADD CONTENT INTO LEFT COLUMN ---  
    with left_column:
        st.write("##")
        st.write("""
                I am trying to learn as much as possible, hoping that I would be able to integrate my skills.
                I could complete all my tasks through continuing my efforts to do something that I like.
                """)
        st.write("[Affiliate website >](https:pickufly.com)")
    
    # ADD ANIMATION to the right column
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")