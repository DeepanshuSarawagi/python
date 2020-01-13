import shelve
with shelve.open("fruit") as fruit_shelve:
    fruit_shelve["apple"] = "Great for making ciders"
    fruit_shelve["orange"] = "A sweet, orange, citrus fruit"
    fruit_shelve["lemon"] = "A sour, yellow, citrus fruit"
    fruit_shelve["lime"] = "A sour/sweet, green, citrus fruit"
    fruit_shelve["banana"] = "A yellow fruit good for breakfast"

    print(fruit_shelve["banana"])
    print(fruit_shelve["lime"])

    fruit_shelve["lime"] = "Great with Tequila"

    for snack in fruit_shelve:
        print(snack + " - " + fruit_shelve[snack])  # When you run this code, you can see that value of lime is changed
    while True:
        shelf_key = input("Please enter a fruit name: ")
        if shelf_key == "quit":
            break
        else:
            description = fruit_shelve.get(shelf_key)
            print(description)

"""Notice the indentation level after the with statement. If we remove the indents, Python will throw an error which
will say "Cannot access the object key on closed shelve."""
"""To overcome this problem please refer to the below code. We need to manually open and close the shelve since "with"
 statement automatically takes care of it."""

fruit2 = shelve.open("fruit2")
fruit2["apple"] = "Great for making ciders"
fruit2["orange"] = "A sweet, orange, citrus fruit"
fruit2["lemon"] = "A sour, yellow, citrus fruit"
fruit2["lime"] = "A sour/sweet, green, citrus fruit"
fruit2["banana"] = "A yellow fruit good for breakfast"

print(fruit2["banana"])
print(fruit2["lime"])

fruit2["lime"] = "Great with tequila"
for snack in sorted(fruit2.keys()):
    print(snack + " - " + fruit2[snack])

print("=" * 50)

while True:
    fruit2_key = input("Please enter a fruit name: ")
    if fruit2_key == "quit":
        break
    else:
        description_of_fruit2 = fruit2.get(fruit2_key)
        print(description_of_fruit2)

fruit2.close()

print(fruit_shelve)
