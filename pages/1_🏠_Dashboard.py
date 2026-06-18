import streamlit as st
import pandas as pd
import plotly.express as px

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'IBM Plex Sans', sans-serif;
}

/* Main title */
h1 {
    font-size: 42px !important;
    font-weight: 700 !important;
    color: #111827;
    letter-spacing: -1px;
}

/* Section titles */
h2 {
    font-size: 30px !important;
    font-weight: 700 !important;
    color: #1F2937;
}

h3 {
    font-size: 24px !important;
    font-weight: 600 !important;
    color: #374151;
}

/* General text */
p, label, div {
    font-size: 16px !important;
    font-weight: 500;
}

/* Metric cards */
div[data-testid="stMetric"] {
    background-color: white;
    border: 1px solid #E5E7EB;
    padding: 22px;
    border-radius: 16px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}

/* Buttons */
div.stButton > button {
    background-color: #0F766E;
    color: white;
    font-size: 16px;
    font-weight: 600;
    border-radius: 12px;
    border: none;
    height: 3.1em;
}

</style>
""", unsafe_allow_html=True)
st.set_page_config(layout="wide")

df = pd.read_csv(
"Astram event data_anonymized - Astram event data_anonymizedb40ac87.csv"
)

st.title("Dashboard")

c1,c2,c3,c4=st.columns(4)

c1.metric(
"Total Events",
len(df)
)

c2.metric(
"Zones",
df['zone'].nunique()
)

c3.metric(
"Police Stations",
df['police_station'].nunique()
)

c4.metric(
"Corridors",
df['corridor'].nunique()
)

st.subheader("Top Event Causes")

cause_counts=df['event_cause'].value_counts().head(10)

fig=px.bar(
x=cause_counts.index,
y=cause_counts.values,
labels={'x':'Cause','y':'Count'}
)

st.plotly_chart(
fig,
use_container_width=True
)

col1,col2=st.columns(2)

with col1:

    st.subheader("Top Corridors")

    corridor_counts=df['corridor'].value_counts().head(10)

    fig=px.bar(
        x=corridor_counts.values,
        y=corridor_counts.index,
        orientation='h'
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:

    st.subheader("Top Police Stations")

    station_counts=df['police_station'].value_counts().head(10)

    fig=px.bar(
        x=station_counts.values,
        y=station_counts.index,
        orientation='h'
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
