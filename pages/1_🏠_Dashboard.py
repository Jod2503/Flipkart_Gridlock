import streamlit as st
import pandas as pd
import plotly.express as px

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* Main title */
h1 {
    font-size: 42px !important;
    font-weight: 700 !important;
    color: #0F172A;
}

/* Section titles */
h2 {
    font-size: 30px !important;
    font-weight: 700 !important;
    color: #1E293B;
}

h3 {
    font-size: 24px !important;
    font-weight: 600 !important;
    color: #334155;
}

/* General text */
p, label {
    font-size: 17px !important;
    font-weight: 500 !important;
}

/* Metric cards */
div[data-testid="stMetric"] {
    background-color: white;
    border: 1px solid #E2E8F0;
    padding: 22px;
    border-radius: 18px;
    box-shadow: 0px 3px 10px rgba(0,0,0,0.06);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #EEF2FF;
}

/* Buttons */
div.stButton > button {
    background-color: #0F766E;
    color: white;
    border-radius: 14px;
    border: none;
    height: 3.2em;
    font-size: 17px;
    font-weight: 600;
}

/* Inputs */
div[data-baseweb="select"] {
    border-radius: 10px;
}

/* Dataframes */
thead tr th {
    font-size: 16px !important;
}

/* Tabs */
button[data-baseweb="tab"] {
    font-size: 16px;
    font-weight: 600;
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
