from fields.field import Field
from validators.phone_validator import PhoneValidator

class RecordPhone:
    def __init__(self, phone=None, phones=None):
        self.phone = Field(phone, PhoneValidator())
        self.phones = phones if phones else []

    def add_phone(self, phone):
        new_phone = Field(validator=PhoneValidator())
        new_phone.set_value(phone)
        self.phones.append(new_phone)

    def remove_phone(self, phone):
        phone_to_remove = str(phone)
        if phone_to_remove in [str(p.get_value()) for p in self.phones]:
            self.phones = [p for p in self.phones if str(p.get_value()) != phone_to_remove]

    def edit_phone(self, old_phone, new_phone):
        old_phone_obj = Field(old_phone)
        for i, phone in enumerate(self.phones):
            if str(phone.get_value()) == str(old_phone_obj.get_value()):
                self.phones[i] = Field(new_phone, PhoneValidator())
                return
        print("Old phone number not found.")