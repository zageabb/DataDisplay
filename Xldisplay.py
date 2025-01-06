import streamlit as st
import pandas as pd

st.title("Upload and Read an Excel File 📊")

# File uploader
uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx"])

if uploaded_file is not None:
    # Read the Excel file
    df = pd.read_excel(uploaded_file, engine="openpyxl")
    
    # Display the DataFrame
    st.write("### Data Preview:")
    st.dataframe(df)
