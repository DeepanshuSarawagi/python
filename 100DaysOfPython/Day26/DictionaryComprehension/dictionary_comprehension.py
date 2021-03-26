"""In this lesson we are going to learn about dictionary comprehension
Syntax for dictionary comprehension is new_dict = {new_key:new_value for item in list}

we can also create new dictionary from an existing dictionary using list comprehension

new_dict = {new_key:new_value for (key, value) in dict.items()}

syntax for conditional dictionary comprehension
new_dict = {new_key:new_value for (key, value) in dict.items() if test} where test is the test condition

"""
import random

names = ["Deepanshu", "Divya", "Rajat", "Vandana", "Pooja", "Krishna", "Shubham", "Lakita"]

student_scores = {student: random.randint(1, 100) for student in names}
print(student_scores)

passed_students = {student: score for student, score in student_scores.items() if score > 60}
print(passed_students)
