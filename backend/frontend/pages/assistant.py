import streamlit as st
import requests

st.title("💬 CHIPI Assistant")

st.caption(
    "Consulta acciones, documentos y actividad."
)

question = st.text_input(
    "Preguntá a CHIPI"
)

if st.button("Enviar"):

    response = requests.post(
        "http://127.0.0.1:8000/api/v1/assistant",
        json={
            "question": question
        }
    )

    data = response.json()

    st.success(
        data["answer"]
    )

    for item in data["details"]:
        st.write(
            f"• {item}"
        )