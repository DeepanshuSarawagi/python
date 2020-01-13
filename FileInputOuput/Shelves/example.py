books = {"recipes": {"blt": ["bacon", "bread", "lettuce", "tomato"],
                     "beans_on_toast": ["beans", "bread"],
                     "pasta": ["pasta", "cheese"],
                     "soup": ["tin of soup"],
                     "scrambled eggs": ["eggs", "milk"]},
         "maintenance": {"stuck": ["oil"],
                         "loose": ["gaffer tape"]}
         }
print(books["recipes"]["pasta"])
print(books["maintenance"]["stuck"])

for keys in books.keys():
    print(keys)
    for key in books[keys]:
        print(f"{key} - {books[keys][key]}")
