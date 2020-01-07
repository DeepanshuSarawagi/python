fruits = {"Orange": "A sweet orange citrus fruit, usually good for skin",
          "Apple": "Good for health if eaten once a day",
          "Lime": "A green sour/sweet citrus fruit",
          "Lemon": "A yellow sour citrus fruit, usually good with Vodka"}

print(fruits)
print(fruits.keys())
print(fruits["Lemon"])

vegetables = {"cabbage": {1: "Good for health"},
              "carrot": {2: "Good for eye"}}
print(vegetables["carrot"][2])  # Extracting the value from dictionary within dictionary


veg = {"Cabbage": "Good for health. Mostly preferred in salads",
       "Carrot": "Very good for eyes. Rich in Vitamin A",
       "Spinach": "High proteins. Good for hair and eyes",
       "Broccoli": "Very high proteins."}

print(veg)
print()
veg.update(fruits)  # We have updated the dictionary veg by adding fruits dictionary in it.
print()
print(veg)

print(fruits["Orange"].split())
print()

nice_veg = fruits.copy()  # Creating a new dictionary by copying fruits dictionary in it
nice_veg.update(veg)      # Updating the newly created dictionary by adding another dictionary "veg" in it
print(nice_veg)
print()

for f in sorted(nice_veg.keys()):
    print(f + " - " + nice_veg[f])
