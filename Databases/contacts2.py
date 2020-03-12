import sqlite3

db = sqlite3.connect("contacts.sqlite")
update_sql = "UPDATE contacts set email = 'update@update.com' WHERE contacts.phone = 654789"
update_cursor = db.cursor()
update_cursor.execute(update_sql)
print(f"{update_cursor.rowcount} rows updated")
update_cursor.close()

for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print("*" * 40)

db.close()
