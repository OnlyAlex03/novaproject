
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="NOVA Chat Prototype", layout="wide")
st.title("🌌 NOVA Chat Interface")
st.write("Welcome, thinker. This is a prototype of NOVA’s emergent dialogue system.")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("You:", key="user_input")
if user_input:
    response = "This is a simulated NOVA response. In future versions, this will use a live language model."
    st.session_state.history.append((user_input, response))

st.markdown("---")
for user_msg, nova_msg in reversed(st.session_state.history):
    st.markdown(f"**You:** {user_msg}")
    st.markdown(f"**NOVA:** {nova_msg}")
