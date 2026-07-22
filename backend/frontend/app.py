import streamlit as st
import requests
import pandas as pd
import plotly.express as px

from datetime import datetime
from streamlit_autorefresh import st_autorefresh

# --------------------------------------------------
# Config
# --------------------------------------------------

st.set_page_config(
    page_title="Chipi Work Monitor",
    page_icon="🚀",
    layout="wide"
)

st_autorefresh(
    interval=30000,
    key="dashboard_refresh"
)

# --------------------------------------------------
# Helpers
# --------------------------------------------------

def kpi_card(title, value, color):

    st.markdown(
        f"""
        <div style="
            background-color:{color};
            padding:20px;
            border-radius:15px;
            text-align:center;
            color:white;
            box-shadow:0px 4px 12px rgba(0,0,0,0.25);
        ">
            <h3>{title}</h3>
            <h1>{value}</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.title("🚀 CHIPI")

st.sidebar.caption(
    "Work Monitor Platform"
)

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    [
        "📊 Dashboard",
        "💬 Assistant"
    ]
)

# --------------------------------------------------
# Assistant
# --------------------------------------------------

if page == "💬 Assistant":

    st.title("💬 CHIPI Assistant")

    st.caption(
        "Consultá acciones y documentos."
    )

    if "question" not in st.session_state:
        st.session_state.question = ""

    if "messages" not in st.session_state:
        st.session_state.messages = []

    st.subheader("Preguntas sugeridas")

    c1, c2 = st.columns(2)

    with c1:

        if st.button("✅ Acciones abiertas"):
            st.session_state.question = (
                "acciones abiertas"
            )

        if st.button("📄 Documentos procesados"):
            st.session_state.question = (
                "documentos procesados"
            )

    with c2:

        if st.button("✅ Acciones completadas"):
            st.session_state.question = (
                "acciones completadas"
            )

        if st.button("📄 Último documento"):
            st.session_state.question = (
                "ultimo documento"
            )

    question = st.text_input(
        "Preguntá a CHIPI",
        value=st.session_state.question
    )

    if st.button("Enviar"):

        response = requests.post(
            "http://127.0.0.1:8000/api/v1/assistant",
            json={
                "question": question
            }
        )

        assistant_data = response.json()

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": assistant_data["answer"],
                "details": assistant_data.get(
                    "details",
                    []
                )
            }
        )

    st.divider()

    for msg in st.session_state.messages:

        if msg["role"] == "user":

            with st.chat_message("user"):
                st.write(
                    msg["content"]
                )

        else:

            with st.chat_message("assistant"):

                st.write(
                    msg["content"]
                )

                for item in msg["details"]:
                    st.write(
                        f"• {item}"
                    )
# --------------------------------------------------
# Dashboard
# --------------------------------------------------

else:

    data = requests.get(
        "http://127.0.0.1:8000/api/v1/workspace"
    ).json()

    stats = requests.get(
        "http://127.0.0.1:8000/api/v1/dashboard/stats"
    ).json()

    st.caption(
        f"Last refresh: "
        f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
    )

    status_col1, status_col2 = st.columns(2)

    with status_col1:
        st.success("✅ Backend Online")

    with status_col2:
        st.success("✅ Database Online")

    st.title("🚀 Chipi Work Monitor")

    st.markdown(
        """
        <div style="
            background: linear-gradient(
                90deg,
                #1E293B,
                #334155
            );
            padding:20px;
            border-radius:15px;
            margin-bottom:20px;
        ">
            <h2>🚀 Executive Workspace</h2>
            <p>
                Monitor actions and document processing activity.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    if data["home"]["top_priority"]:

        st.warning(
            f"⚠ TOP PRIORITY: "
            f"{data['home']['top_priority']}"
        )

    col1, col2, col3 = st.columns(3)

    with col1:

        kpi_card(
            "🔴 CRITICAL ACTIONS",
            data["kpis"]["open_risks"],
            "#DC2626"
        )

    with col2:

        kpi_card(
            "🟠 OPEN ACTIONS",
            data["kpis"]["open_actions"],
            "#EA580C"
        )

    with col3:

        kpi_card(
            "📄 DOCUMENTS",
            data["kpis"]["documents_processed"],
            "#2563EB"
        )

    st.divider()

    risks_df = pd.DataFrame(
        {
            "Severity": [
                "HIGH",
                "MEDIUM",
                "LOW"
            ],
            "Count": [
                stats["risks"]["HIGH"],
                stats["risks"]["MEDIUM"],
                stats["risks"]["LOW"]
            ]
        }
    )

    actions_df = pd.DataFrame(
        {
            "Status": [
                "OPEN",
                "IN_PROGRESS",
                "DONE"
            ],
            "Count": [
                stats["actions"]["OPEN"],
                stats["actions"]["IN_PROGRESS"],
                stats["actions"]["DONE"]
            ]
        }
    )

    chart1, chart2 = st.columns(2)

    with chart1:

        fig_risks = px.pie(
            risks_df,
            values="Count",
            names="Severity",
            hole=0.6,
            title="Actions Priority Distribution"
        )

        st.plotly_chart(
            fig_risks,
            use_container_width=True
        )

    with chart2:

        fig_actions = px.pie(
            actions_df,
            values="Count",
            names="Status",
            hole=0.6,
            title="Actions Status Distribution"
        )

        st.plotly_chart(
            fig_actions,
            use_container_width=True
        )

    st.divider()

    panel1, panel2 = st.columns(2)

    with panel1:

        st.subheader("🟠 Open Actions")

        for action in data["action_board"]["open"]:
            st.write(
                f"• {action['title']}"
            )

    with panel2:

        st.subheader("✅ Recent Processing")

        for item in data["processing_center"]:
            st.write(
                f"📄 {item['document']}"
            )

    st.divider()

    st.caption(
        "CHIPI • Operational Intelligence Assistant • v0.3.0-alpha"
    )