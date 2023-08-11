class Stock:
    def __init__(self, ticker: str, current_cost: float, percent_allocation: float):
        """Stock object

        Args:
            ticker (str): Ticker of the stoc
            current_cost (float): Current cost. Must be found by API
            percet_allocation (float): Percent allocation as decribed by a number from 0 - 1.00. This is the desired percent allocation to buy with the remaining money
        """
        self.ticker = ticker.upper()
        self.current_cost = current_cost
        self.percent_allocation = percent_allocation
        self.purchase_number = 0

    def __str__(self) -> str:
        return f"Stock: {self.ticker} costs {self.current_cost} and you have allocated {self.percent_allocation * 100}%"
