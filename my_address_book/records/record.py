from records.record_phone import RecordPhone
from records.record_birthday import RecordBirthday
from records.record_address import RecordAddress
from records.record_email import RecordEmail
from records.record_info import RecordInfo
from fields.field import Field
from display.display_strategy import DisplayStrategy

class Record:
    def __init__(self, name):
        self.name = name
        self.phone = RecordPhone()
        self.birthday = RecordBirthday()
        self.address = RecordAddress()
        self.email = RecordEmail()
        self.info = RecordInfo()

    def display(self, display_strategy):
        display_strategy.display(self)
