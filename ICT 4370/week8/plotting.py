import matplotlib.dates as mdates
import matplotlib.pyplot as plt

def plot_stock_prices(stock_dict):
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.suptitle('Closing Prices for Different Stocks', fontsize=16, fontweight='bold')

    for stock in stock_dict:
        stock_obj = stock_dict[stock]['Stock']
        close_prices = stock_obj.closelist
        dates = mdates.date2num(stock_obj.datelist)
        stock_name = stock_obj.ticker

        color = next(ax._get_lines.prop_cycler)['color']
        ax.plot_date(dates, close_prices, linestyle="-.", label=stock_name, color=color, linewidth=0.1)
        ax.lines[-1].set_linewidth(0.1)

    ax.set_xlabel('Date')
    ax.set_ylabel('Closing Price')

    date_fmt = mdates.DateFormatter('%Y-%m-%d')
    ax.xaxis.set_major_formatter(date_fmt)
    ax.xaxis.set_tick_params(rotation=30, labelsize=10)

    ax.yaxis.set_major_formatter('${:.0f}'.format)

    ax.legend(loc='upper left', fontsize=10)
    ax.grid(True)

    plt.show()

def save_plot_as_png(filename):
    plt.savefig(filename)
