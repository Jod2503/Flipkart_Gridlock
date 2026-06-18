import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.title("Vulnerable Junction Ranking")

df = pd.read_csv(
    "Astram event data_anonymized - Astram event data_anonymizedb40ac87.csv"
)

top_junctions = (
    df.groupby("junction")
    .size()
    .sort_values(ascending=False)
    .head(20)
    .reset_index()
)

top_junctions.columns = ["Junction", "Event Count"]

st.dataframe(
    top_junctions,
    use_container_width=True
)

fig = px.bar(
    top_junctions,
    x="Event Count",
    y="Junction",
    orientation='h',
    title="Top 20 Vulnerable Junctions"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
