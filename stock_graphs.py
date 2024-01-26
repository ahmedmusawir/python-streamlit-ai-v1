import yfinance as yf
import streamlit as st
import pandas as pd

# App Title
st.write("""
# Simple Stock Price Graphs App
Shown are the stock closing price and volumes

""")

# Define stock symbols and names
stocks = {
    'Google': 'GOOGL',
    'Meta': 'META',
    'Amazon': 'AMZN',
    'Microsoft': 'MSFT'
}

# Dropdown for stock selection
selected_stock_name = st.selectbox('Select a stock', list(stocks.keys()))
tickerSymbol = stocks[selected_stock_name]

#Display the chosen stock in the header
st.write(f"### {selected_stock_name} Stocks ({tickerSymbol})")

# Gettting the data on the ticker
tickerData = yf.Ticker(tickerSymbol)

#getting the historical prices
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

st.line_chart(tickerDf.Close)

st.line_chart(tickerDf.Volume)


