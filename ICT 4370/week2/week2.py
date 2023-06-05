# author: apv
# date: 8/4/23
# this program calculates the increase/decrease in Bob's portfolio

# part 1 (creating data tables)
stock_symbols = ['GOOGLE', 'MSFT', 'RDS-A', 'AIG', 'FB']
num_shares = [55, 35, 470, 215, 13]
purchase_price = [72.88, 356, 98.06, 453.87, 11.83]
current_price = [41.53, 673.04, 55.74, 365.27, 175.45]

# part 2 (Calculating earnings/loss for each stock and storing it in a list)
earnings_loss = []
for i in range(len(stock_symbols)):
    earnings_loss.append(round((current_price[i] - purchase_price[i]) * num_shares[i]))

# Printing the report
print("Stock ownership for Bob Smith")
print('Stock \t\t Share \t\t Earnings/Loss')
for i in range(len(stock_symbols)):
    print(stock_symbols[i] + "\t\t" + str(num_shares[i]) + "\t\t$" + str(earnings_loss[i]))

# Finding the stock with highest increase in value
highest_increase_index = earnings_loss.index(max(earnings_loss))
highest_increase_stock = stock_symbols[highest_increase_index]

# Checking if all stocks lost value
if all(i < 0 for i in earnings_loss):
    least_loss_index = earnings_loss.index(max(earnings_loss))
    least_loss_stock = stock_symbols[least_loss_index]
    print("The stock with least decrease in value in your portfolio on a per-share basis is: " + least_loss_stock)
else:
    print("The stock with the highest increase in value in your portfolio on a per-share basis is: " + highest_increase_stock)

# Finding stock with least decrease in value on a per-share basis
min_decrease = None
min_decrease_stock = None

for i in range(len(stock_symbols)):
    decrease = current_price[i] - purchase_price[i]
    per_share_decrease = decrease / num_shares[i]
    if min_decrease is None or per_share_decrease > min_decrease:
        min_decrease = per_share_decrease
        min_decrease_stock = stock_symbols[i]

# Output
if min_decrease is not None and min_decrease < 0:
    print("The stock with least decrease in value in your portfolio on a per-share basis is: " + min_decrease_stock)
elif min_decrease is not None and min_decrease >= 0:
    print("The stock with the highest increase in value in your portfolio on a per-share basis is: " + highest_increase_stock)
else:
    print("There was an error in calculating the stock performance.")
