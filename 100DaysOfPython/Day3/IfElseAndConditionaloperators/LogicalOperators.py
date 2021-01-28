name1 = input("Enter your name: ")
name1 = name1.lower()
name2 = input("Enter their name: ")
name2 = name2.lower()

final_name_string = name1 + " " + name2

no_of_t = 0
no_of_r = 0
no_of_u = 0
no_of_e = 0
no_of_l = 0
no_of_o = 0
no_of_v = 0

for i in range(0, len(final_name_string)):
    if final_name_string[i] == "t":
        no_of_t += 1
    if final_name_string[i] == "r":
        no_of_r += 1
    if final_name_string[i] == "u":
        no_of_u += 1
    if final_name_string[i] == "e":
        no_of_e += 1
    if final_name_string[i] == "l":
        no_of_l += 1
    if final_name_string[i] == "o":
        no_of_o += 1
    if final_name_string[i] == "v":
        no_of_v += 1

true_factor = no_of_t + no_of_r + no_of_u + no_of_e
love_factor = no_of_l + no_of_o + no_of_v + no_of_e

true_factor = str(true_factor)
love_factor = str(love_factor)

love_percentage = true_factor + love_factor

print("The True Love between you and your crush is {}%.".format(love_percentage))

love_percentage = int(love_percentage)

if love_percentage < 10 | love_percentage > 90:
    print("Your score is {}%, ypu go together like Coke and Mentos.".format(love_percentage))
elif 40 <= love_percentage <= 50:
    print("Your score is {}%, you are alright together.".format(love_percentage))
else:
    print("Your score is {}%.".format(love_percentage))
