import smtplib

my_email = "deepanshu.highplacesintl@yahoo.com"
password = "gibberishpassword:P"

with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="sarawagideepanshu@gmail.com",
                        msg="Subject:Hello\n\nHey There!! This is a test email using Python script")
