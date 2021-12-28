import mysql.connector

cnt = mysql.connector.connect(user='root', password="Nitbys270591", database='inventory_box')
cursor = cnt.cursor()
