from user import User
from db_connection import mycursor,mydb



class Manager(User):
    def __init__(self, name, id, phone, email, role):
        super().__init__(name, id, phone, email, role)
