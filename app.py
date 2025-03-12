import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Scouting & Recruitment Dashboard", layout="wide")

# App title
st.title("Scouting & Recruitment Dashboard")
st.write("Welcome to the scouting and recruitment dashboard. This tool is designed to analyse football player statistics for scouting purposes.")

# Sidebar for future filters
st.sidebar.header("Filters")

# Load Data Function with Updated Caching
@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

# Update file path
file_path = "top5-players.csv"
data = load_data(file_path)

# Display Data
st.subheader("Player Statistics")
st.dataframe(data)
