# app.py  (NEW OPENAI v1.x VERSION / FIXED)

import os
import streamlit as st
import pandas as pd
from agent import SocialMediaAgent
from utils import save_csv

st.set_page_config(page_title="Social Media Agent", layout="wide")
st.title("AI Social Media Agent (New OpenAI API)")

# Sidebar
st.sidebar.header("Settings")
api_key = st.sidebar.text_input("OpenAI API Key", type="password")
if api_key:
    os.environ["OPENAI_API_KEY"] = api_key

# FIXED: Added index=0 so Streamlit works without errors
model = st.sidebar.selectbox(
    "Model",
    ["gpt-4o-mini", "gpt-4o", "gpt-4o-mini-instruct"],
    index=0
)

temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7)
num_ideas = st.sidebar.slider("Ideas", 1, 10, 5)

with st.form("inputs"):
    st.header("Campaign Info")
    brand_name = st.text_input("Brand Name", "Acme Co.")
    brand_voice = st.text_area("Brand Voice", "Friendly and helpful")
    audience = st.text_input("Audience", "Young adults 18–30")
    campaign_goal = st.text_input("Goal", "Improve engagement")
    platforms = st.multiselect(
        "Platforms",
        ["Instagram", "X / Twitter", "LinkedIn"],
        default=["Instagram"]
    )
    start_date = st.date_input("Start Date")
    end_date = st.date_input("End Date")
