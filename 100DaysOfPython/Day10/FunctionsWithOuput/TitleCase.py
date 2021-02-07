# In this chapter we are going to learn how to change the string with Title Case


def format_name(f_name, l_name):
    f_name_titled = title_case(f_name)
    l_named_titled = title_case(l_name)
    return f_name_titled + " " + l_named_titled


def title_case(name):
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