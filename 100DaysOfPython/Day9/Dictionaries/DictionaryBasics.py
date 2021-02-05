# In this lesson we are going to learn about the dictionaries in Python

programming_dictionary = {
                        "bug": "A piece of code which prevents the program from running as expected",
                        "function": "A program which can be called again and again"
                        }

# Adding new items to the dictionary

programming_dictionary["Loop"] = "The action of doing something again and again."

for keys in programming_dictionary.keys():
    print("{}: {}".format(keys, programming_dictionary[keys]))

list_of_even = {}

for i in range(101):
    list_of_even[i] = i * 2

print(list_of_even)

print()

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for key in student_scores:
    if 91 <= student_scores[key] <= 100:
        student_grades[key] = "Outstanding"
    elif 81 <= student_scores[key] <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif 71 <= student_scores[key] <= 80:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

print(student_grades)
