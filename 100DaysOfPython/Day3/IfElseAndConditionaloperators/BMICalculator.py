# BMI calculator 2.0
height = float(input("Please enter your height in meters: "))
weight = float(input("Please enter your weight in kgs: "))

bmi = float(round(weight / (height ** 2), 2))
if bmi < 18.5:
    print("BMI = {:.2f}. You are underweight".format(bmi))
elif 18.5 <= bmi <= 25:
    print("BMI = {:.2f}. You are normal weight.".format(bmi))
elif 25 < bmi <= 30:
    print("BMI = {:.2f}. You are overweight.".format(bmi))
elif 30 < bmi <= 35:
    print("BMI = {:.2f}. You are obese.".format(bmi))
else:
    print("BMI = {:.2f}. You are clinically obese.".format(bmi))
