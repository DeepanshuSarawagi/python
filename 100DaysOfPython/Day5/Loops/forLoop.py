# In this lesson we are going to learn about For loop

fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)

student_heights = input("Please enter the student heights separated by comma and space: ")
student_heights = student_heights.split(", ")

count = 0
sum_of_height = 0
for student in student_heights:
    count += 1
    sum_of_height += int(student)

print("Average students height = {}".format(round(sum_of_height / count)))
