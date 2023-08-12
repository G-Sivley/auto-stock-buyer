from tkinter import *
from tkinter import ttk


class FrontEnd():
    def __init__(self) -> None:
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
        ttk.Label(self.frm, text="Total cash for purchase").grid(column=2, row=1, sticky=W)
        ttk.Label(self.frm, text="Ticker").grid(column=2, row=2, sticky=W)
        ttk.Label(self.frm, text="Percent Allocation").grid(column=2, row=3, sticky=W)

    def insert_buttons(self):
        # Buttons
        total_cash_button = ttk.Button(self.root, text="Add Total Cash", default="active", command=self.add_new_cash)        
        total_cash_button.grid(column=1, row=4, sticky=(W,E))
        self.root.bind("<Return>", lambda e: self.add_new_cash)

        create_new_stock_button = ttk.Button(
            self.root, text="Add New Stock", default="active", command=self.add_new_stock)
        create_new_stock_button.grid(column=2, row=4, sticky=(W, E))
        self.root.bind('<Return>', lambda e: self.add_new_stock.invoke())

    def add_new_cash(self):
        total_cash = self.total_cash.get()
        print(total_cash)

    def add_new_stock(self):
        ticker = self.ticker.get()
        percent = self.percent.get() 
        print((ticker, percent))
        

    def run_loop(self):
        self. root.mainloop()


s = FrontEnd()