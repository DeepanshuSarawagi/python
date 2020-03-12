import sqlite3

db = sqlite3.connect("contacts.sqlite")
email = "newupdate@update.com"
phone = input("Please provide the email to update the email: ")

# update_sql = f"UPDATE contacts SET email = '{email}' WHERE phone = {phone}"
update_sql = "UPDATE contacts SET email = ? WHERE phone = ?"  # Make changes to avoid SQL Injection attacks
print(update_sql)

update_cursor = db.cursor()
update_cursor.execute(update_sql, (email, phone))  # Add the tuple to avoid SQL Injection attacks
print(f"{update_cursor.rowcount} rows updated")
update_cursor.close()

update_cursor.connection.commit()  # Use cursor to commit any changes to DB

for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print("*" * 40)

db.close()
