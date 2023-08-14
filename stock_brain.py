from math import floor
import yfinance as yf

from stock import Stock


class StockBrain:
    def __init__(self, total_cash: float):
        self.starting_cash = total_cash
        self.remaining_cash = total_cash
        self.stocks = []

    def set_total_cash(self, total_cash: float):
        self.starting_cash = total_cash
        self.remaining_cash = total_cash

    def add_stock(self, stock: Stock):
        self.stocks.append(stock)

    def order_stocks_by_percentage(self):
        # Order stocks by percent allocation
        self.stocks.sort(key=lambda x: x.percent_allocation)

    def get_floor(self, cost: float, allocation_cash: float):
        # If we have enough cash, that it is greater than allocation cash, use allocation cash
        if self.remaining_cash >= allocation_cash:
            return floor(allocation_cash/cost)

        # If not use remaining cash as the numerator
        else:
            return floor(self.remaining_cash/cost)

    def get_cost_can_allocate(self, percentage):
        return self.starting_cash * percentage

    def reduce_remaining_cash(self, stock_count: int, stock_current_cost: float):
        self.remaining_cash -= (stock_count * stock_current_cost)

    # Buy Stocks

    def allocate_cash(self):
        self.remaining_cash = self.starting_cash
        new_list = []
        self.order_stocks_by_percentage()
        for stock in self.stocks:
            allocation_cash = self.get_cost_can_allocate(
                stock.percent_allocation)

            # If last stock in list just buy the rest
            if stock == self.stocks[-1]:
                stock.purchase_number = self.get_floor(stock.current_cost, self.remaining_cash)
            # If there is not enough money do not buy stock
            
            elif stock.current_cost > self.remaining_cash:
                stock.purchase_number = 0

            # If the allocation cash is less than current cost, get the number of stocks can buy
            elif allocation_cash >= stock.current_cost:
                stocks_can_buy = self.get_floor(
                    stock.current_cost, allocation_cash)
                stock.purchase_number = stocks_can_buy

            # If there is enough money and the stock is not the last stock, buy at least one
            else:
                stock.purchase_number = 1

            self.reduce_remaining_cash(
                stock.purchase_number, stock.current_cost)
            new_list.append(stock)

    def make_stock_with_text(self):
        ticker = input("What is the stock ticker: ")
        yf_ticker = yf.Ticker(ticker)
        current_cost = yf_ticker.info["ask"]
        percent_allocation = float(
            input("What percentage would you like to allocate (0.00 - 1.00): "))
        new_stock = Stock(ticker=ticker, current_cost=current_cost,
                          percent_allocation=percent_allocation)
        self.stocks.append(new_stock)

    def make_stock(self, ticker: str, percent_allocation: float):
        yf_ticker = yf.Ticker(ticker)
        current_cost = float(yf_ticker.info["ask"])
        new_stock = Stock(ticker=ticker, current_cost=current_cost, percent_allocation=float(percent_allocation))
        self.add_stock(new_stock)
    
    def print_stocks(self):
        for i in self.stocks:
            print(i)
