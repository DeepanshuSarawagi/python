# Writing something to a file.
cities = ["Chennai", "Bengaluru", "Delhi", "Mumbai", "Pune", "Jaipur"]
with open("cities.txt", 'w') as city_file:
    for city in cities:
        print(city, file=city_file, end='\n')

# Since we are using the with statement, we need not explicity close the file.