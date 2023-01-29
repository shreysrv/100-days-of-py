import random

name_list = input("Enter names:").split(",")
random_person = random.randint(0, len(name_list) - 1)

print(f"{name_list[random_person]} pays the bill")
name_list.extend(["sagar", "yash"])
print(f"{random.choice(name_list)} pays the bill, next time")
