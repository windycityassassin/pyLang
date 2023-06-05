import datetime

# Defining a function to calculate earnings/loss for each stock and store it in a list
def calculate_earnings_loss(stock_symbols, num_shares, purchase_price, current_price):
    earnings_loss = []
    for i in range(len(stock_symbols)):
        earnings_loss.append(round((current_price[i] - purchase_price[i]) * num_shares[i]))
    return earnings_loss


# Defining a function to calculate percentage yield/loss for each stock
def calculate_percentage_yield_loss(stock_symbols, purchase_date, purchase_price, current_price):
    percentage_yield_loss = []
    for i in range(len(stock_symbols)):
        purchase_days = (datetime.date.today() - purchase_date[i]).days
        if purchase_days > 0:
            yearly_yield_loss = round((((current_price[i] - purchase_price[i]) / purchase_price[i]) / (purchase_days / 365)) * 100, 2)
        else:
            yearly_yield_loss = 0
        percentage_yield_loss.append(yearly_yield_loss)
    return percentage_yield_loss


# Printing the report
def print_report(stock_symbols, num_shares, earnings_loss, percentage_yield_loss):
    # Printing the header for the report
    print("Stock ownership for Bob Smith")
    print('Stock \t\t Share \t\t Earnings/Loss \t\t Yearly Earning/Loss %')

    # Printing the stock information for each stock symbol
    for i in range(len(stock_symbols)):
        print(f"{stock_symbols[i]} \t\t {num_shares[i]} \t\t ${earnings_loss[i]} \t\t {percentage_yield_loss[i]}%")
