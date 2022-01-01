
# from cryptography.fernet import Fernet
# import mysql.connector

# cnt = mysql.connector.connect(user='root', password="Nitbys270591", database='inventory_box')
# cursor = cnt.cursor()

# key = Fernet.generate_key()
# fernet = Fernet(key)

# cursor.execute("SELECT * from checks")
# result = cursor.fetchall()

# query = ("INSERT INTO checks "
#                    "(pass) "
#                    "VALUES (%s)")

# encodedPass = fernet.encrypt('nitsan2345'.encode('utf-8'))
# cursor.execute(query, encodedPass)
# cnt.commit()
# cursor.close()
# cnt.close()
