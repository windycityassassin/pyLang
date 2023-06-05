# author: apv
# date: 23/5/23
# purpose: Data Analytics applied to the Stock Problem

import pandas as pd
import matplotlib.pyplot as plt

# Defining file paths for each stock
file_paths = {
    'SPY': r'/Users/apv/PycharmProjects/ICT 4370/week9/Data/AIG.csv',
    'AIG': r'/Users/apv/PycharmProjects/ICT 4370/week9/Data/AIG.csv',
    'F': r'/Users/apv/PycharmProjects/ICT 4370/week9/Data/AIG.csv',
    'FB': r'/Users/apv/PycharmProjects/ICT 4370/week9/Data/AIG.csv',
    'GOOG': r'/Users/apv/PycharmProjects/ICT 4370/week9/Data/AIG.csv',
    'IBM': r'/Users/apv/PycharmProjects/ICT 4370/week9/Data/AIG.csv',
    'M': r'/Users/apv/PycharmProjects/ICT 4370/week9/Data/AIG.csv',
    'MSFT': r'/Users/apv/PycharmProjects/ICT 4370/week9/Data/AIG.csv',
    'RDS': r'/Users/apv/PycharmProjects/ICT 4370/week9/Data/AIG.csv'
}

data_frames = {}  # Dictionary to store stock data frames

try:
    # Reading each file into a data frame
    for stock, file_path in file_paths.items():
        data_frames[stock] = pd.read_csv(file_path)
        data_frames[stock]['Date'] = pd.to_datetime(data_frames[stock]['Date'])  # Convert 'Date' to datetime format

        # Calculating average stock prices
    for stock, df in data_frames.items():
        average_price = df['Close'].mean()
        print(f"{stock} average: {average_price}")

    print("\n")

    # Calculating standard deviations
    for stock, df in data_frames.items():
        std_deviation = df['Close'].std()
        print(f"{stock} standard deviation: {std_deviation}")

    print("\n")

    # Calculating correlation coefficients
    for stock, df in data_frames.items():
        correlation = df['Close'].corr(data_frames['SPY']['Close'])
        print(f"{stock} correlation: {correlation}")

        # Plotting stock prices
        plt.figure(figsize=(10, 6))
    for stock, df in data_frames.items():
        plt.plot(df['Date'], df['Close'], label=stock)

        plt.title('Stock Data')
        plt.xlabel('Date')
        plt.ylabel('Value')
        plt.legend()
        plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
        plt.show()

except Exception as e:
    print(f"An error occurred: {str(e)}")
