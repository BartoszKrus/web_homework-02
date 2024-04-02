from address_book import AddressBook
from display.console_display_strategy import ConsoleDisplayStrategy
from fields.field import Field
from records.record import Record
from validators.data_validator import DateValidator
from validators.email_validator import EmailValidator
from validators.phone_validator import PhoneValidator

if __name__ == "__main__":
    address_book = AddressBook()
    record1 = Record("John Doe")
    record1.phone.add_phone("123456789")
    record1.phone.add_phone("123456789")
    record1.phone.add_phone("123456789")
    record1.phone.add_phone("123456789")
    record1.birthday.add_birthday("15-05-1990")
    record1.info.add_note("Rodzina", "Mam żonę.")
    record1.info.add_note("Zwierzęta", "Mam dwa psy i jednego kota.")
    record1.address.add_address("ul. Zachlapana 13, 01-200 Warszawa")
    record1.email.add_email("john.doe@gmail.com")

    record2 = Record("Jane Smith")
    record2.phone.add_phone("987654321")
    record2.birthday.add_birthday("30-11-1988")

    record3 = Record("Alice Wonderland")
    record3.phone.add_phone("555888777")
    record3.birthday.add_birthday("20-03-1995")

    address_book.add_record(record1)
    address_book.add_record(record2)
    address_book.add_record(record3)

    print("\n")
    
    console_display_strategy = ConsoleDisplayStrategy()

    address_book.display_all(console_display_strategy)
