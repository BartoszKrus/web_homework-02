from abc import ABC, abstractmethod
import re

class Validator(ABC):
    @abstractmethod
    def validate(self, value):
        pass

class EmailValidator(Validator):
    def validate(self, value):
        if value is not None:
            check = re.findall(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', value)
            if len(check) != 1:
                raise ValueError('Incorrect email address')
