import streamlit as st

def local_css():
    st.markdown("""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    h1 {
        font-size: 42px !important;
        font-weight: 800 !important;
    }

    h2 {
        font-size: 30px !important;
        font-weight: 700 !important;
    }

    p, label {
        font-size: 16px !important;
    }

    div[data-testid="stMetric"] {
        background-color: white;
        border: 1px solid #E5E7EB;
        padding: 22px;
        border-radius: 16px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }

    div.stButton > button {
        background-color: #B91C1C;
        color: white;
        border-radius: 12px;
        border: none;
        height: 3em;
        font-size: 16px;
        font-weight: 600;
    }

    </style>
    """, unsafe_allow_html=True)
