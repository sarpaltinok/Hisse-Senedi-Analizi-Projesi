# Stock Analysis Project

This project uses Python and various data analysis libraries to analyze stock data for specific technology companies. The project calculates average values, highest closing prices, percentage changes, and correlations of stock prices.

## Libraries Used

- **yfinance:** Used to pull stock data.

- **pandas:** Used for data processing and analysis.

- **numpy:** Used for numerical calculations.

- **matplotlib:** Used for data visualization.

## Project Steps

### 1. Data Fetch
Using the `yfinance` library, the closing prices of Google (GOOGL), Microsoft (MSFT), Meta (META), Apple (AAPL), and Amazon (AMZN) stocks for the year 2024 are pulled.

### 2. Average Closing Prices
The average closing price for each stock throughout the year 2024 is calculated and displayed in a table.

### 3. Highest Closing Price
For each stock, the highest closing price in 2024 and the date on which this price occurred are found.

### 4. Percentage Change
The percentage change between the first and last closing prices of the year is calculated for each stock. The company that gained the most is determined.

### 5. Moving Average
A 1-month (30-day) moving average is calculated for each stock and the moving averages of all companies are shown on the same graph.

### 6. Correlation Matrix
A correlation matrix is ​​calculated using the daily closing prices of all companies. The relationship between price movements is analyzed.

## Results

- **Average Closing Prices:** The average closing prices of each stock throughout 2024 are calculated and presented in a table.
- **Highest Closing Price:** The highest closing price and the date on which this price occurred are determined for each stock.
- **Percentage Change:** The performance of the stocks throughout the year was calculated as a percentage change and the company that made the most profit was determined.

- **Moving Average:** 1-month moving averages were shown on the graph and the trends of the stocks were compared.

- **Correlation Matrix:** The similarity of price movements between stocks was analyzed and interpreted with the correlation matrix.

## How to Run?

Install the necessary libraries:

```bash
pip install yfinance pandas numpy matplotlib
```

Run:

```bash
python analysis.py
```

## Contributing
This project is open source. You can fork it and send a pull request to contribute.

## Project Partners
- [Sarp Altınok](https://github.com/sarpaltinok)
- [Berat](https://github.com/brgkdm)
## License
This project is licensed under the MIT license. For more information, see the LICENSE file.