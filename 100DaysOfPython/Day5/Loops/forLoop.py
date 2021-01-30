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

# Day 5 - Exercise 2 - Print the highest score from the list

high_scores = input("Enter the high scores of the students separated by commas and space: ")
high_scores = high_scores.split(", ")

highest_score = 0

for high_score in high_scores:
    if int(high_score) > highest_score:
        highest_score = int(high_score)

print(highest_score)
lowest = 100
for i in range(0, (len(high_scores) - 1)):
    if int(high_scores[i]) < lowest:
        lowest = int(high_scores[i])
print(lowest)
