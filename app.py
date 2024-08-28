import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
from datetime import datetime

# Set the title of the app
st.title('Stock Candlestick Chart Application')

# Create two columns: one for inputs and one for the chart
col1, col2 = st.columns([1, 4])

# Input fields in the left column
with col1:
    symbol = st.text_input("Enter Stock Symbol (e.g., BHEL.NS)", "RELIANCE.NS")
    start_date = st.date_input("Start Date", datetime(2023, 1, 1))
    end_date = st.date_input("End Date", datetime.today())
    timeframe = st.selectbox("Select Timeframe", ["1m", "5m", "15m", "60m", "1d", "1wk", "1mo"], index=4)
    generate_chart = st.button("Get Charts")

# Chart display in the right column
with col2:
    if generate_chart:
        # Fetch the stock data
        data = yf.download(symbol, start=start_date, end=end_date, interval=timeframe)

        # Check if the data is not empty
        if not data.empty:
            # Plotting candlestick chart with dark theme and category mode for x-axis
            fig = go.Figure(data=[go.Candlestick(x=data.index,
                                                 open=data['Open'],
                                                 high=data['High'],
                                                 low=data['Low'],
                                                 close=data['Close'])])

            fig.update_layout(title=f'Candlestick chart for {symbol}',
                              xaxis_title='Date',
                              yaxis_title='Price',
                              xaxis_rangeslider_visible=False,
                              template='plotly_dark',
                              xaxis_type='category',  # Set x-axis to category mode to remove gaps
                              xaxis=dict(
                                  nticks=10  # Reduce the number of x-axis labels to 10 ticks
                              ))

            # Display the chart
            st.plotly_chart(fig, use_container_width=False)  # Enforce the exact chart size
        else:
            st.write("No data available for the selected dates.")