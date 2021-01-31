# In this lesson we are going to learn about range function in Python

sum_of_numbers = 0
for i in range(1, 101):
    sum_of_numbers += i
print(sum_of_numbers)

# Day 5 - Exercise 3

sum_of_even = 0
for i in range(0, 101, 2):  # Here we are using the step as 2 to loop through every second item in the range
    sum_of_even += i
print(sum_of_even)
