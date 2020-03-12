import sqlite3

db = sqlite3.connect("contacts.sqlite")

cursor = db.cursor()

cursor.execute("SELECT * FROM contacts")

for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print("*" * 40)

cursor.close()

db.close()
