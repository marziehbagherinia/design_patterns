from models.Subjects.Subject import *

class StockManager(Subject):
    def __init__(self):
        self.observers = []
        self.stocks = {}

    def register(self, observer):
        self.observers.append(observer)
        self.init_observer_data(observer)

    def unregister(self, observer):
        self.observers.remove(observer)

    def notify(self, stock):
        for observer in self.observers:
            observer.update(stock, self.stocks[stock])

    def init_observer_data(self, observer):
        for key, value in self.stocks.items():
            observer.update(key, value)

    def set_stock_price(self, stock, price):
        self.stocks[stock] = price
        self.notify(stock)