import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
from datetime import datetime

# Set the title of the app
st.title('Stock Candlestick Chart')

# Input fields for the stock symbol, start date, end date, and timeframe
symbol = st.text_input("Enter Stock Symbol (e.g., ^NSEI)", "RELIANCE.NS")
start_date = st.date_input("Start Date", datetime(2023, 1, 1))
end_date = st.date_input("End Date", datetime.today())
timeframe = st.selectbox("Select Timeframe", ["1d", "1wk", "1mo"], index=0)

# Fetching data from yfinance
if st.button("Generate Chart"):
    # Fetch the stock data
    data = yf.download(symbol, start=start_date, end=end_date, interval=timeframe)

    # Check if the data is not empty
    if not data.empty:
        # Plotting candlestick chart
        fig = go.Figure(data=[go.Candlestick(x=data.index,
                                             open=data['Open'],
                                             high=data['High'],
                                             low=data['Low'],
                                             close=data['Close'])])

        fig.update_layout(title=f'Candlestick chart for {symbol}',
                          xaxis_title='Date',
                          yaxis_title='Price (USD)',
                          xaxis_rangeslider_visible=False)

        # Display the chart
        st.plotly_chart(fig)
    else:
        st.write("No data available for the selected dates.")