from tkinter import *
from tkinter import ttk

from stock_brain import StockBrain


class FrontEnd():
    def __init__(self, sb: StockBrain) -> None:
        self.sb = sb
        self.total_cash = None
        self.ticker = None
        self.percent = None

        self.root = Tk()
        self.frm = self.make_window()
        self.insert_entry()
        self.insert_label()
        self.insert_buttons()
        self.run_loop()

    def make_window(self):
        self.root.title("Stock Calculator")

        frm = ttk.Frame(self.root, padding=50)
        frm.grid(column=0, row=0, sticky=(N, W, E, S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        return frm
    
    def insert_entry(self):
        total_cash = StringVar()
        total_cash_entry = ttk.Entry(self.frm, width=7, textvariable=total_cash)
        total_cash_entry.grid(column=1, row=1, sticky=(W, E))
        self.total_cash = total_cash_entry

        ticker = StringVar()
        ticker_entry = ttk.Entry(self.frm, width=7, textvariable=ticker)
        ticker_entry.grid(column=1, row=2, sticky=(W, E))
        self.ticker = ticker_entry

        percent = StringVar()
        percent_entry = ttk.Entry(self.frm, width=7, textvariable=percent)
        percent_entry.grid(column=1, row=3, sticky=(W, E))
        self.percent = percent_entry

    def insert_label(self):
        # Labels
        ttk.Label(self.frm, text="Stock Purchase Calculator", font="bold 18" ).grid(column=2, row=0, pady=10, columnspan=3, sticky=W)
        ttk.Label(self.frm, text="Total cash for purchase ($)").grid(column=2, row=1, sticky=W, columnspan=3)
        ttk.Label(self.frm, text="Ticker").grid(column=2, row=2, sticky=W)
        ttk.Label(self.frm, text="Percent Allocation (0.00 - 1.00)").grid(column=2, row=3, sticky=W, columnspan=3)
        ttk.Label(self.frm, text="Stocks", font="bold 16").grid(column=2, row=5, sticky=W, pady=10, columnspan=3)

        ttk.Label(self.frm, text="Ticker", font="bold 11").grid(column=1, row=6, sticky=W)
        ttk.Label(self.frm, text="Price", font="bold 11").grid(column=2, row=6, sticky=W)
        ttk.Label(self.frm, text="Percent", font="bold 11").grid(column=3, row=6, sticky=W)
        ttk.Label(self.frm, text="Stocks", font="bold 11").grid(column=4, row=6, sticky=W)
        ttk.Label(self.frm, text="Cost", font="bold 11").grid(column=5, row=6, sticky=W)


    def insert_buttons(self):
        # Buttons
        total_cash_button = ttk.Button(self.root, text="Add Total Cash", default="active", command=self.add_new_cash)        
        total_cash_button.grid(column=0, row=4, sticky=E, pady=10)
        self.root.bind("<Return>", lambda e: self.add_new_cash)

        create_new_stock_button = ttk.Button(
            self.root, text="Add New Stock", default="active", command=self.add_new_stock)
        create_new_stock_button.grid(column=1, row=4, sticky=W, padx=10, pady=10)
        self.root.bind('<Return>', lambda e: self.add_new_stock.invoke())

        calculate_button = ttk.Button(self.root, text="Calculate", default="active", command=self.calculate)        
        calculate_button.grid(column=2, row=4, sticky=W, padx=(0, 10))
        self.root.bind("<Return>", lambda e: self.calculate)

    def add_new_cash(self):
        total_cash = self.total_cash.get()
        self.sb.set_total_cash(total_cash)

    def add_new_stock(self):
        ticker = self.ticker.get()
        percent = self.percent.get() 
        self.sb.make_stock(ticker=ticker, percent_allocation=percent) 
        self.display_stocks() 

    def calculate(self):
        print("calculate")
    
    def display_stocks(self):
        self.sb.allocate_cash()

        row = 7
        for stock in self.sb.stocks:
            ttk.Label(self.frm, text=stock.ticker).grid(column=1, row=row)
            ttk.Label(self.frm, text=stock.current_cost).grid(column=2, row=row)
            ttk.Label(self.frm, text=stock.percent_allocation).grid(column=3, row=row)
            ttk.Label(self.frm, text=stock.purchase_number).grid(column=4, row=row)
            ttk.Label(self.frm, text={stock.purchase_number * stock.current_cost}).grid(column=5, row=row)

            row += 1

    def run_loop(self):
        self. root.mainloop()

sb = StockBrain(500)
s = FrontEnd(sb)