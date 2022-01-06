import mysql.connector
from db_connection import cursor, cnt

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

        args = [self.id, self.firstname, self.lastname, self.username, self.phone, self.email, self.password, self.role]
        cursor.execute(newuser, args)
        cnt.commit()
        cursor.close()
        cnt.close()
        print("User " + self.firstname + " " + self.lastname + " created successfully.")

    def loginUser(self):
        user_d = []
        print("Login to the System")
        self.username = input("Username: ")
        self.password = input("Password: ")

        cursor.execute("SELECT * from users")
        result = cursor.fetchall()
        for user in result:
            if user[4] == self.username:
                password = user[7].decode('UTF-8')
                if password == self.password:
                    print("User " + self.username + " logged in successfully")
                else:
                    print("Passwords don't match, try again")
                    return
            elif user[4] != self.username:
                user_d = [user[4]]
                continue

        if user_d[0] != self.username:
            print("Username does not exist in the system")
