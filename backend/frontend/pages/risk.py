import streamlit as st
import requests

st.title("⚠ Risks")

data = requests.get(
    "http://127.0.0.1:8000/api/v1/risk-board"
).json()

st.subheader("🔴 High")

for risk in data["high"]:
    st.error(risk["title"])

st.subheader("🟠 Medium")

for risk in data["medium"]:
    st.warning(risk["title"])

st.subheader("🟢 Low")

for risk in data["low"]:
    st.success(risk["title"])