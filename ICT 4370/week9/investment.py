class InvestmentPortfolio:
    def __init__(self):
        self.stocks = []
        self.bonds = []

    def add_stock(self, stock):
        self.stocks.append(stock)

    def add_bond(self, bond):
        self.bonds.append(bond)
