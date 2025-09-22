from models.user import User

class UserBuilder: # Provides methods to set optional fields and returns self for chaining
    def __init__(self, user_id, name, role): # Required fields
        self.user_id = user_id
        self.name = name
        self.role = role
        self.email = None
        self.phone = None
        self.address = None

    def with_email(self, email):  # sets a email field
        self.email = email # sets the email field
        return self # returns self for chaining

    def with_phone(self, phone):
        self.phone = phone
        return self

    def with_address(self, address):
        self.address = address
        return self

    def build(self): # returns a User object
        return User(self.user_id, self.name, self.role, self.email, self.phone, self.address) # Returns a User object(Final object)
