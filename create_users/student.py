class Student:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    def get_query_for_creation(self):
        return {
            "email": self.email,
            "password": self.id,
            "username": self.id,
            "name": self.name
        }