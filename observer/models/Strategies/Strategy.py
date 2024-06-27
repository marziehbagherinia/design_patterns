from models.Observers.Observer import *

class Strategy(Observer):
    def __init__(self, name):
        self.name = name
        self.stocks = {}

    def update(self, stock, price):
        self.stocks[stock] = price

    def print(self):
        print(f"Strategy {self.name} Data:")
        for key, value in self.stocks.items():
            print(f"{key}: {value}")
        print()
