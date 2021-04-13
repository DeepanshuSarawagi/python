import datetime
import random
import smtplib

with open("quotes.txt", "r") as file:
    motivation_quotes = file.readlines()

random_quote = random.choice(motivation_quotes)
quote = random_quote.split(" - ")[0]
author = random_quote.split(" - ")[1].strip("\n")

day_now = datetime.datetime.now().weekday()

email = "gibberish"
password = "gibberish"
to_list = ["gibberishuser1", "gibberishuser2"]
if day_now == 1:
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs=to_list,
                            msg=f"Subject:Monday Motivation\n\nThis is a project created by Deepanshu Sarawagi."
                               " This automated monday motivation email project is created using Python."
                               " You will receive Motivational quotes every Monday."
                               " Time for some motivation now."
                               f"\n\n{quote} - {author}")
