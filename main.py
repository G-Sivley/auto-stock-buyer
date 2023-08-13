from front_end import FrontEnd
from stock_brain import StockBrain


def main():
    # Get data from API or website

    # Once data is received use the numbers to calculate how many stocks to buy
    total_cash = 500 
    sb = StockBrain(total_cash=total_cash)
    fe = FrontEnd(sb=sb)

    # sb.allocate_cash()
    # for stock in sb.stocks:
    #     print(f"Buy {stock.purchase_number} of {stock.ticker}!")

# Buy the number of stocks

    # Send a confirmation


if __name__ == "__main__":
    main()
