
import mysql.connector
from db_connection import cursor, cnt
from user import User
from clothingItem import clothingItem
import base64
import sys

person = User(305365455, 'Bob', 'Daniels', 'Bobbyboo', '0501231345', 'bob@gmail.com', 'bob123456', 'Manager')
# person.registerUser()

# person.loginUser()

item = clothingItem(1, 'Short Blouse', 'Beige', 'M', 150 , 1, 'Short', 159.99)

# item.addItem()
item.updateItem()
