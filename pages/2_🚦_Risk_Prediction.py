import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

model=joblib.load("risk_classifier.pkl")
import plot_theme
st.title("🚦 Risk Prediction")

lat=st.number_input(
"Latitude",
value=12.97
)

lon=st.number_input(
"Longitude",
value=77.59
)

hour=st.slider(
"Hour",
0,
23,
8
)

event_type=st.selectbox(
"Event Type",
[
"planned",
"unplanned"
]
)

event_cause=st.text_input(
"Event Cause",
"value"
)

if st.button("Predict"):

    X=pd.DataFrame({

'latitude':[lat],
'longitude':[lon],

'hour':[hour],
'dayofweek':[2],
'month':[7],

'is_peak_hour':[1],
'is_weekend':[0],

'event_type':[event_type],
'event_cause':[event_cause],

'priority':['medium'],

'requires_road_closure':[0],

'zone':['Unknown'],
'junction':['Unknown'],
'corridor':['Unknown'],
'police_station':['Unknown'],

'cluster':[0],

'junction_event_count':[10],
'cause_frequency':[10],

'zone_event_count':[15],
'cluster_event_count':[10]

})

    pred = str(model.predict(X)[0]).strip()

    probs=model.predict_proba(X)[0]

    classes=model.classes_

    st.success(
        f"Predicted Risk : {pred}"
    )

    prob_df=pd.DataFrame({

        "Risk Level":classes,
        "Probability":probs

    })

    fig=px.bar(
        prob_df,
        x="Risk Level",
        y="Probability"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    resource_map={

        "Low":(2,1),
        "Medium":(5,3),
        "High":(10,6),
        "Critical":(15,10)

    }

    officers,barricades=resource_map[pred]

    c1,c2=st.columns(2)

    c1.metric(
        "Police Officers",
        officers
    )

    c2.metric(
        "Barricades",
        barricades
    )
