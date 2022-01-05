import mysql.connector

mydb = mysql.connector.connect( host="localhost",user="root",password="Tr12a15s-19",database="Inventory_Management_Box")

mycursor = mydb.cursor()
# mycursor.execute("show databases")

#
# for i in mycursor:
#     print(i)