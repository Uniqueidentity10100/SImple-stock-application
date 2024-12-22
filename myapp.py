import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App
 """)

tickerSymbol="AAPL"
tickerdata=yf.Ticker(tickerSymbol)
tickerDf=tickerdata.history(period='1d',start='2014-12-20',end='2024-12-20')

st.write("""
### Close Price
 """)
st.line_chart(tickerDf.Close)
st.write("""
### Volume Price
 """)
st.line_chart(tickerDf.Volume)
