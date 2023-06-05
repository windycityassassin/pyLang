class Stock:
    def __init__(self, ticker):
        self.ticker = ticker
        self.datelist = []
        self.closelist = []

    def add_price(self, date, close):
        self.closelist.append(close)
        self.datelist.append(date)
