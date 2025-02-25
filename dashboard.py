import pandas as pd
import streamlit as st

# Load the Excel file
df = pd.read_excel("Baggae testing.xlsx", sheet_name="Testing", skiprows=4)

# Keep only relevant columns
df = df[["Airlines", "Route", "Cabin", "Cabin Baggage (TAW)", "Checked Baggage (TAW)"]].dropna()

# Title
st.title("\U0001F6EB Airline Baggage Rules Interactive Dashboard")

# Dropdown for airline selection
airline = st.selectbox("Select an Airline", df["Airlines"].unique())

# Filter routes based on selected airline
routes = df[df["Airlines"] == airline]["Route"].unique()
route = st.selectbox("Select a Route", routes)

# Filter cabin brands based on selected route
cabins = df[(df["Airlines"] == airline) & (df["Route"] == route)]["Cabin"].unique()
cabin = st.selectbox("Select a Cabin Brand", cabins)

# Display baggage details
row = df[(df["Airlines"] == airline) & (df["Route"] == route) & (df["Cabin"] == cabin)]
if not row.empty:
    st.write(f"**Cabin Baggage:** {row.iloc[0]['Cabin Baggage (TAW)']}")
    st.write(f"**Checked Baggage:** {row.iloc[0]['Checked Baggage (TAW)']}")
else:
    st.write("No data available.")
