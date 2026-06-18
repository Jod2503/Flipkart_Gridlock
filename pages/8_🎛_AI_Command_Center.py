import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(layout="wide")

st.title("🎛 AI Command Center")

df = pd.read_csv(
"Astram event data_anonymized - Astram event data_anonymizedb40ac87.csv"
)

total_events = len(df)

top_corridor = (
    df['corridor']
    .value_counts()
    .index[0]
)

top_station = (
    df['police_station']
    .value_counts()
    .index[0]
)

peak_zone = (
    df['zone']
    .value_counts()
    .index[0]
)

c1,c2,c3,c4 = st.columns(4)

c1.metric(
    "Total Events",
    total_events
)

c2.metric(
    "Top Corridor",
    top_corridor
)

c3.metric(
    "Top Station",
    top_station
)

c4.metric(
    "Peak Zone",
    peak_zone
)

fig = go.Figure(

go.Indicator(

mode="gauge+number",

value=total_events,

title={'text':"Traffic Load"},

gauge={
'axis':{
'range':[0,10000]
}
}

)

)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("Top Event Causes")

st.bar_chart(
    df['event_cause']
    .value_counts()
    .head(10)
)

st.subheader("Top Zones")

st.bar_chart(
    df['zone']
    .value_counts()
    .head(10)
)
