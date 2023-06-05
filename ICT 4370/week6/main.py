from datetime import datetime
from tabulate import tabulate
from investor import Investor
from purchase import Stock, Bond
from portfolio import InvestmentPortfolio

try:
    # Read stocks data from CSV file
    with open('Lesson6_Data_Stocks.csv', mode='r') as stocks_file:
        stocks_lines = stocks_file.readlines()
    stocks_data = [line.strip().split(',') for line in stocks_lines[1:]]

    # Read bonds data from CSV file
    with open('Lesson6_Data_Bonds.csv', mode='r') as bonds_file:
        bonds_lines = bonds_file.readlines()
    bonds_data = [line.strip().split(',') for line in bonds_lines[1:]]

    # Create investor objects
    investor1 = Investor(1, "John Doe", "123 Main St", "555-1234")
    investor2 = Investor(2, "Jane Smith", "456 Elm St", "555-5678")

    # Create stock objects
    stocks = []
    for data in stocks_data:
        symbol, shares, purchase_price, current_value, purchase_date = data
        purchase_date = datetime.strptime(purchase_date, "%m/%d/%Y").date()
        stock = Stock(None, None, symbol, int(shares), float(purchase_price), purchase_date, float(current_value))
        stocks.append(stock)

    # Create bond objects
    bonds = []
    for data in bonds_data:
        symbol, shares, purchase_price, current_value, purchase_date, coupon, yield_rate = data
        purchase_date = datetime.strptime(purchase_date, "%m/%d/%Y").date()
        bond = Bond(None, None, symbol, int(shares), float(purchase_price), purchase_date, float(current_value), float(coupon), float(yield_rate))
        bonds.append(bond)

    # Create investment portfolio and add purchases
    portfolio = InvestmentPortfolio()
    portfolio.add_purchase(stocks)
    portfolio.add_purchase(bonds)

    # Open a file for writing the report
    with open('report1.txt', mode='w') as report_file:
        # Write the stocks data to the report
        report_file.write('Stocks Data:\n')
        stocks_table = tabulate(stocks_data[:5], headers='firstrow', tablefmt='pipe')
        report_file.write(stocks_table)
        report_file.write('\n\n')

        # Write the bonds data to the report
        report_file.write('Bonds Data:\n')
        bonds_table = tabulate(bonds_data[:5], headers='firstrow', tablefmt='pipe')
        report_file.write(bonds_table)
        report_file.write('\n')

    # Confirm that the report was written by reading and printing its contents
    with open('report1.txt', mode='r') as report_file:
        report_contents = report_file.read()
        print(report_contents)

except FileNotFoundError:
    print("File not found. Please check the file path and try again.")
except ValueError:
    print("Invalid data format in the files.")
except Exception as e:
    print("An error occurred:", e)
