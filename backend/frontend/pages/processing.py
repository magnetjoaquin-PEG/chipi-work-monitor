import streamlit as st
import requests

st.title("📄 Processing Center")

data = requests.get(
    "http://127.0.0.1:8000/api/v1/processing-center"
).json()

for item in data["recent_documents"]:

    st.success(
        f"{item['document']} | "
        f"Actions: {item['actions_created']} | "
        f"Risks: {item['risks_created']}"
    )