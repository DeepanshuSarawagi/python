# In this lesson we are going to learn more about the string data type.

parrot = "Norwegian Blue"
print(parrot)
print(parrot[3])

# In the above example, the number in square paranthesis is call index number.

# Below is an example of negative index of a string

print(parrot[-4])
print(parrot[-5])
print(parrot[-6])

print(50 * "=")
# Slicing the string

print(parrot[0:6])

# In this example we have asked python to slice the string from index 0 upto and not including index 6.
# It is not necessary to provide the start index value if you want to slice a string from the beginning.
# Below example will print the Sliced string from index 0 to index 8
print(parrot[:9])

print(50 * "=")

print(parrot[10:14])
# if you want to print the sequence by slicing at any start value till the end, we need not specify the end index value.

print(parrot[10:])

# Below example will slice the entire string because we have not provided the start and end value.

print(parrot[:])
