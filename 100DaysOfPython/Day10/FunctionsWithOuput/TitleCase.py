# In this chapter we are going to learn how to change the string with Title Case
# Always remember that return keyword is always the end of the function

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return  # This is going to end the function since we are asking the function to quit
    f_name_titled = title_case(f_name)
    l_named_titled = title_case(l_name)
    return f_name_titled + " " + l_named_titled


def title_case(name):
    """
    :param name: This will accept one parameter name
    :return: The parameter name will be formatted to the title case and returned to the user
    """
    titled_case = ""
    for i in range(len(name)):
        if i == 0:
            titled_case += name[0]
            titled_case = titled_case.upper()
        else:
            next_char = name[i]
            next_char = next_char.lower()
            titled_case += next_char
    return titled_case


final_name = format_name(f_name="deEPanShU", l_name="sARaWaGI")
print(final_name)


# Day 10 Exercise 1

def is_leap_year(year):
    if year % 4 == 0 or year % 400 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year) and month == 2:
        return month_days[1] + 1
    else:
        return month_days[month - 1]


year = int(input("Enter a year: "))
month = int(input("Enter a month between 1 and 12: "))
days = days_in_month(year=year, month=month)
print(days)
