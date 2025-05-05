import streamlit as st
from data import crawl_data

st.set_page_config(layout="wide")
st.title("Reddit data from r/MachineLearning")

limit = st.number_input(
    "Number of posts:",
    min_value=1,
    max_value=1000,
    value=100,
    step=1
)

df = crawl_data(limit)
st.dataframe(df, use_container_width=True)

csv_data = df.to_csv(index=False)
st.download_button(
    label="Download CSV",
    data=csv_data,
    file_name="reddit_data.csv",
    mime="text/csv"
)