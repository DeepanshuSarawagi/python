bill_amount = float(input("What was the total bill?\n"))
tip = int(input("What is the percentage of tip you would like to give? 12, 14 or 15?\n"))
tip_on_bill = float((bill_amount * tip) / 100)
total_bill = float(bill_amount + tip_on_bill)
no_of_persons = int(input("How many people to split the bill?\n"))
print("Each person should pay {:.2f}".format(round(total_bill / no_of_persons, 2)))
