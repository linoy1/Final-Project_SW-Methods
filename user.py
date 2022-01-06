from db_connection import mycursor
import mysql.connector

mydb = mysql.connector.connect( host="localhost",user="root",password="Tr12a15s-19",database="Inventory_Management_Box")

mycursor = mydb.cursor()


class User:
    def __init__(self,id,firstname,lastname, username,phone,email, password,role):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.phone = phone
        self.email = email
        self.password = password
        self.role = role

#####create table#####
# mycursor.execute("CREATE TABLE User (id int auto_increment primary key, name varchar(255),phone int(255),"
#                  "email varchar(255),password varchar(50),username varchar(50),type varchar(50))")

###### insert user into system########
# sql = "INSERT INTO User (id, name, phone, email, password, username, type) VALUES (%s, %s, %s, %s, %s, %s, %s)"
# val = ("123456", "Linoy Siman Tov", "0537404026", "lin.si.tov@gmail.com", "linoy123", "linoy1", "storekeeper")
# mycursor.execute(sql, val)
#
# mydb.commit()

# print(mycursor.rowcount, "record inserted.")

#
# mycursor.execute("DESCRIBE User")
# for i in mycursor:
#     print(i)

#
# mycursor.execute("SELECT * FROM User")
#
# myresult = mycursor.fetchall()
#
# for x in myresult:
#   print(x)