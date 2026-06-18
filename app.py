
import streamlit as st
import streamlit as st
import pandas as pd
import joblib

# ===================================
# LOAD
# ===================================

model = joblib.load("risk_classifier.pkl")

df = pd.read_csv(
    "Astram event data_anonymized - Astram event data_anonymizedb40ac87.csv"
)

# ===================================
# TITLE
# ===================================

st.title("🚦 Event Congestion Intelligence System")

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Choose",
    [
        "Risk Prediction",
        "Analytics"
    ]
)

# ===================================
# RISK PREDICTION
# ===================================

if page == "Risk Prediction":

    st.header("Event Risk Prediction")

    event_type = st.selectbox(
        "Event Type",
        sorted(df['event_type'].dropna().unique())
    )

    event_cause = st.selectbox(
        "Event Cause",
        sorted(df['event_cause'].dropna().unique())
    )

    zone = st.selectbox(
        "Zone",
        sorted(df['zone'].fillna('Unknown').unique())
    )

    corridor = st.selectbox(
        "Corridor",
        sorted(df['corridor'].fillna('Unknown').unique())
    )

    police_station = st.selectbox(
        "Police Station",
        sorted(df['police_station'].fillna('Unknown').unique())
    )

    hour = st.slider(
        "Hour",
        0,
        23,
        8
    )

    latitude = st.number_input(
        "Latitude",
        value=12.97
    )

    longitude = st.number_input(
        "Longitude",
        value=77.59
    )

    if st.button("Predict Risk"):

        input_df = pd.DataFrame({

            'latitude':[latitude],
            'longitude':[longitude],

            'hour':[hour],
            'dayofweek':[2],
            'month':[7],

            'is_peak_hour':[1],
            'is_weekend':[0],

            'event_type':[event_type],
            'event_cause':[event_cause],

            'priority':['medium'],

            'requires_road_closure':[0],

            'zone':[zone],
            'junction':['Unknown'],
            'corridor':[corridor],
            'police_station':[police_station],

            'cluster':[0],

            'junction_event_count':[10],
            'cause_frequency':[50],

            'zone_event_count':[100],
            'cluster_event_count':[40]

        })

        prediction = model.predict(input_df)[0]

        st.success(
            f"Predicted Risk Level: {prediction}"
        )

# ===================================
# ANALYTICS
# ===================================

if page == "Analytics":

    st.header("Traffic Analytics")

    st.subheader("Event Cause Distribution")

    st.bar_chart(
        df['event_cause']
        .value_counts()
        .head(10)
    )

    st.subheader("Top Corridors")

    st.bar_chart(
        df['corridor']
        .value_counts()
        .head(10)
    )
