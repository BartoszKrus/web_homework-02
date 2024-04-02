from abc import ABC, abstractmethod

class Field:
    def __init__(self, value=None, validator=None):
        self.value = value
        self.validator = validator

    def set_value(self, value):
        if self.validator:
            self.validator.validate(value)
        self.value = value

    def get_value(self):
        return self.value
