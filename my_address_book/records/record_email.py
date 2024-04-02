from fields.field import Field
from validators.email_validator import EmailValidator

class RecordEmail:
    def __init__(self, email=None):
        self.email = Field(email, EmailValidator())
        
    def add_email(self, email):
        self.email.set_value(email)

    def edit_email(self, new_email):
        self.email.set_value(new_email)

    def remove_email(self):
        self.email.set_value(None)   