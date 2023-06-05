import datetime
from stock_report import calculate_earnings_loss, calculate_percentage_yield_loss, print_report

def main():
    # Creating lists to store data for different stocks
    stock_symbols = ['GOOGLE', 'MSFT', 'RDS-A', 'AIG', 'FB', 'M', 'F', 'IBM']
    num_shares = [55, 35, 470, 215, 13, 425, 85, 80]
    purchase_price = [72.88, 356, 98.06, 453.87, 11.83, 30.30, 12.58, 150.37]
    current_price = [41.53, 673.04, 55.74, 365.27, 175.45, 23.98, 10.95, 145.30]
    purchase_date = [datetime.date(2017, 8, 1)] * 5 + [datetime.date(2018, 1, 10), datetime.date(2018, 2, 17),
                                                       datetime.date(2018, 5, 12)]

    # Calling the functions to calculate earnings/loss and percentage yield/loss
    earnings_loss = calculate_earnings_loss(stock_symbols, num_shares, purchase_price, current_price)
    percentage_yield_loss = calculate_percentage_yield_loss(stock_symbols, purchase_date, purchase_price, current_price)

    # Calling the function to print the report
    print_report(stock_symbols, num_shares, earnings_loss, percentage_yield_loss)


if __name__ == "__main__":
    main()
