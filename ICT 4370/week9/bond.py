class Bond:
    def __init__(self, symbol, shares, purchase_price, current_price, purchase_date, coupon, yield_rate):
        self.symbol = symbol
        self.shares = shares
        self.purchase_price = purchase_price
        self.current_price = current_price
        self.purchase_date = purchase_date
        self.coupon = coupon
        self.yield_rate = yield_rate
        self.current_value = 0.0

    def calculate_current_value(self):
        self.current_value = self.shares * self.current_price
