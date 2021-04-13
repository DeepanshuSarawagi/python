import smtplib

my_email = "sarawagideepanshu@gmail.com"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password="hidden:P")
connection.sendmail(from_addr=my_email, to_addrs="deepanshu.highplacesintl@yahoo.com",
                    msg="Hey There!! This is an email from a Python script")
connection.close()
