for i in range(1,13):
    print("No. {:2} squared is {:3} and cubed is {:4}".format(i,i**2,i**3)) #Field replacement width
print()
for i in range(1,13):
    print("No. {:<2} squared is {:<3} and cubed is {:<4}".format(i,i**2,i**3)) # Field replacement left alignment

print()
print("Pi is approximately {0:12}".format(22 / 7))  # Default with 15 precision points of 15 digits float number post decimal
print("Pi is approximately {0:.2f}".format(22 / 7)) # Exactly two precision points of 2 digits float number post decimal
print("Pi is approximately {0:12.12f}".format(22 / 7)) # Exactly two precision points of 12 digits float number post decimal
print("Pi is approximately {0:12.50f}".format(22 / 7)) # Exactly two precision points of 50 digits float number post decimal
print("Pi is approximately {0:52.50f}".format(22 / 7)) # The 12, 52, 62, 72 are field width
print("Pi is approximately {0:62.50f}".format(22 / 7))
print("Pi is approximately {0:72.50f}".format(22 / 7))