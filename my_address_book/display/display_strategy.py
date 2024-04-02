from abc import ABC, abstractmethod

class DisplayStrategy(ABC):
    @abstractmethod
    def display(self, record):
        pass