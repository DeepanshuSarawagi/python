import smtplib

my_email = "sarawagideepanshu@gmail.com"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password="Yo!!ItIsHidden:P")
    connection.sendmail(from_addr=my_email, to_addrs="deepanshu.highplacesintl@yahoo.com",
                        msg="Subject:Hello\n\nHey There!! This is a test email using Python script")
