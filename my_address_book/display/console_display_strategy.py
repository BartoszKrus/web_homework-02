from display.display_strategy import DisplayStrategy

class ConsoleDisplayStrategy(DisplayStrategy):
    def display(self, record):
        print("Name:", record.name)
        print("Phone:", ', '.join([str(phone.get_value()) for phone in record.phone.phones]))
        print("Birthday:", record.birthday.birthday.get_value())
        print("Address:", record.address.address.get_value())
        print("Email:", record.email.email.get_value())
        print("Info:")
        for key, value in record.info.notes.items():
            print(f"{key.get_value()} -> {value.get_value()}")
        print("\n")