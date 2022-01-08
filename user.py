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
)