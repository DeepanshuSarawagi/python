import sqlite3

db = sqlite3.connect("accounts.sqlite")

for row in db.execute("SELECT * FROM history"):
    print(row)

db.close()