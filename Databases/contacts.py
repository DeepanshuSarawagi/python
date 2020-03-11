import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts (name, phone, email) VALUES('Deepanshu', 654789, 'deepanshu@email.com')")
db.execute("INSERT INTO contacts VALUES('Rajat', 987654, 'rajat@wmail.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")
for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print("*" * 40)

cursor.close()
db.close()
