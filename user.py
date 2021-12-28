import mysql.connector
from db_connection import cursor, cnt
# must install lib named cryptography
from cryptography.fernet import Fernet

key = Fernet.generate_key()
class User:
    def __init__(self, id, firstname, lastname, username, phone, email, password, role):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.phone = phone
        self.email = email
        self.password = password
        self.role = role

    def registerUser(self):
        print("Register to the System")
        self.id = input("ID: ")
        self.firstname = input("First Name: ")
        self.lastname = input("Last Name: ")
        self.username = input("Username: ")
        self.phone = input("Phone: ")
        self.email = input("Email: ")
        self.password = input("Password: ")
        self.role = input("Role: ")

        cursor.execute("SELECT * from users")
        result = cursor.fetchall()
        for user in result:
            if user[1] == self.id:
                print("User " + self.firstname + " " + self.lastname + " already exists")
                return
        newuser = ("INSERT INTO users "
                   "(id, firstname, lastname, username, phone, email, password, role) "
                   "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")

        fernet = Fernet(key)
        encodedPass = fernet.encrypt((self.password).encode())
        args = [self.id, self.firstname, self.lastname, self.username, self.phone, self.email, encodedPass, self.role]
        cursor.execute(newuser, args)
        cnt.commit()
        cursor.close()
        cnt.close()
        print("User " + self.firstname + " " + self.lastname + " created successfully.")

    def loginUser(self):
        print("Login to the System")
        self.username = input("Username: ")
        self.password = input("Password: ")

        cursor.execute("SELECT * from users")
        result = cursor.fetchall()
        for user in result:
            if user[4] == self.username:
                # password = bytes(user[7], 'utf-8')
                # encPass = Fernet(key)
                # decPass = encPass.decrypt(password)
                print("User " + self.username + " logged in")
