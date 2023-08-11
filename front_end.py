from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Stock Calculator")

frm = ttk.Frame(root, padding=10)
frm.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

total_cash = StringVar()
total_cash_entry = ttk.Entry(frm, width=7, textvariable=total_cash)
total_cash_entry.grid(column=2, row=1, sticky=(W, E))

ticker = StringVar()
ticker_entry = ttk.Entry(frm, width=7, textvariable=ticker)
ticker_entry.grid(column=1, row=2, sticky=(W, E))

percent = StringVar()
percent_entry = ttk.Entry(frm, width=7, textvariable=percent)
percent_entry.grid(column=1, row=3, sticky=(W, E))

# Labels
ttk.Label(frm, text="Total cash for purchase").grid(column=3, row=1, sticky=W)
ttk.Label(frm, text="Ticker").grid(column=2, row=2, sticky=W)
ttk.Label(frm, text="Percent Allocation").grid(column=2, row=3, sticky=W)

# Buttons


def add_new_stock():
    print("I love Kelly!")


create_new_stock = ttk.Button(
    root, text="Add New Stock", default="active", command=add_new_stock)
create_new_stock.grid(column=2, row=4, sticky=(W, E))
root.bind('<Return>', lambda e: add_new_stock.invoke())

root.mainloop()
