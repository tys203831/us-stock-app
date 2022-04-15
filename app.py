import streamlit as st

st.set_page_config(page_title="My Website", page_icon=":wave:", layout="wide")



# --HEADER SECTION---
with st.container():
    st.subheader('Hi, I am Yong Sheng :smile:')
    st.title("A first try on streamlit website building")
    st.write("I am passionate to write python code to get more data.")
    st.write("[Learn more here:](https://tanyongsheng.xyz)")

# ---- ------
with st.container():
    st.write("----")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("##")
        st.write("""
                I am trying to learn as much as possible, hoping that I would be able to integrate my skills.
                I could complete all my tasks through continuing my efforts to do something that I like.
                """)
        st.write("[Affiliate website >](https:pickufly.com)")
    
    
