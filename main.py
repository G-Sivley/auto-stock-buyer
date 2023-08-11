from stock_brain import StockBrain


def main():
    # Get data from API or website

    # Once data is received use the numbers to calculate how many stocks to buy
    total_cash = float(input("How much cash do you have?: "))
    sb = StockBrain(total_cash)
    while True:
        add_stock = input("Would you like to add a stock in text? (y/n): ")
        if add_stock.lower() == "y":
            sb.make_stock_with_text()
        else:
            break

    sb.allocate_cash()
    for stock in sb.stocks:
        print(f"Buy {stock.purchase_number} of {stock.ticker}!")

# Buy the number of stocks

    # Send a confirmation


if __name__ == "__main__":
    main()