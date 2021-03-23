import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrel = squirrel_data[squirrel_data['Primary Fur Color'] == "Gray"]
no_of_gray_squirrel = gray_squirrel["Primary Fur Color"].count()

cinnamon_squirrel = squirrel_data[squirrel_data['Primary Fur Color'] == "Cinnamon"]
no_of_cinnamon_squirrel = cinnamon_squirrel["Primary Fur Color"].count()

black_squirrel = squirrel_data[squirrel_data['Primary Fur Color'] == "Black"]
no_of_black_squirrel = black_squirrel["Primary Fur Color"].count()

squirrel_dict = {
                "Fur Color": ["red", "gray", "white"],
                "Count": [no_of_cinnamon_squirrel, no_of_gray_squirrel, no_of_black_squirrel]
}

squirrel_df = pandas.DataFrame(squirrel_dict)
print(squirrel_df)

squirrel_df.to_csv("squirrel_count.csv")
