# In this lesson we are going to learn about Nesting in lists and dictionaries

# Here we are going to create a dictionary by nesting a list as value of key

travel_log = {
    "Tamil Nadu": ["Chennai", "Coimbatore", "Rameshwaram", "Dindigul", "Salem"],
    "Kerala": ["Cochin", "Munnar", "Ernakulam"],
    "Maharashtra": ["Mumbai", "Nagpur", "Pune"],
    "Uttar Pradesh": ["Lucknow", "Saharanpur", "Mathura", "Vrindavan", "Naimisharanye"],
    "Rajasthan": ["Jaipur", "Mehandipur Balaji", "Pushkar", "Salasar", "Jhunjhunu"]
}

for key in travel_log:
    for value in travel_log[key]:
        print("{}: {}".format(key, value))

# Nesting a dictionary within a dictionary

travel_log_dict = {
    "Tamil Nadu": {"cities_visited": ["Chennai", "Coimbatore", "Rameshwaram", "Dindigul", "Salem"]},
    "Kerala": {"cities_visited": ["Cochin", "Munnar", "Ernakulam"]},
    "Maharashtra": {"cities_visited": ["Mumbai", "Nagpur", "Pune"]},
    "Uttar Pradesh": {"cities_visited": ["Lucknow", "Saharanpur", "Mathura", "Vrindavan", "Naimisharanye"]},
    "Rajasthan": {"cities_visited": ["Jaipur", "Mehandipur Balaji", "Pushkar", "Salasar", "Jhunjhunu"]}
}

for states in travel_log_dict:
    print(states, travel_log_dict[states])
    for key in travel_log_dict[states]:
        print("{}: {}".format(key, travel_log_dict[states][key]))
