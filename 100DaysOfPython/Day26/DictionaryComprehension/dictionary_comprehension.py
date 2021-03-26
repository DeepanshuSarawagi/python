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

# Day - 26 - Challenge 4

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
list_of_words = sentence.split(" ")

new_dict = {word: len(word) for word in list_of_words}
print(new_dict)

# Day 26 - Challenge 5

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: "{:.1f}".format(temp * 1.8 + 32) for day, temp in weather_c.items()}
print(weather_f)
