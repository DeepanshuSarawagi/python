age = int(input("Enter your age: "))
print("You have {} days or {} weeks or {} months left to live.".
      format((90 - age) * 365, (90 - age) * 52, (90 - age) * 12))
