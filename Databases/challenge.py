import sqlite3

db = sqlite3.connect("contacts.sqlite")

for row in db.execute("SELECT * FROM sqlite_master"):
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
