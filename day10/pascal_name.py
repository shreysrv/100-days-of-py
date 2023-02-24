def format_name(f_name, l_name):
    formatted_f_name = str(f_name).title()
    formatted_l_name = str(l_name).title()
    return f_name + " " + l_name


f_name = input("Enter first name: ")
l_name = input("Enter last name: ")
formatted_name = format_name(f_name, l_name)
print(formatted_name)
