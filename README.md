
# Stock Candlestick Chart Application

This is a simple Streamlit application that allows users to input a stock symbol, start date, end date, and timeframe to generate a candlestick chart using Plotly. The application fetches stock data from Yahoo Finance and displays it in an interactive candlestick chart.

## Features

- **Input Fields:**
  - **Symbol:** Text input for the stock symbol (e.g., AAPL).
  - **Start Date & End Date:** Date pickers to select the range.
  - **Timeframe:** Dropdown to select the timeframe (Daily, Weekly, Monthly).
- **Output:** A candlestick chart generated using Plotly, showing the stock data for the given symbol and date range.

## Installation

To run this application locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/maketcalls/yfinancecharts
   cd yfinancecharts
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

## Dependencies

- Python 3.x
- Streamlit
- yfinance
- Plotly

You can install the dependencies using the `requirements.txt` file:

```txt
streamlit
yfinance
plotly
```

## Usage

- Launch the application using the `streamlit run app.py` command.
- Enter a valid stock symbol (e.g., `AAPL` for Apple Inc.).
- Select the desired start and end dates using the date pickers.
- Choose the timeframe (Daily, Weekly, Monthly) from the dropdown menu.
- Click the "Generate Chart" button to view the candlestick chart.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This application uses data from [Yahoo Finance](https://finance.yahoo.com/).
- Built using [Streamlit](https://streamlit.io/) and [Plotly](https://plotly.com/).
