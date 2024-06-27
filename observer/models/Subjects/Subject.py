from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def register(self, observer):
        pass
    @abstractmethod
    def unregister(self, observer):
        pass    
    @abstractmethod
    def notify(self, data):
        pass
