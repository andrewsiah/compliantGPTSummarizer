import streamlit as st
import streamlit.components.v1 as components
import privateGPT as pGPT

st.set_page_config(
    page_title="Private GPT",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="collapsed"
)


st.title("CompliantGPT")
st.button("Click to summarize your emails in source documents.")

