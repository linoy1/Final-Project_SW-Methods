from self import self
from user import User
from storekeeper import Storekeeper, insert_storekeeper, update_storekeeper, selectStorekeeperById, \
    selectAllStorekeepers

from db_connection import cursor, cnt


class Manager(User):
    def __init__(self, id, firstname, lastname, username, phone, email, password, role):
        super().__init__(id, firstname, lastname, username, phone, email, password, role)

    def insert_storekeeper(self):
        super().insert_storekeeper()

    def update_storekeeper(self):
        super().update_storekeeper()

    def selectStorekeeperById(self):
        super().selectStorekeeperById()

    def selectAllStorekeepers(self):
        super().selectAllStorekeepers()


####select selectManagerById#####
def selectManagerById(self):
    self.id = input("Enter manager ID:")
    cursor.execute("SELECT * FROM users WHERE id='" + self.id + "'")
    # Fetch all records from table
    res = cursor.fetchall()
    if res == []:
        print("\n")
        print("user not exists!")
        print("\n")
        return -1
    else:
        print("------------------------------------------------------------------------")
        print("id   firstname   lastname    username    phone   email   password    role")
        print("------------------------------------------------------------------------")

    for x in res:
        print(x[0], "  ", x[1], "  ", x[2], "  ", x[3], "  ", x[4], "  ", x[5], "  ", x[6], "  ", x[7])
    print("------------------------------------------------------------------------")


#####select all managers#####
# Execute SELECT statement
def selectAllManagers():
    cursor.execute("SELECT * FROM users WHERE role='"+'Manager'+"'")
    res = cursor.fetchall()

    print("------------------------------------------------------------------------")
    print("id   firstname   lastname    username    phone   email   password    role")
    print("------------------------------------------------------------------------")

    for x in res:
        print(x[0], "  ", x[1], "  ", x[2], "  ", x[3], "  ", x[4], "  ", x[5], "  ", x[6], "  ", x[7])
    print("------------------------------------------------------------------------")


####insert manager#####
def insert_manager(self):
    # read values to be inserted
    self.id = input("ID: ")
    # check if user exist
    cursor.execute("SELECT * from users WHERE id='" + self.id + "'")
    result = cursor.fetchone()
    if result != None:
        print("user already exists!")
        print("\n")
        return

    else:
        self.firstname = input("First Name: ")
        self.lastname = input("Last Name: ")
        self.username = input("Username: ")
        self.phone = input("Phone: ")
        self.email = input("Email: ")
        self.password = input("Password: ")
        self.role = input("Role: ")
        # create the Insert query
        sql = (
            "INSERT INTO users ( id, firstname,lastname, username,phone,email, password,role) VALUES (%s, %s,%s, %s,%s, %s,%s,%s)")
        # create list of values typed from user to insert in customer table
        val = [self.id, self.firstname, self.lastname, self.username, self.phone, self.email, self.password, self.role]
        # Execute query with values
        cursor.execute(sql, val)
        # commit for permanent storage in database
        cnt.commit()
        # display success message
        print(cursor.rowcount, "Record inserted.")
        # cursor.close()
        # cnt.close()


##update storekeepers#####
def update_user(self):
    # read values to be updated
    # self.id = input("Enter storekeeper ID:")
    if (selectManagerById(self) == -1):
        return

    print("which field do you want update?")
    ch = 0
    # display menu until user presses 8
    while (ch < 8):
        # menu options
        print("1. Firstname")
        print("2. Lastname")
        print("3. Username")
        print("4. Phone")
        print("5. Email")
        print("6. Password")
        print("7. Role")
        print("8. Exit")
        ch = int(input("Enter Your choice:"))
        if (ch == 1):
            self.firstname = input("Enter new first name:")
            # create update query
            cursor.execute("UPDATE users SET firstname='" + self.firstname + "' WHERE id='" + self.id + "'")
            # commit Changes to DB
            cnt.commit()
        if (ch == 2):
            self.lastname = input("Enter new last name:")
            # create update query
            cursor.execute("UPDATE users SET lastname='" + self.lastname + "' WHERE id='" + self.id + "'")
            # commit Changes to DB
            cnt.commit()
        if (ch == 3):
            self.username = input("Enter new username:")
            # create update query
            cursor.execute("UPDATE users SET username='" + self.username + "' WHERE id='" + self.id + "'")
            # commit Changes to DB
            cnt.commit()
        if (ch == 4):
            self.phone = input("Enter new phone:")
            # create update query
            cursor.execute("UPDATE users SET phone='" + self.phone + "' WHERE id='" + self.id + "'")
            # commit Changes to DB
            cnt.commit()

        if (ch == 5):
            self.email = input("Enter new email:")
            # create update query
            cursor.execute("UPDATE users SET email='" + self.email + "' WHERE id='" + self.id + "'")
            # commit Changes to DB
            cnt.commit()
        if (ch == 6):
            self.password = input("Enter new password:")
            # create update query
            cursor.execute("UPDATE users SET password='" + self.password + "' WHERE id='" + self.id + "'")
            # commit Changes to DB
            cnt.commit()
        if (ch == 7):
            self.role = input("Enter new role:")
            # create update query
            cursor.execute("UPDATE users SET role='" + self.role + "' WHERE id='" + self.id + "'")
            # commit Changes to DB
            cnt.commit()

        # #display success message
        print(cursor.rowcount, "Record updated.")
        print('\n')


def delete_user(self):
    self.id = input("Enter manager ID:")
    cursor.execute("SELECT * FROM users WHERE id='" + self.id + "'")
    # Fetch all records from table
    res = cursor.fetchall()
    if res == []:
        print("\n")
        print("user not exists!")
        print("\n")
    else:
    # Create Delete Query
        sql = "DELETE FROM users where id = '" + self.id + "'"
    # execute delete query
        cursor.execute(sql)
    # commit changes to DB
        cnt.commit()
    # display success message
        print(cursor.rowcount, "Record deleted.")




def main():
    # open cursor
    ch = 0
    # display menu until user presses 5
    while (ch <= 10):
        # menu options
        print("1. Display Specific Manager")
        print("2. Display All Managers")
        print("3. Register New Manager")
        print("4. Update Manager")
        print("5. Display Specific Storekeeper")
        print("6. Display All Storekeepers")
        print("7. Register New Storekeeper")
        print("8. Update Storekeeper")
        print("9. Delete User")
        print("10. Exit")
        # ask user to enter what he wants to do
        ch = int(input("Enter Your Choice:"))
        # call relevant functions defined above
        if (ch == 1):
            selectManagerById(self)
        if (ch == 2):
            selectAllManagers()
        if (ch == 3):
            insert_manager(self)
        if (ch == 4):
            update_user(self)
        if (ch == 5):
            selectStorekeeperById(self)
        if (ch == 6):
            selectAllStorekeepers()
        if (ch == 7):
            insert_storekeeper(self)
        if (ch == 8):
            update_storekeeper(self)
        if (ch == 9):
            delete_user(self)
# call main
main()
