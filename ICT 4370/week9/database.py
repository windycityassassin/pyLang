import sqlite3
from stock import Stock
from bond import Bond

class Database:
    def __init__(self, db_name):
        self.db_name = db_name

    def create_table(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()

        # Create the stock_data table if it doesn't exist
        c.execute('''CREATE TABLE IF NOT EXISTS stock_data
                     (symbol TEXT, shares INTEGER, purchase_price REAL, current_price REAL,
                     purchase_date DATE, coupon REAL, yield_rate REAL)''')

        conn.commit()
        conn.close()

    def insert_data(self, data):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()

        for item in data:
            if isinstance(item, Stock):
                c.execute("INSERT INTO stock_data VALUES (?, ?, ?, ?, ?, NULL, NULL)",
                          (item.symbol, item.shares, item.purchase_price, item.current_price, item.purchase_date))
            elif isinstance(item, Bond):
                c.execute("INSERT INTO stock_data VALUES (?, ?, ?, ?, ?, ?, ?)",
                          (item.symbol, item.shares, item.purchase_price, item.current_price, item.purchase_date,
                           item.coupon, item.yield_rate))

        conn.commit()
        conn.close()
