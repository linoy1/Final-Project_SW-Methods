from user import User
from db_connection import mycursor,mydb



class Manager(User):
    def __init__(self, name, id, phone, email, role):
        super().__init__(name, id, phone, email, role)

        ####create table#####
        mycursor.execute("CREATE TABLE Manager (id int auto_increment primary key, name varchar(255),phone varchar(255),"
                         "email varchar(255),password varchar(50),username varchar(50),type varchar(50))")
#
#
#         #####insert manager#####
#         # read values to be inserted
#         cid = input("Enter customer ID:")
#         cnm = input("Enter customer Name:")
#         cph = input("Enter customer Phone:")
#         cem = input("Enter customer Email:")
#         cps = input("Enter customer password:")
#         cun = input("Enter customer username:")
#         ctp = input("Enter customer type:")
#
#         # create the Insert query
#         sql = "INSERT INTO manager ( id, name, phone, email, password,username,type) VALUES (%s, %s,%s, %s,%s, %s,%s)"
#         # create list of values typed from user to insert in customer table
#         val = (cid, cnm, cph, cem, cps,cun,ctp)
#         # Execute query with values
#         mycursor.execute(sql, val)
#         # commit for permanent storage in database
#         mydb.commit()
#         # display success message
#         print(mycursor.rowcount, "Record inserted.")
#
#         def update(con, cur):
#             # read values to be updated
#             cid = input("Enter customer ID:")
#             cnm = input("Enter customer Name:")
#             cad = input("Enter customer Address:")
#             cph = input("Enter customer Phone:")
#             cem = input("Enter customer Email:")
#             cct = input("Enter customer City:")
#             # create update query
#             sql = "update customer set CustName='" + cnm + "', CustAddress='" + cad + "',CustPhone='" + cph + "', CustEmail='" + cem + "', CustCity='" + cct + "' where CustID=" + cid
#             # Execute Update query on opened cursor
#             cur.execute(sql)
#             # commit Changes to DB
#             con.commit()
#             # display success message
#             print(cur.rowcount, "Record updated.")
#
#         def delete(con, cur):
#             # read the customer ID for which record to be deleted
#             cid = input("Enter customer ID to delete:")
#             # Create Delete Query
#             sql = "delete FROM customer where CustID = '" + cid + "'"
#             # execute delete query
#             cur.execute(sql)
#             # commit changes to DB
#             con.commit()
#             # display success message
#             print(cur.rowcount, "Record deleted.")
#
#         def display(cur):
#             # Execute SELECT statement
#             cur.execute("SELECT * FROM customer")
#             # Fetch all records from table
#             res = cur.fetchall()
#             # print
#             print("------------------------------------------------------------------------")
#             print("CustID   CustName    CustAddress     CustCity   CustPhone   CustEmail")
#             print("------------------------------------------------------------------------")
#
#             for x in res:
#                 print(str(x[0]) + "  " + x[1] + "  " + x[2] + "  " + x[5] + "  " + x[3] + "  " + x[4])
#             print("------------------------------------------------------------------------")
#
#         def main():
#             # make connection to database using localhost, root as username, no password so "" and database name
#             con = mysql.connector.connect(
#                 host="localhost",
#                 user="root",
#                 passwd="",
#                 database="bikerentdb"
#             )
#             # opne cursor
#             cur = con.cursor()
#             ch = 0
#             # diaplay menu until user presses 5
#             while (ch <= 4):
#                 # menu options
#                 print("1. INSERT")
#                 print("2. UPDATE")
#                 print("3. DELETE")
#                 print("4. DISPLAY")
#                 print("5. EXIT")
#                 # ask user to enter what he wants to do
#                 ch = int(input("Enter Your choice:"))
#                 # call relevant fucntions defined above
#                 if (ch == 1):
#                     insert(con, cur)
#                 if (ch == 2):
#                     update(con, cur)
#                 if (ch == 3):
#                     delete(con, cur)
#                 if (ch == 4):
#                     display(cur)
#
#         # call main
#         main()
#     # import the module
#
#
# import mysql.connector
#
#
# def insert(con, cur):
#     # read values to be inserted
#     cid = input("Enter customer ID:")
#     cnm = input("Enter customer Name:")
#     cad = input("Enter customer Address:")
#     cph = input("Enter customer Phone:")
#     cem = input("Enter customer Email:")
#     cct = input("Enter customer City:")
#     # create the Insert query
#     sql = "INSERT INTO customer (CustID, CustName, CustAddress,CustPhone, CustEmail, CustCity) VALUES (%s, %s,%s, %s,%s, %s)"
#     # create list of values typed from user to insert in customer table
#     val = (cid, cnm, cad, cph, cem, cct)
#     # Execute query with values
#     cur.execute(sql, val)
#     # commit for permanent storage in database
#     con.commit()
#     # display success message
#     print(cur.rowcount, "Record inserted.")
#
#
# def update(con, cur):
#     # read values to be updated
#     cid = input("Enter customer ID:")
#     cnm = input("Enter customer Name:")
#     cad = input("Enter customer Address:")
#     cph = input("Enter customer Phone:")
#     cem = input("Enter customer Email:")
#     cct = input("Enter customer City:")
#     # create update query
#     sql = "update customer set CustName='" + cnm + "', CustAddress='" + cad + "',CustPhone='" + cph + "', CustEmail='" + cem + "', CustCity='" + cct + "' where CustID=" + cid
#     # Execute Update query on opened cursor
#     cur.execute(sql)
#     # commit Changes to DB
#     con.commit()
#     # display success message
#     print(cur.rowcount, "Record updated.")
#
#
# def delete(con, cur):
#     # read the customer ID for which record to be deleted
#     cid = input("Enter customer ID to delete:")
#     # Create Delete Query
#     sql = "delete FROM customer where CustID = '" + cid + "'"
#     # execute delete query
#     cur.execute(sql)
#     # commit changes to DB
#     con.commit()
#     # display success message
#     print(cur.rowcount, "Record deleted.")
#
#
# def display(cur):
#     # Execute SELECT statement
#     cur.execute("SELECT * FROM customer")
#     # Fetch all records from table
#     res = cur.fetchall()
#     # print
#     print("------------------------------------------------------------------------")
#     print("CustID   CustName    CustAddress     CustCity   CustPhone   CustEmail")
#     print("------------------------------------------------------------------------")
#
#     for x in res:
#         print(str(x[0]) + "  " + x[1] + "  " + x[2] + "  " + x[5] + "  " + x[3] + "  " + x[4])
#     print("------------------------------------------------------------------------")
#
#
# def main():
#     # make connection to database using localhost, root as username, no password so "" and database name
#     con = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         passwd="",
#         database="bikerentdb"
#     )
#     # opne cursor
#     cur = con.cursor()
#     ch = 0
#     # diaplay menu until user presses 5
#     while (ch <= 4):
#         # menu options
#         print("1. INSERT")
#         print("2. UPDATE")
#         print("3. DELETE")
#         print("4. DISPLAY")
#         print("5. EXIT")
#         # ask user to enter what he wants to do
#         ch = int(input("Enter Your choice:"))
#         # call relevant fucntions defined above
#         if (ch == 1):
#             insert(con, cur)
#         if (ch == 2):
#             update(con, cur)
#         if (ch == 3):
#             delete(con, cur)
#         if (ch == 4):
#             display(cur)
#
#
# # call main
# main()
#
