from abc import ABC, abstractmethod

class Validator(ABC):
    @abstractmethod
    def validate(self, value):
        pass

class PhoneValidator(Validator):
    def validate(self, value):
        if not value.isdigit():
            raise ValueError("The phone number must contain only digits.")
        if len(value) != 9:
            raise ValueError("Phone number must contain exactly 9 digits.")
