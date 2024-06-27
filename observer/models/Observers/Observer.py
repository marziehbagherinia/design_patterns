from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, stock, price):
        pass
    
    @abstractmethod
    def print(self):
        pass