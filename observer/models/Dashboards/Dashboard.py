from models.Observers.Observer import *

class Dashboard(Observer):
    def __init__(self):
        self.stocks = {}

    def update(self, stock, price):
        self.stocks[stock] = price

    def getData(self):
        return self.stocks
    
    def print(self):
        print("Dashboard Data:")
        for key, value in self.stocks.items():
            print(f"{key}: {value}")
        print()