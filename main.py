import mysql.connector
from db_connection import cursor, cnt
from user import User
from clothingItem import clothingItem
import base64
import sys

# person = User(111111122, 'Bono', 'nnb', 'bbbbb', '0501231345', 'bob@gmail.com', '123123', 'Manager')
# person.registerUser()
#
# person.loginUser()

item = clothingItem(2, 'Long Denim', 'Indigo', 'S', 300 , 3, 'Long', 215)

# item.addItem()
# item.updateItem()

# item.viewItem()
# item.deleteItem()