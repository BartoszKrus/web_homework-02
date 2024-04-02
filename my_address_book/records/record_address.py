from fields.field import Field

class RecordAddress:
    def __init__(self, address=None):
        self.address = Field(address)

    def add_address(self, address):
        self.address.set_value(address)

    def edit_address(self, new_address):
        self.address.set_value(new_address)

    def remove_address(self):
        self.address.set_value(None)