# This is a US Floor app exercise on freeCodeCamp


EUFloor = int(input("Enter on which floor you are? "))
print("The European floor is {0}".format(EUFloor))
USFloor = EUFloor + 1
print("You are on US floor: {0}".format(USFloor))


Hours = int(input("Enter the no. of hours you have worked: "))
Pay = 9.56
print("Your pay is {0:9.2f}".format(Hours*Pay))
