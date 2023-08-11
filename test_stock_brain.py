import unittest
from stock_brain import StockBrain
from stock import Stock


class TestStockBrain(unittest.TestCase):
    def setUp(self):
        total_cash = 500.50
        self.sb = StockBrain(total_cash)

        self.s1 = Stock("VXUS", 50, 0.1)
        self.s2 = Stock("SCHB", 50, 0.7)
        self.s3 = Stock("AVUV", 80, 0.2)
        for stock in [self.s1, self.s2, self.s3]:
            self.sb.add_stock(stock)

    def test_init_object(self):
        self.assertIsInstance(self.sb, StockBrain)

    def test_add_stock(self):
        self.sb.add_stock(self.s1)
        self.assertIn(self.s1, self.sb.stocks)

    def test_order_by_percentage(self):
        self.sb.order_stocks_by_percentage()
        list_of_stocks = self.sb.stocks
        self.assertListEqual([self.s1, self.s3, self.s2], list_of_stocks)

    def test_not_enough_cash(self):
        self.sb.stocks[0].current_cost = 1000
        self.sb.allocate_cash()
        number_of_stocks = self.sb.stocks[0].purchase_number
        self.assertEqual(number_of_stocks, 0)

    def test_cost_can_allocate(self):
        cost = self.sb.get_cost_can_allocate(0.1)
        self.assertAlmostEqual(cost, 50.05)

    def test_add_stock_purchase_number(self):
        self.sb.allocate_cash()
        self.assertEqual(self.sb.stocks[0].purchase_number, 1)
        self.assertEqual(self.sb.stocks[1].purchase_number, 1)
        self.assertEqual(self.sb.stocks[2].purchase_number, 7)
    
    def test_buy_at_least_one_stock_if_enough_money(self):
        self.sb.stocks[0].current_cost = 200
        self.sb.stocks[1].current_cost = 200
        self.sb.stocks[2].current_cost = 200
        self.sb.allocate_cash()
        self.assertEqual(self.sb.stocks[0].purchase_number, 1)
        self.assertEqual(self.sb.stocks[1].purchase_number, 1)
        self.assertEqual(self.sb.stocks[2].purchase_number, 0)




if __name__ == "__main__":
    unittest.main()
