import streamlit as st
import pandas as pd
import plotly.express as px

import streamlit as st
from style import local_css

st.set_page_config(layout="wide")

local_css()

st.title("Traffic Risk Prediction")
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
