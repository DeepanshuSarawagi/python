height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
print("Your BMI is {}".format(round(weight / (height * height), 2)))
