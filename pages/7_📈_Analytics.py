import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.title("Analytics")

df = pd.read_csv(
"Astram event data_anonymized - Astram event data_anonymizedb40ac87.csv"
)

st.subheader("Top Event Causes")

cause_counts = (
    df['event_cause']
    .value_counts()
    .head(10)
)

fig = px.bar(
    x=cause_counts.index,
    y=cause_counts.values,
    labels={
        'x':'Cause',
        'y':'Count'
    }
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("Top Corridors")

corridor_counts = (
    df['corridor']
    .value_counts()
    .head(10)
)

fig = px.bar(
    x=corridor_counts.values,
    y=corridor_counts.index,
    orientation='h'
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("Top Police Stations")

station_counts = (
    df['police_station']
    .value_counts()
    .head(10)
)

fig = px.bar(
    x=station_counts.values,
    y=station_counts.index,
    orientation='h'
)

st.plotly_chart(
    fig,
    use_container_width=True
)
