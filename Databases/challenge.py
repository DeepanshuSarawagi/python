import sqlite3

db = sqlite3.connect("contacts.sqlite")
name_input = input("Please enter the name to retrieve the data: ")

for row in db.execute("SELECT * FROM contacts where name = ?", (name_input,)):
    print(row)

# cursor = db.cursor()
#
# cursor.execute("SELECT * FROM sqlite_master")
#
# for name, phone, email in cursor:
#     print(name)
#     print(phone)
#     print(email)
#     print("*" * 40)
#
# cursor.close()

db.close()
