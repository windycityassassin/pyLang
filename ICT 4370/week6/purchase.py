import datetime

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
            yearly_yield_loss = round((((self.current_price - self.purchase_price) / self.purchase_price) / (purchase_days / 365)) * 100, 2)
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
