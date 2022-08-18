import streamlit as st
import yfinance as yf
import pandas as pd

data = yf.download("AMZN", start="2021-01-01", end="2022-08-17")

chart_data = pd.DataFrame(data.Close)

st.line_chart(chart_data)