import mysql.connector
from db_connection import cursor, cnt


class clothingItem:
    def __init__(self, id, name, color, size, quantity,category, kind, price):
        self.id = id
        self.name = name
        self.color = color
        self.size = size
        self.quantity = quantity
        self.category = category
        self.kind = kind
        self.price = price

    # Select item by id
    def selectItemById(self):
        self.id = input("Enter Item ID: ")
        cursor.execute("SELECT * FROM clothingItems WHERE item_id='" + self.id + "'")
        # Fetch all records from table
        items = cursor.fetchall()
        if items == []:
            print("Item does not exist in system")
            return -1
        else:
            return 1


    def addItem(self):
        print("Add new item:")
        self.id = input("ID: ")
        self.name = input("Name of the Item: ")
        self.color = input("Color: ")
        self.size = input("Size: ")
        self.quantity = input("Quantity: ")
        self.category = input("Category ID: ")
        self.kind = input("Kind: ")
        self.price = input("Price: ")

        cursor.execute("SELECT * from clothingItems")
        items = cursor.fetchall()
        for item in items:
            if item[1] == self.id:
                print("Item " + self.name + " already exists")
                return
        newItem = ("INSERT INTO clothingItems "
                   "(item_id, itemname, color, size, quantity, category_id, kind, price) "
                   "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")

        args = [self.id, self.name, self.color, self.size, self.quantity, self.category, self.kind, self.price]
        cursor.execute(newItem, args)
        cnt.commit()
        cursor.close()
        cnt.close()
        print("Item " + self.name + " of category: " + self.category + " added successfully.")

    # Id change is not possible
    def updateItem(self):
        if (self.selectItemById() == -1):
            return

        print("Update item:")
        print("Which field would you like to update?\n")
        ch = 0

        # display menu until user presses 8
        while (ch < 8):
            # menu options
            print("1. Item Name")
            print("2. Color")
            print("3. Size")
            print("4. Quantity")
            print("5. Category ID")
            print("6. Kind")
            print("7. Price")
            print("8. Exit\n")
            ch = int(input("Enter Your choice: "))
            if ch == 1:
                self.name = input("Enter New Item Name: ")
                cursor.execute(
                    "UPDATE clothingItems SET itemname='" + self.name + "' WHERE item_id='" + self.id + "'")
                cnt.commit()

            if ch == 2:
                self.color = input("Enter New Color: ")
                cursor.execute(
                    "UPDATE clothingItems SET color='" + self.color + "' WHERE item_id='" + self.id + "'")
                cnt.commit()

            if ch == 3:
                self.size = input("Enter New Size: ")
                cursor.execute(
                    "UPDATE clothingItems SET size='" + self.size + "' WHERE item_id='" + self.id + "'")
                cnt.commit()

            if ch == 4:
                self.quantity = input("Enter New Quantity: ")
                cursor.execute("UPDATE clothingItems SET quantity='" + self.quantity + "' WHERE item_id='" + self.id + "'")
                cnt.commit()

            if ch == 5:
                self.category = input("Enter New Category ID: ")
                cursor.execute("UPDATE clothingItems SET category_id='" + self.category + "' WHERE item_id='" + self.id + "'")
                cnt.commit()

            if ch == 6:
                self.kind = input("Enter New Kind: ")
                cursor.execute(
                    "UPDATE clothingItems SET kind='" + self.kind + "' WHERE item_id='" + self.id + "'")
                cnt.commit()

            if ch == 7:
                self.price = input("Enter New Price: ")
                cursor.execute("UPDATE clothingItems SET price='" + self.price + "' WHERE item_id='" + self.id + "'")
                cnt.commit()

            if ch == 8:
                cursor.close()
                cnt.close()
                print("Exit Update Mode")

            #display success message
            if ch < 8:
                print(cursor.rowcount, "Record updated.\n")

    # def viewItem(self):
    #
    # def deleteItem(self, item):

