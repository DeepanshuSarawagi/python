# In this lesson we are going to learn about string replacement fields.
# It is possible to concatinate a number with string by converting the int data type to string using str function.

age = 27
print("My age is " + str(age) + " years.")

# Hence str() function, we can coerce an integer to a string.
# However, coercing every integer to a string could become tedious. Hence, Python 3 provides a better way of formatting
# string using the .format() method. We can achieve the same output of code in line 5 by replacing the string coercion
# with string formatting. Refer to code in line 11.
print("My age is {0} years.".format(age))

