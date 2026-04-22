import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Credit Card Dashboard", layout="wide")

st.title("💳 Credit Card Analytics Dashboard")

# File Upload
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

@st.cache_data
def load_data(file):
    df = pd.read_csv(file)
    return df

# Default synthetic fallback
def generate_sample_data():
    data = {
        "credit_limit": np.random.randint(5000, 50000, 1000),
        "card_type": np.random.choice(["Debit", "Credit"], 1000),
        "card_brand": np.random.choice(["Visa", "Mastercard"], 1000),
        "has_chip": np.random.choice([0, 1], 1000),
        "num_cards_issued": np.random.randint(1, 4, 1000),
        "card_on_dark_web": np.random.choice([0, 1], 1000)
    }
    return pd.DataFrame(data)

if uploaded_file:
    df = load_data(uploaded_file)
else:
    st.warning("No file uploaded. Using sample data.")
    df = generate_sample_data()

st.session_state["data"] = df

st.write("### Dataset Preview")
st.dataframe(df.head())

st.write("### Basic Info")
st.write(df.describe())

st.success("Use the sidebar to navigate to EDA, Visualization, and Prediction 🚀")