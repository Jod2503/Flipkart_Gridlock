import streamlit as st
import pandas as pd
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium

st.set_page_config(layout="wide")

st.title("🔥 Congestion Hotspot Heatmap")

df = pd.read_csv(
    "Astram event data_anonymized - Astram event data_anonymizedb40ac87.csv"
)

df = df.dropna(subset=['latitude', 'longitude'])

m = folium.Map(
    location=[12.97, 77.59],
    zoom_start=11
)

heat_data = df[['latitude', 'longitude']].values.tolist()

HeatMap(
    heat_data,
    radius=15,
    blur=10
).add_to(m)

st_folium(
    m,
    width=1400,
    height=700
)
