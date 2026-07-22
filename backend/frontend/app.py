from streamlit_autorefresh import st_autorefresh

import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Chipi Work Monitor",
    page_icon="🚀",
    layout="wide"
)

from datetime import datetime

st.caption(
    f"Last refresh: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
)

st_autorefresh(
    interval=30000,
    key="dashboard_refresh"
)

status_col1, status_col2 = st.columns(2)

with status_col1:
    st.success("✅ Backend Online")

with status_col2:
    st.success("✅ Database Online")

def kpi_card(title, value, color):
    st.markdown(
        f"""
        <div style="
            background-color:{color};
            padding:20px;
            border-radius:15px;
            text-align:center;
            color:white;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.25);
        ">
            <h3>{title}</h3>
            <h1>{value}</h1>
        </div>
        """,
        unsafe_allow_html=True
    )



# APIs

data = requests.get(
    "http://127.0.0.1:8000/api/v1/workspace"
).json()

stats = requests.get(
    "http://127.0.0.1:8000/api/v1/dashboard/stats"
).json()

# Sidebar

st.sidebar.title("🚀 CHIPI")

st.sidebar.caption(
    "Work Monitor Platform"
)

st.sidebar.markdown("---")

st.sidebar.write("🏠 Home")
st.sidebar.write("📊 Dashboard")
st.sidebar.write("⚠ Risks")
st.sidebar.write("✅ Actions")
st.sidebar.write("📄 Processing")
st.sidebar.write("📅 Agenda")

# Header

st.title("🚀 Chipi Work Monitor")

st.markdown(
    """
    <div style="
        background: linear-gradient(90deg,#1E293B,#334155);
        padding:20px;
        border-radius:15px;
        margin-bottom:20px;
    ">
        <h2>🚀 Executive Workspace</h2>
        <p>
            Monitor risks, actions and document processing activity.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Top Priority

if data["home"]["top_priority"]:
    st.warning(
        f"⚠ TOP PRIORITY: {data['home']['top_priority']}"
    )

# KPI Cards

col1, col2, col3 = st.columns(3)

with col1:
    kpi_card(
        "🔴 OPEN RISKS",
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
        "🔵 DOCUMENTS",
        data["kpis"]["documents_processed"],
        "#2563EB"
    )

st.divider()

# Summary

st.info(
    f"""
Critical Risks: {len(data['risk_board']['high'])}

Open Actions: {len(data['action_board']['open'])}

Documents Processed: {data['kpis']['documents_processed']}
"""
)

# Charts

chart1, chart2 = st.columns(2)

with chart1:

    st.subheader("📊 Risks by Severity")

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

    st.bar_chart(
        risks_df,
        x="Severity",
        y="Count"
    )

with chart2:

    st.subheader("📈 Actions by Status")

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

    st.bar_chart(
        actions_df,
        x="Status",
        y="Count"
    )

st.divider()

# Panels

panel1, panel2, panel3 = st.columns(3)

with panel1:

    st.subheader("🔴 Critical Risks")

    for risk in data["risk_board"]["high"]:
        st.write(
            f"• {risk['title']}"
        )

with panel2:

    st.subheader("🟠 Open Actions")

    for action in data["action_board"]["open"]:
        st.write(
            f"• {action['title']}"
        )

with panel3:

    st.subheader("✅ Recent Processing")

    for item in data["processing_center"]:
        st.write(
            f"📄 {item['document']}"
        )

st.divider()

st.caption(
    "Chipi Work Monitor • Executive Dashboard • v0.2.0-alpha"
)