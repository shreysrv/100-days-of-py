print("Welcome to Pizza order calculator")
size = input("What Size of pizza do you want? (S/M/L):")
pepperoni = input("Do you want extra Pepperoni? (Y/N)")
cheese = input("Do you want extra cheese? (Y/N)")

bill = 0;
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

if pepperoni == "Y":
    if size == "S":
        bill += 2
    elif size == "M" or size == "L":
        bill += 3

if cheese == "Y":
    bill += 1

print(f"You have ordered {size} pizza with {pepperoni} extra pepperoni and {cheese} extra cheese")
print(f"Total bill:${bill}")
