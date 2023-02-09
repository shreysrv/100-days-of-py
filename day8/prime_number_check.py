def prime_number_checker(number):
    for i in (2, number - 1):
        if number % i == 0:
            return False
    return True


num = int(input("Enter a number"))
if prime_number_checker(number=num):
    print("Prime number")
else:
    print("Not a Prime number")
