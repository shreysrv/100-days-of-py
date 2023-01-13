first_name = input("Enter name of first person: ")
second_name = input("Enter name of Second person: ")

first_name_lower = first_name.lower()
second_name_lower = second_name.lower()

count_true = 0

count_true += first_name_lower.count("t")
count_true += first_name_lower.count("r")
count_true += first_name_lower.count("u")
count_true += first_name_lower.count("e")

count_true += second_name_lower.count("t")
count_true += second_name_lower.count("r")
count_true += second_name_lower.count("u")
count_true += second_name_lower.count("e")

count_love = 0
count_love += first_name_lower.count("l")
count_love += first_name_lower.count("o")
count_love += first_name_lower.count("v")
count_love += first_name_lower.count("e")

count_love += second_name_lower.count("l")
count_love += second_name_lower.count("o")
count_love += second_name_lower.count("v")
count_love += second_name_lower.count("e")

result_string = str(count_true) + str(count_love)
result = int(result_string)

if result < 10 or result > 90:
    print(f"your score is {result}, you go together like coke and mentos")
elif 40 < result < 50:
    print(f"your score is {result}, you are alright together")
else:
    print(f"your score is {result}")
