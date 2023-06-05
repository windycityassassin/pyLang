import json
import pandas as pd
import mplfinance as mpf

try:
    with open("AllStocks.json") as file:
        data = json.load(file)
except FileNotFoundError:
    print('JSON file not found in the directory.')
else:
    # Create a DataFrame from the JSON data
    df = pd.DataFrame(data)

    # Convert the "Date" column to datetime format
    df["Date"] = pd.to_datetime(df["Date"], format="%d-%b-%y")

    # Sort the DataFrame by date in ascending order
    df = df.sort_values(by="Date")

    # Get the minimum and maximum dates
    min_date = df["Date"].min()
    max_date = df["Date"].max()

    print("Minimum Date:", min_date)
    print("Maximum Date:", max_date)

    # Prompt the user for the duration period
    while True:
        start_date = pd.to_datetime(input("Enter the start date (YYYY-MM-DD): "))
        end_date = pd.to_datetime(input("Enter the end date (YYYY-MM-DD): "))

        if start_date < min_date or end_date > max_date:
            print("Invalid date range. Please enter dates within the available range.")
        else:
            break

    # Filter the DataFrame based on the user-defined date range
    df = df.loc[(df["Date"] >= start_date) & (df["Date"] <= end_date)]

    # Convert string values for "Open", "High", and "Low" to float, replacing errors with NaN
    df['Open'] = pd.to_numeric(df['Open'], errors='coerce')
    df['High'] = pd.to_numeric(df['High'], errors='coerce')
    df['Low'] = pd.to_numeric(df['Low'], errors='coerce')

    # Filter each stock into a separate DataFrame based on symbols
    symbols = ['AIG', 'F', 'FB', 'GOOG', 'M', 'MSFT', 'RDS-A']
    stock_list = [(symbol, df.loc[df['Symbol'] == symbol].copy()) for symbol in symbols]

    # Prompt the user for the chart type
    chart_type = input("Enter the type of chart you want to plot (candle): ")

    # Iterate through each stock DataFrame and plot the data
    for symbol, stock in stock_list:
        # Set the index as DatetimeIndex
        stock.set_index("Date", inplace=True)

        # Drop rows with missing values in the "Open," "High," "Low," and "Close" columns
        stock_filtered = stock.loc[:, ["Open", "High", "Low", "Close"]].copy()
        stock_filtered.dropna(inplace=True)

        if not stock_filtered.empty:  # Check if there are remaining valid rows
            mpf.plot(stock_filtered, type=chart_type, title=f"Stock: {symbol}")

