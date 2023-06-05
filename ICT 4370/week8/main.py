import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the stocks portfolio data from a CSV file
df_stocks = pd.read_csv('Lesson6_Data_Stocks.csv')

# Read the market data from a JSON file
df_market = pd.read_json('AllStocks.json')

# Merge the stocks portfolio data with the market data on the symbol column
df_merged = pd.merge(df_market, df_stocks, left_on='Symbol', right_on='SYMBOL', how='inner')

# Convert the 'Close' column to numeric type
df_merged['Close'] = pd.to_numeric(df_merged['Close'], errors='coerce')

# Calculate the stock day value by multiplying the 'Close' price with the number of shares
df_merged['Stock Day Value'] = df_merged['Close'] * df_merged['NO_SHARES']

# Sort the merged data by date in ascending order
df_merged = df_merged.sort_values('Date')

# Create a line chart to visualize the trend of Bob's stocks performance over time
plt.figure(figsize=(12, 8))
for symbol in df_merged['Symbol'].unique():
    df = df_merged[df_merged['Symbol'] == symbol]
    plt.plot(df['Date'], df['Stock Day Value'], label=symbol)

plt.xlabel('Date')
plt.ylabel('Stock Day Value')
plt.title('Stock Day Value over Time')
plt.legend()

# Save the chart as an image file
plt.savefig('Stock_Performance.png')

# Show the chart
plt.show()
