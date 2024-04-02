from abc import ABC, abstractmethod
from datetime import datetime

class Validator(ABC):
    @abstractmethod
    def validate(self, value):
        pass

class DateValidator(Validator):
    def validate(self, value):
        try:
            datetime.strptime(value, "%d-%m-%Y")
        except ValueError:
            raise ValueError("Birthday must be in 'dd-mm-yyyy' format.")
