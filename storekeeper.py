from self import self
from user import User
from db_connection import mycursor, mydb

class Storekeeper(User):
    def __init__(self, id ,firstname, lastname, username, phone, email, password, role):
        super().__init__(id, firstname, lastname, username, phone, email, password, role)
####select selectStorekeeperById#####
def selectStorekeeperById(self):
    self.id = input("Enter storekeeper ID:")
    mycursor.execute("SELECT * FROM storekeepers WHERE id='"+self.id+"'")
    # Fetch all records from table
    res = mycursor.fetchall()
    if res== []:
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

#####select all storekeepers#####
# Execute SELECT statement
def selectAllStorekeepers():
    mycursor.execute("SELECT * FROM storekeepers")
    res = mycursor.fetchall()

    print("------------------------------------------------------------------------")
    print("id   firstname   lastname    username    phone   email   password    role")
    print("------------------------------------------------------------------------")

    for x in res:
        print(x[0], "  ", x[1], "  ", x[2], "  ", x[3], "  ", x[4], "  ", x[5], "  ", x[6], "  ", x[7])
    print("------------------------------------------------------------------------")

####insert storekeeper#####
def insert_user(self):
    # read values to be inserted
    self.id = input("ID: ")
    #check if user exsist
    mycursor.execute("SELECT * from storekeepers WHERE id='"+self.id+"'")
    result = mycursor.fetchone()
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
        sql = ("INSERT INTO storekeepers ( id, firstname,lastname, username,phone,email, password,role) VALUES (%s, %s,%s, %s,%s, %s,%s,%s)")
# create list of values typed from user to insert in customer table
        val = [self.id, self.firstname,self.lastname, self.username,self.phone,self.email, self.password, self.role]
# Execute query with values
        mycursor.execute(sql, val)
# commit for permanent storage in database
        mydb.commit()
# display success message
        print(mycursor.rowcount, "Record inserted.")
        mycursor.close()
        mydb.close()


# ##update storekeepers#####
# # def update_user(self):
#     # read values to be updated
#     id = input("Enter customer ID:")
#     mycursor.execute("SELECT * FROM storekeepers WHERE id='"+id+"'")
#     oldUserDetails = mycursor.fetchall()
#     print(oldUserDetails[0][1])
#     # for user in oldUserDetails:
#     #     if(user[0]== self.id):
#     #         name=user[1]
#     #         print(name)
#     #
#     #     self.firstname = input("Enter customer Name:")
#     #     self.lastname = input("Enter customer Name:")
#     #     self.username = input("Enter customer username:")
#     #     self.phone = input("Enter customer Phone:")
#     #     self.email = input("Enter customer Email:")
#     #     self.password = input("Enter customer password:")
#     #     self.role = input("Enter customer role:")
#
#     # #create update query
#     # mycursor.execute("UPDATE storekeepers SET name='"+self.firstname+"', phone='"+cph+"', email='"+cem+"', password='"+cps+"', username='"+cun+"', type='"+ctp+"' WHERE id="+id)
#     # #commit Changes to DB
#     mydb.commit()
#     # #display success message
#     print(mycursor.rowcount, "Record updated.")

##update storekeepers#####
def update_user(self):
    # read values to be updated
    # self.id = input("Enter storekeeper ID:")
    if(selectStorekeeperById(self) == -1):
        return

    print("which field do you want update?")
    ch = 0
    # diaplay menu until user presses 8
    while (ch < 7):
        # menu options
        print("1. firstname")
        print("2. lastname")
        print("3. username")
        print("4. phone")
        print("5. email")
        print("6. password")
        print("7. role")
        print("8. exit")
        ch = int(input("Enter Your choice:"))
        if (ch == 1):
            self.firstname = input("Enter new first name:")
        # create update query
            mycursor.execute("UPDATE storekeepers SET firstname='" + self.firstname + "' WHERE id='"+ self.id+"'")
        # commit Changes to DB
            mydb.commit()
        if (ch == 2):
            self.lastname = input("Enter new last name:")
        # create update query
            mycursor.execute("UPDATE storekeepers SET lastname='" + self.lastname + "' WHERE id='"+ self.id+"'")
        # commit Changes to DB
            mydb.commit()
        if (ch == 3):
            self.username = input("Enter new username:")
        # create update query
            mycursor.execute("UPDATE storekeepers SET username='" + self.username + "' WHERE id='"+ self.id+"'")
        # commit Changes to DB
            mydb.commit()
        if (ch == 4):
            self.phone = input("Enter new phone:")
        # create update query
            mycursor.execute("UPDATE storekeepers SET phone='" + self.phone + "' WHERE id='"+ self.id+"'")
        # commit Changes to DB
            mydb.commit()
        if (ch == 5):
            self.email = input("Enter new email:")
        # create update query
            mycursor.execute("UPDATE storekeepers SET email='" + self.email + "' WHERE id='"+ self.id+"'")
        # commit Changes to DB
            mydb.commit()
        if (ch == 6):
            self.password = input("Enter new password:")
        # create update query
            mycursor.execute("UPDATE storekeepers SET password='" + self.password + "' WHERE id='"+ self.id+"'")
        # commit Changes to DB
            mydb.commit()
        if (ch == 7):
            self.role = input("Enter new role:")
        # create update query
            mycursor.execute("UPDATE storekeepers SET role='" + self.role + "' WHERE id='"+ self.id+"'")
        # commit Changes to DB
            mydb.commit()

        # #display success message
        print(mycursor.rowcount, "Record updated.")
        print('\n')


def main():
    # open cursor
    ch = 0
    # diaplay menu until user presses 5
    while (ch <= 4):
        # menu options
        print("1. INSERT")
        print("2. UPDATE")
        # print("3. DELETE")
        print("3. DISPLAY SPECIFIC STOREKEEPER")
        print("4. DISPLAY ALL STOREKEEPERS")
        print("5. EXIT")
        # ask user to enter what he wants to do
        ch = int(input("Enter Your choice:"))
        # call relevant fucntions defined above
        if (ch == 1):
            insert_user(self)
        if (ch == 2):
            update_user(self)
        # if (ch == 3):
        #     delete(con, cur)
        if (ch == 3):
            selectStorekeeperById(self)
        if (ch == 4):
            selectAllStorekeepers()


# call main
main()