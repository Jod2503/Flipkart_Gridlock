import streamlit as st

st.title("🚓 Resource Planner")

risk = st.selectbox(
    "Risk Level",
    ["Low", "Medium", "High", "Critical"]
)

if risk == "Low":
    officers = 2
    barricades = 1
    diversion = "No"

elif risk == "Medium":
    officers = 5
    barricades = 3
    diversion = "Optional"

elif risk == "High":
    officers = 10
    barricades = 6
    diversion = "Recommended"

else:
    officers = 15
    barricades = 10
    diversion = "Mandatory"

c1, c2, c3 = st.columns(3)

c1.metric(
    "Police Officers",
    officers
)

c2.metric(
    "Barricades",
    barricades
)

c3.metric(
    "Diversion Needed",
    diversion
)

st.subheader("Deployment Recommendation")

st.success(
f"""
Deploy {officers} officers.

Install {barricades} barricades.

Diversion Status : {diversion}
"""
)
