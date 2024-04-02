class AddressBook:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def display_all(self, display_strategy):
        for record in self.records:
            record.display(display_strategy)