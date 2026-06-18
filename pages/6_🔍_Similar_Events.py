import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import NearestNeighbors

st.set_page_config(layout="wide")

st.title("Similar Event Search")

df = pd.read_csv(
    "Astram event data_anonymized - Astram event data_anonymizedb40ac87.csv"
)

cols = ['event_type', 'event_cause', 'zone']

for col in cols:
    df[col] = df[col].fillna("Unknown")

encoders = {}

for col in cols:
    encoders[col] = LabelEncoder()
    df[col] = encoders[col].fit_transform(df[col])

X = df[cols]

nn = NearestNeighbors(n_neighbors=5)

nn.fit(X)

event_type = st.selectbox(
    "Event Type",
    encoders['event_type'].classes_
)

event_cause = st.selectbox(
    "Event Cause",
    encoders['event_cause'].classes_
)

zone = st.selectbox(
    "Zone",
    encoders['zone'].classes_
)

sample = pd.DataFrame({

'event_type':[encoders['event_type'].transform([event_type])[0]],
'event_cause':[encoders['event_cause'].transform([event_cause])[0]],
'zone':[encoders['zone'].transform([zone])[0]]

})

if st.button("Find Similar Events"):

    distances, indices = nn.kneighbors(sample)

    st.subheader("Top 5 Similar Historical Events")

    st.dataframe(
        df.iloc[indices[0]],
        use_container_width=True
    )
