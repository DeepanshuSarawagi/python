# In this lesson we are going to learn about string replacement fields.
# It is possible to concatenate a number with string by converting the int data type to string using str function.

name =  "Deepanshu"
age = 27
print("My age is " + str(age) + " years.")
print(name + " is " + str(age) + " years old.")

# Hence str() function, we can coerce an integer to a string.
# However, coercing every integer to a string could become tedious. Hence, Python 3 provides a better way of formatting
# string using the .format() method. We can achieve the same output of code in line 5 by replacing the string coercion
# with string formatting. Refer to code in line 11.
print("My age is {0} years.".format(age))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, {7}.".
      format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))

print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1}, Jul: {2}, Aug: {2}, Sep: {1}, Oct: {2}, Nov: {1}, "
      "Dec: {2} "
      .format(28, 30, 31))


# Let's learn about f-strings
# code on line 6 can also be written like this.

print(name + f" is {age} years old. ")
# code on line 26 is example of f-strings in python which is used in version 3.6 and above.
