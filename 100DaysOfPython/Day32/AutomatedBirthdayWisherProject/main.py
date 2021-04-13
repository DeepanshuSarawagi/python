import datetime
import smtplib
import random
import pandas

data = pandas.read_csv("birthdays.csv")
birthday_data = pandas.DataFrame(data)

birthday_person = birthday_data.to_dict(orient="records")

print(birthday_person)

month_now = datetime.datetime.now().month
day_now = datetime.datetime.now().day
letters = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
for person in birthday_person:
    if person["month"] == month_now and person["day"] == day_now:
        person_email = person["email"]
        person_name = person["name"]
        my_email = "blahbah@yahoo.com"
        password = "blahblahblah"
        random_letter = random.choice(letters)
        with open(random_letter, "r") as file:
            contents = file.readlines()
        with open(random_letter, "w") as file:
            contents[0] = "Dear " + person_name + ",\n"
            for content in contents:
                file.write(content)
        with open(random_letter, "r") as file:
            contents = file.read()

        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=person_email,
                                msg=f"Subject:Happy Birthday {person_name}\n\nThis is a test birthday message.\n{contents}")
