import streamlit as st
import requests

st.title("✅ Actions")

data = requests.get(
    "http://127.0.0.1:8000/api/v1/action-board"
).json()

st.subheader("🟠 Open")

for item in data["open"]:
    st.write(item["title"])

st.subheader("🔵 In Progress")

for item in data["in_progress"]:
    st.write(item["title"])

st.subheader("✅ Done")

for item in data["done"]:
    st.write(item["title"])