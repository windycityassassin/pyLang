# author: apv
# date: 26/4/23
# purpose: Improving by adding classes and also additionally adding bonds

import datetime

class Investor:
    def __init__(self, investor_id, name, address, phone_number):
        self.investor_id = investor_id
        self.name = name
        self.address = address
        self.phone_number = phone_number

class Purchase:
    def __init__(self, purchase_id, investor_id, symbol, shares, purchase_price, purchase_date):
        self.purchase_id = purchase_id
        self.investor_id = investor_id
        self.symbol = symbol
        self.shares = shares
        self.purchase_price = purchase_price
        self.purchase_date = purchase_date

class Stock(Purchase):
    def __init__(self, purchase_id, investor_id, symbol, shares, purchase_price, purchase_date, current_price):
        super().__init__(purchase_id, investor_id, symbol, shares, purchase_price, purchase_date)
        self.current_price = current_price

    def calculate_earnings_loss(self):
        return round((self.current_price - self.purchase_price) * self.shares, 2)

    def calculate_percentage_yield_loss(self):
        purchase_days = (datetime.date.today() - self.purchase_date).days
        if purchase_days > 0:
            yearly_yield_loss = round(
                (((self.current_price - self.purchase_price) / self.purchase_price) / (purchase_days / 365)) * 100, 2)
        else:
            yearly_yield_loss = 0
        return yearly_yield_loss

class Bond(Stock):
    def __init__(self, purchase_id, investor_id, symbol, shares, purchase_price, purchase_date, current_price, coupon, yield_rate):
        super().__init__(purchase_id, investor_id, symbol, shares, purchase_price, purchase_date, current_price)
        self.coupon = coupon
        self.yield_rate = yield_rate

    def calculate_earnings_loss(self):
        return round((self.coupon * self.shares), 2)

    def calculate_percentage_yield_loss(self):
        return round(self.yield_rate, 2)

class InvestmentPortfolio:
    def __init__(self):
        self.purchases = []

    def add_purchase(self, purchase):
        self.purchases.append(purchase)

    def remove_purchase(self, purchase):
        self.purchases.remove(purchase)

    def calculate_total_earnings_loss(self):
        total_earnings_loss = 0
        for purchase in self.purchases:
            total_earnings_loss += purchase.calculate_earnings_loss()
        return round(total_earnings_loss, 2)

    def calculate_total_percentage_yield_loss(self):
        total_yield_loss = 0
        for purchase in self.purchases:
            total_yield_loss += purchase.calculate_percentage_yield_loss()
        return round(total_yield_loss, 2)

# create investor
bob = Investor(1, "Bob Smith", "123 Main St", "555-1234")

# create bond purchases
gt2_gov = Bond(1, 1, "GT2:GOV", 200, 100.02, datetime.date(2017, 8, 1), 100.05, 1.38, 1.35)

# create stock purchases
stock_symbols = ['GOOGLE', 'MSFT', 'RDS-A', 'AIG', 'FB', 'M', 'F', 'IBM']
num_shares = [55, 35, 470, 215, 13, 425, 85, 80]
purchase_price = [72.88, 356, 98.06, 453.87, 11.83, 30.30, 12.58, 150.37]
current_price = [41.53, 673.04, 55.74, 365.27, 175.45, 23.98, 10.95, 145.30]
purchase_date = [datetime.date(2017, 8, 1)] * 5 + [datetime.date(2018, 1, 10), datetime.date(2018, 2, 17), datetime.date(2018, 5, 12)]

stock_purchases = []
for i in range(len(stock_symbols)):
    stock_purchase = Stock(i+2, 1, stock_symbols[i], num_shares[i], purchase_price[i], purchase_date[i], current_price[i])
    stock_purchases.append(stock_purchase)

# create investment portfolio
bob_portfolio = InvestmentPortfolio()

# add purchases to investment portfolio
bob_portfolio.add_purchase(gt2_gov)
for stock_purchase in stock_purchases:
    bob_portfolio.add_purchase(stock_purchase)

# calculate total earnings loss and total percentage yield loss for investment portfolio
total_earnings_loss = bob_portfolio.calculate_total_earnings_loss()
total_percentage_yield_loss = bob_portfolio.calculate_total_percentage_yield_loss()

# print bond and stock information
print("\nBonds:")
print(f"{'Symbol':<10} {'Quantity':<10} {'Purchase Price':<20} {'Current Price':<20} {'Coupon':<10} {'Yield Rate':<10} {'Earnings/Loss':<15} {'% Yield/Loss':<15}")
for purchase in bob_portfolio.purchases:
    if isinstance(purchase, Bond):
        earnings_loss = purchase.calculate_earnings_loss()
        percentage_yield_loss = purchase.calculate_percentage_yield_loss()
        print(f"{purchase.symbol:<10} {purchase.shares:<10} {purchase.purchase_price:<20} {purchase.current_price:<20} {purchase.coupon:<10} {purchase.yield_rate:<10} {earnings_loss:<15} {percentage_yield_loss:<15}")

print("\nStocks:")
print(f"{'Symbol':<10} {'Quantity':<10} {'Purchase Price':<20} {'Current Price':<20} {'Earnings/Loss':<15} {'% Yield/Loss':<15}")
for purchase in bob_portfolio.purchases:
    if isinstance(purchase, Stock):
        earnings_loss = purchase.calculate_earnings_loss()
        percentage_yield_loss = purchase.calculate_percentage_yield_loss()
        print(f"{purchase.symbol:<10} {purchase.shares:<10} {purchase.purchase_price:<20} {purchase.current_price:<20} {earnings_loss:<15} {percentage_yield_loss:<15}")