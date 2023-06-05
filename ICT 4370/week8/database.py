import sqlite3
from datetime import datetime


def create_database(data):
    conn = sqlite3.connect('stock_data.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS stock_data
                 (symbol TEXT, date TEXT, close REAL)''')

    for line in data:
        symbol = line['Symbol']
        close = line['Close']
        date = datetime.datetime.strptime(line['Date'], '%d-%b-%y').date()
        c.execute("INSERT INTO stock_data VALUES (?, ?, ?)", (symbol, date, close))

    conn.commit()
    conn.close()
