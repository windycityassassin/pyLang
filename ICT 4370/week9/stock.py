import numpy as np


class Stock:
    def __init__(self, symbol, shares, purchase_price, current_price, purchase_date):
        self.symbol = symbol
        self.shares = shares
        self.purchase_price = purchase_price
        self.current_price = current_price
        self.purchase_date = purchase_date

    def calculate_current_value(self):
        return self.shares * self.current_price

    def calculate_average_price(self):
        return np.mean([self.purchase_price, self.current_price])

    def calculate_standard_deviation(self):
        return np.std([self.purchase_price, self.current_price])

    def calculate_correlation(self, other_stock):
        return np.corrcoef([self.current_price], [other_stock.current_price])[0, 1]
