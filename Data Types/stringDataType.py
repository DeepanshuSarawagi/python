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

# Negative indexing to slice a string

print(parrot[-4:-2])

# Or you can the get the same output using the below code.

print(parrot[-4:12])

# since the positive index value of l is same as negative index value when calculated.
# One important thing to note is that we cannot slice a string backwards

# Using a step in a slice. We can use the step in slicing. Let`s see an example to understand how step is used in
# slicing.

print(parrot[0:6:2])  # Here, slice starts from index 0 and extends upto index value 6 (not including 6 and every 2nd
                      # index value is omitted.
# Norwegian Blue
# 01234567890123
# hence output of print(parrot[0:6:2]) is Nre
print(parrot[0:14:3])

# Negative step in slicing

letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[25:0:-1]

# when we print backwards, it will print the letters in backwards excluding a because index stop value is till index 0
# and not including that

print(backwards)

Backwards = letters[25::-1]
print(Backwards)

# Challenge1
print(letters[16:13:-1])

# Challenge2
print(letters[4::-1])

# Challenge3

print(letters[25:17:-1])
