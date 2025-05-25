import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
os.chdir(os.path.dirname(__file__))

# Stock tickers
tickers = ["GOOGL", "MSFT", "META", "AAPL", "AMZN"]

# Download data
data = {}
for ticker in tickers:
    data[ticker] = yf.download(ticker, start="2024-01-01", end="2025-01-01")['Close']

# Calculate average closing prices
average_close = {}
for ticker in tickers:
    average_close[ticker] = data[ticker].mean()

# Convert average close prices to DataFrame
average_close_df = pd.DataFrame(list(average_close.items()), columns=['Company', 'Average_Close'])

# Display the DataFrame
print(average_close_df)

# Find the company and date with the highest closing price in 2024
max_close_info = {}  
for ticker in tickers:
    max_price = data[ticker].max()
    max_date = data[ticker].idxmax()
    max_close_info[ticker] = {'Max Price': max_price, 'Date': max_date}

# Display results
max_close_df = pd.DataFrame(max_close_info).T
print(max_close_df)

# Calculate percentage change
returns = {}
for ticker in tickers:
    first_price = data[ticker].iloc[0]
    last_price = data[ticker].iloc[-1]
    pct_change = ((last_price - first_price) / first_price) * 100
    returns[ticker] = {
        'First Price': first_price,
        'Last Price': last_price,
        'Percent Change': pct_change}
    
returns_df = pd.DataFrame(returns).T
print(returns_df)  

# Find the best performing company
if not returns_df.empty:
    returns_df['Percent Change'] = returns_df['Percent Change'].apply(
    lambda x: float(x.iloc[0]) if isinstance(x, pd.Series) else float(x)
)
    best_investment = returns_df['Percent Change'].idxmax()
    best_return = returns_df.loc[best_investment, 'Percent Change']
    print(f"Top performing company: {best_investment} ({best_return:.2f}%)")
else:
    print("No stock data found or DataFrame is empty.")

# 1-month moving average chart
plt.figure(figsize=(18, 10))

for ticker in tickers:
    moving_avg = data[ticker].rolling(window=21).mean()
    plt.plot(moving_avg, label=f'{ticker} 1-Month MA')

plt.title('1-Month Moving Averages for 2024')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.legend(fontsize=14)
plt.grid(True)

# Maximize the window
manager = plt.get_current_fig_manager()
try:
    manager.window.showMaximized()
except AttributeError:
    try:
        manager.full_screen_toggle()
    except:
        pass

plt.show()

# Combine all closing prices into one DataFrame
combined_data = pd.concat(data, axis=1)
combined_data.columns = tickers

# Correlation matrix
corr_matrix = combined_data.corr()
print(corr_matrix)

# Evaluation function
def evaluate(corr_matrix):
    print("\nEvaluation Results:\n")
    print("The diagonal values in the correlation matrix indicate a perfect correlation (1.0) of each company with itself.\n")
    print("Below is a detailed interpretation of the closing price correlations between companies:\n")
    
    tickers = corr_matrix.columns
    n = len(tickers)
    
    for i in range(n):
        for j in range(i+1, n):
            corr_value = corr_matrix.iloc[i, j]
            company_1 = tickers[i]
            company_2 = tickers[j]
            
            if corr_value >= 0.9:
                comment = (f"There is a very strong positive correlation ({corr_value*100:.1f}%) between {company_1} and {company_2}. "
                           "This means their stock prices usually move in the same direction and at similar rates.")
            elif corr_value >= 0.75:
                comment = (f"There is a high level of positive correlation ({corr_value*100:.1f}%) between {company_1} and {company_2}, "
                           "indicating similar responses to market conditions.")
            elif corr_value >= 0.5:
                comment = (f"There is a moderate positive correlation ({corr_value*100:.1f}%) between {company_1} and {company_2}. "
                           "They often show parallel price movements.")
            elif corr_value >= 0.3:
                comment = (f"There is a weak positive correlation ({corr_value*100:.1f}%) between {company_1} and {company_2}. "
                           "They sometimes move similarly, but the relationship is not strong.")
            elif corr_value > -0.3:
                comment = (f"The correlation between {company_1} and {company_2} is neutral or very weak ({corr_value*100:.1f}%). "
                           "Their price movements are mostly independent.")
            elif corr_value > -0.5:
                comment = (f"There is a weak negative correlation ({corr_value*100:.1f}%) between {company_1} and {company_2}. "
                           "When one price increases, the other tends to decrease slightly.")
            elif corr_value > -0.75:
                comment = (f"There is a moderate negative correlation ({corr_value*100:.1f}%) between {company_1} and {company_2}. "
                           "Their price movements often go in opposite directions.")
            else:
                comment = (f"There is a very strong negative correlation ({corr_value*100:.1f}%) between {company_1} and {company_2}. "
                           "One typically rises while the other falls, indicating a significant contrast in market dynamics.")
            
            print(f"- {comment}\n")
    
    print("Overall, various levels of positive and negative correlations are observed among the stock prices of companies in the technology sector.")
    print("These relationships are influenced by sector dynamics, common market conditions, and investor behavior.\n")

evaluate(corr_matrix)

input("Press Enter to exit...")