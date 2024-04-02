from fields.field import Field
from validators.data_validator import DateValidator
from datetime import datetime


class RecordBirthday:
    def __init__(self, birthday=None):
        self.birthday = Field(birthday, DateValidator())

    def add_birthday(self, birthday):
        self.birthday.set_value(birthday)

    def edit_birthday(self, new_birthday):
        self.birthday.set_value(new_birthday)

    def remove_birthday(self):
        self.birthday.set_value(None)

    def days_to_birthday(self):
        if self.birthday.get_value():
            today = datetime.today()
            birthday_date = datetime.strptime(self.birthday.get_value(), '%d-%m-%Y')
            next_birthday = datetime(today.year, birthday_date.month, birthday_date.day)
            if today > next_birthday:
                next_birthday = datetime(today.year + 1, birthday_date.month, birthday_date.day)
            delta = next_birthday - today
            return delta.days
        else:
            return None