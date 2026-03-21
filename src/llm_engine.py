from groq import Groq
import streamlit as stg
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)
