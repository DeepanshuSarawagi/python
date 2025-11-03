age = 24
print("My age is " + str(age) + " years.")
# replacement fields in strings
print("My age is {} years.".format(age))

# Can also be used with string literals
print("""
Jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
Jun: {1}
Jul: {2}
Aug: {2}
Sep: {1}
Oct: {2}
Nov: {1}
Dec: {2}"""
      .format(28, 30, 31,))
