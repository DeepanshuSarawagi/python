import sqlite3

db = sqlite3.connect("contacts.sqlite")
email = "anotherupdate@update.com"
phone = input("Please provide the email to update the email: ")

update_sql = f"UPDATE contacts SET email = '{email}' WHERE phone = {phone}"
update_cursor = db.cursor()
update_cursor.execute(update_sql)
print(f"{update_cursor.rowcount} rows updated")
update_cursor.close()

update_cursor.connection.commit()  # Use cursor to commit any changes to DB

for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print("*" * 40)

db.close()
