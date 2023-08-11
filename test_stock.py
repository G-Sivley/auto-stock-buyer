import unittest


from stock import Stock

class TestStock(unittest.TestCase):
    def test_init_object(self):
        s = Stock(ticker="SCHB", current_cost=272.2, percet_allocation=0.4)
        print(s.current_cost)
        self.assertIsInstance(s, Stock)
    

if __name__ == "__main__":
    unittest.main()