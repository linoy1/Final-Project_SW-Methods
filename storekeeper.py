from user import User
from db_connection import mycursor, mydb


class Storekeeper(User):
    def __init__(self, id, name, phone, email, password,username,type):
        super().__init__(id, name, phone, email, password,username,type)
#####insert storekeeper#####
# def insert_user(self):
# # read values to be inserted
#     self.id = input("Enter customer ID:")
#     self.name = input("Enter customer Name:")
#     self.phone = input("Enter customer Phone:")
#     self.email = input("Enter customer Email:")
#     self.password = input("Enter customer password:")
#     self.username = input("Enter customer username:")
#     self.type = input("Enter customer type:")
#
#     # create the Insert query
#     sql = "INSERT INTO storekeepers ( id, name, email, password,username,type,phone) VALUES (%s, %s,%s, %s,%s, %s,%s)"
#     # create list of values typed from user to insert in customer table
#     val = (id, name, phone, email, password,username,type)
#     # Execute query with values
#     mycursor.execute(sql, val)
#     # commit for permanent storage in database
#     mydb.commit()
#     # display success message
#     print(mycursor.rowcount, "Record inserted.")

###update storekeepers#####
# read values to be updated
cid = input("Enter new storekeeper ID:")

mycursor.execute("SELECT * FROM storekeepers WHERE id='"+cid+"'")
oldDetail = mycursor.fetchall()

cnm = input("Enter new storekeeper Name:")
cph = input("Enter new storekeeper Phone:")
cem = input("Enter new storekeeper Email:")
cps = input("Enter new storekeeper password:")
cun = input("Enter new storekeeper username:")
ctp = input("Enter new storekeeper type:")
cph = input("Enter new storekeeper Phone:")

#create update query
mycursor.execute("update storekeepers set name='"+cnm+"', phone='"+cph+"', email='"+cem+"', password='"+cps+"', username='"+cun+"', type='"+ctp+"' where id="+cid)
#commit Changes to DB
mydb.commit()
#display success message
print(mycursor.rowcount, "Record updated.")



#####select specific storekeeper#####

# Execute SELECT statement
# cid = input("Enter new storekeeper ID:")
#
# mycursor.execute("SELECT * FROM storekeepers WHERE id='"+cid+"'")
# # Fetch all records from table
#
# res = mycursor.fetchall()
#
# # print
# print("------------------------------------------------------------------------")
# print("id   name    email  password     username    type    phone")
# print("------------------------------------------------------------------------")
#
# for x in res:
#     print(x[0], "  ", x[1], "  ", x[2], "  ", x[3], "  ", x[4], "  ", x[5], "  ", x[6])
# print("------------------------------------------------------------------------")

#####select all storekeepers#####

#Execute SELECT statement

# mycursor.execute("SELECT * FROM storekeepers")
# # Fetch all records from table
#
# res = mycursor.fetchall()
#
# # print
# print("------------------------------------------------------------------------")
# print("id   name    email  password     username    type    phone")
# print("------------------------------------------------------------------------")
#
# for x in res:
#     print(x[0], "  ", x[1], "  ", x[2], "  ", x[3], "  ", x[4], "  ", x[5], "  ", x[6])
# print("------------------------------------------------------------------------")
#