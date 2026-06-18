import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.title("📅 Trend Analysis")

df = pd.read_csv(
"Astram event data_anonymized - Astram event data_anonymizedb40ac87.csv"
)

df['start_datetime'] = pd.to_datetime(
    df['start_datetime'],
    errors='coerce'
)

df['hour'] = df['start_datetime'].dt.hour

df['month'] = df['start_datetime'].dt.month

hour_counts = (
    df.groupby('hour')
    .size()
    .reset_index(name='Events')
)

fig = px.line(
    hour_counts,
    x='hour',
    y='Events',
    title="Events by Hour"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

month_counts = (
    df.groupby('month')
    .size()
    .reset_index(name='Events')
)

fig = px.bar(
    month_counts,
    x='month',
    y='Events',
    title="Events by Month"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
