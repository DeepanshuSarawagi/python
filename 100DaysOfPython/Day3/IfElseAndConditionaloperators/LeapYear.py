year = int(input("Please enter the year of your choice: "))

if (year % 4 == 0) or (year % 400 == 0) or (year % 100 == 0):
    if year % 100 == 0 and year % 400 != 0:
        print("{} is not a leap year".format(year))
    else:
        print("{} is a leap year".format(year))
else:
    print("{} is not a leap year".format(year))
