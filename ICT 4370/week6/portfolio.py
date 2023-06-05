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
