from self import self

from db_connection import cursor, cnt


class Category():
    def __init__(self, id, name):
        self.id = id
        self.name = name


####select category by id#####
def selectCategoryById(self):
    self.id = input("Enter category ID:")
    cursor.execute("SELECT * FROM categories WHERE id='" + self.id + "'")
    # Fetch all records from table
    res = cursor.fetchall()
    if res == []:
        print("\n")
        print("category not exists!")
        print("\n")
        return -1
    else:
        print("-------------------")
        print("categoryNum  id   categoryName")
        print("-------------------")

    for x in res:
        print(x[0], "  ", x[1], "  ", x[2])
    print("-------------------")


#####select all categories#####
# Execute SELECT statement
def selectAllCategory():
    cursor.execute("SELECT * FROM categories")
    res = cursor.fetchall()

    print("-------------------")
    print("categoryNum id   categoryName")
    print("-------------------")

    for x in res:
        print(x[0], "  ", x[1], "  ", x[2])
    print("-------------------")


####insert category#####
def insert_category(self):
    # read values to be inserted
    self.id = input("ID: ")
    # check if user exist
    cursor.execute("SELECT * from categories WHERE id='" + self.id + "'")
    result = cursor.fetchone()
    if result != None:
        print("category already exists!")
        print("\n")
        return

    else:
        self.name = input("Category Name: ")
        # create the Insert query
        sql = ("INSERT INTO categories ( id, name) VALUES (%s, %s)")
        # create list of values typed from user to insert in customer table
        val = [self.id, self.name]
        # Execute query with values
        cursor.execute(sql, val)
        # commit for permanent storage in database
        cnt.commit()
        # display success message
        print(cursor.rowcount, "Record inserted.")
        # cursor.close()
        # cnt.close()


##update category#####
def update_category(self):
    # read values to be updated
    # self.id = input("Enter storekeeper ID:")
    if (selectCategoryById(self) == -1):
        return
    else:
        self.name = input("Enter new name:")
            # create update query
        cursor.execute("UPDATE categories SET name='" + self.name + "' WHERE id='" + self.id + "'")
            # commit Changes to DB
        cnt.commit()
        # #display success message
        print(cursor.rowcount, "Record updated.")
        print('\n')


def delete_category(self):
    # read the customer ID for which record to be deleted
    self.id = input("Enter category ID:")
    cursor.execute("SELECT * FROM categories WHERE id='" + self.id + "'")
    # Fetch all records from table
    res = cursor.fetchall()
    if res == []:
        print("\n")
        print("category not exists!")
        print("\n")

    else:
    # Create Delete Query
        sql = "DELETE FROM categories where id = '" + self.id + "'"
    # execute delete query
        cursor.execute(sql)
    # commit changes to DB
        cnt.commit()
    # display success message
    print(cursor.rowcount, "Category deleted.")
    print("\n")


def main():
    # open cursor
    ch = 0
    # display menu until user presses 5
    while (ch <= 6):
        # menu options
        print("1. Display Specific Category")
        print("2. Display All Categories")
        print("3. Add New Category")
        print("4. Update Category By Id")
        print("5. Delete Category")
        print("6. Exit")
        # ask user to enter what he wants to do
        ch = int(input("Enter Your Choice:"))
        # call relevant fucntions defined above
        if (ch == 1):
            selectCategoryById(self)
        if (ch == 2):
            selectAllCategory()
        if (ch == 3):
            insert_category(self)
        if (ch == 4):
            update_category(self)
        if (ch == 5):
            delete_category(self)



# call main
main()
