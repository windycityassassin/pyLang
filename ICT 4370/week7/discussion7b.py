import sqlite3
from tabulate import tabulate
import csv

# Open a connection to the database
conn = sqlite3.connect('investments.db')
cursor = conn.cursor()

# Drop the investors table if it already exists
cursor.execute("DROP TABLE IF EXISTS investors")
cursor.execute("DROP TABLE IF EXISTS stocks")
cursor.execute("DROP TABLE IF EXISTS bonds")

# Create the investors table
cursor.execute('''CREATE TABLE investors (
    investor_id INTEGER PRIMARY KEY,
    name TEXT,
    address TEXT,
    phone_number TEXT
)''')

cursor.execute('''CREATE TABLE stocks (
    purchase_id INTEGER PRIMARY KEY,
    investor_id INTEGER,
    symbol TEXT,
    shares INTEGER,
    purchase_price REAL,
    purchase_date TEXT,
    current_value REAL,
    FOREIGN KEY (investor_id) REFERENCES investors (investor_id)
)''')

cursor.execute('''CREATE TABLE bonds (
    purchase_id INTEGER PRIMARY KEY,
    investor_id INTEGER,
    symbol TEXT,
    shares INTEGER,
    purchase_price REAL,
    purchase_date TEXT,
    current_value REAL,
    coupon REAL,
    yield REAL,
    FOREIGN KEY (investor_id) REFERENCES investors (investor_id)
)''')


# Define functions for inserting data into the database

def investor_insert(name, address, phone_number):
    # Define query string with placeholders for parameters
    query = "INSERT INTO investors (name, address, phone_number) VALUES (%s, %s, %s)"
    # Create tuple of values to substitute into query string
    values = (name, address, phone_number)
    # Execute the query with values tuple and commit changes
    cursor.execute(query, values)
    conn.commit()


def stock_insert(investor_id, symbol, shares, purchase_price, current_value, purchase_date):
    # Define query string with placeholders for parameters
    query = "INSERT INTO stocks (investor_id, symbol, shares, purchase_price, current_value, purchase_date) VALUES (" \
            "%s, %s, %s, %s, %s, %s) "
    # Create tuple of values to substitute into query string
    values = (investor_id, symbol, shares, purchase_price, current_value, purchase_date)
    # Execute the query with values tuple and commit changes
    cursor.execute(query, values)
    conn.commit()


def bond_insert(investor_id, symbol, shares, purchase_price, current_value, purchase_date, coupon, bond_yield):
    # Define query string with placeholders for parameters
    query = "INSERT INTO bonds (investor_id, symbol, shares, purchase_price, current_value, purchase_date, coupon, " \
            "yield) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) "
    # Create tuple of values to substitute into query string
    values = (investor_id, symbol, shares, purchase_price, current_value, purchase_date, coupon, bond_yield)
    # Execute the query with values tuple and commit changes
    cursor.execute(query, values)
    conn.commit()


# Function to import data from a file for a given investor and data type
def data_import(absolute_path, investor_id, data_type):
    try:
        with open(absolute_path) as data:
            reader = csv.reader(data)
            is_header = True
            # Loop through each line in the file
            for line in reader:
                if not is_header:  # Skip the header line
                    if data_type == 'bond':  # If data type is bond, insert into bond table
                        if len(line) == 9:
                            bond_insert(investor_id, *line)
                        else:
                            print(
                                f"Error: Invalid number of fields in line for bond data. Expected 9 fields, got {len(line)}")
                    elif data_type == 'stock':  # If data type is stock, insert into stock table
                        if len(line) == 6:
                            stock_insert(investor_id, *line)
                        else:
                            print(
                                f"Error: Invalid number of fields in line for stock data. Expected 6 fields, got {len(line)}")
                is_header = False  # Set header flag to False after processing the first line
    except:
        print(f'Failed to import {data_type}s from file: {absolute_path}')


# Function to import bond data from a file for a given investor
def bonds_import(absolute_path, investor_id):
    data_import(absolute_path, investor_id, 'bond')


# Function to import stock data from a file for a given investor
def stocks_import(absolute_path, investor_id):
    data_import(absolute_path, investor_id, 'stock')


try:
    # Read stocks data from CSV file
    with open('Lesson6_Data_Stocks.csv', mode='r') as stocks_file:
        stocks_lines = stocks_file.readlines()
    stocks_data = [line.strip().split(',') for line in stocks_lines]

    # Read bonds data from CSV file
    with open('Lesson6_Data_Bonds.csv', mode='r') as bonds_file:
        bonds_lines = bonds_file.readlines()
    bonds_data = [line.strip().split(',') for line in bonds_lines]

    # Open a file for writing the report
    with open('report1.txt', mode='w') as report_file:
        # Write the stocks data to the report
        report_file.write('Stocks Data:\n')
        stocks_table = tabulate(stocks_data,
                                headers=["Symbol", "Shares", "Purchase Price", "Current Value", "Purchase Date"])
        report_file.write(stocks_table)
        report_file.write('\n\n')

        # Write the bonds data to the report
        report_file.write('Bonds Data:\n')
        bonds_table = tabulate(bonds_data,
                               headers=["Symbol", "Shares", "Purchase Price", "Current Value", "Purchase Date",
                                        "Coupon", "Yield"])
        report_file.write(bonds_table)
        report_file.write('\n\n')

    # Confirm that the report was written by reading and printing its contents
    with open('report1.txt', mode='r') as report_file:
        report_contents = report_file.read()
        print(report_contents)

except FileNotFoundError:
    # Handle file not found error
    print("File not found. Please check the file path and try again.")
except Exception as e:
    # Handle any other error
    print("An error occurred:", e)


    def generate_report():
        # Try to open the investor file
        try:
            with open("investors.csv", "r") as f:
                investor_records = f.readlines()
        # If the file does not exist, create an empty file
        except FileNotFoundError:
            print("The file does not exist.")
            with open("investors.csv", "w"):
                pass
            # Set the investor records to an empty list
            investor_records = []

        # Loop over each investor record
        for investor in investor_records:
            # Split the investor record into ID and name
            investor_id, investor_name = investor.split(",")

            # Open the bond file
            with open("Lesson6_Data_Bonds.csv", "r") as f:
                bond_records = f.readlines()

            # Open the stock file
            with open("Lesson6_Data_Stocks.csv", "r") as f:
                stock_records = f.readlines()

            # Calculate the total value of the investor's bonds
            total_bond_value = 0
            for bond in bond_records:
                bond_id, bond_name, bond_shares, bond_current_value = bond.split(",")
                total_bond_value += int(bond_current_value) * int(bond_shares)

            # Calculate the total value of the investor's stocks
            total_stock_value = 0
            for stock in stock_records:
                stock_id, stock_name, stock_shares, stock_current_value = stock.split(",")
                total_stock_value += int(stock_current_value) * int(stock_shares)

            # Print a report for the investor
            print(f"Investor: {investor_name}")
            print("Bond Holdings:")
            for bond in bond_records:
                bond_id, bond_name, bond_shares, bond_current_value = bond.split(",")
                print(f"\t{bond_name}: {bond_shares} shares, current value: {bond_current_value}")
            print(f"\tTotal Bond Value: {total_bond_value}")
            print("Stock Holdings:")
            for stock in stock_records:
                stock_id, stock_name, stock_shares, stock_current_value = stock.split(",")
                print(f"\t{stock_name}: {stock_shares} shares, current value: {stock_current_value}")
            print(f"\tTotal Stock Value: {total_stock_value}")
            print(f"Total Portfolio Value: {total_bond_value + total_stock_value}\n")


    if __name__ == "__main__":
        # Call the generate_report function
        generate_report()

# close db connection
conn.close()