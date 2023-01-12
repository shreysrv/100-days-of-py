print("Welcome to that tip calculator")
bill = float(input("what is the bill amount?"))
tip_percentage = int(input("What the percentage tip? - 10, 12 or 15?"))
people = int(input("How many people to split the bill?"))
# calculations
tip_actual = round(bill * tip_percentage / 100, 2)
total_bill = bill + tip_actual
people_share = round(total_bill / people, 2)
print(f"Each person should pay : {people_share}")
people_share_formatted = "{:.2f}".format(people_share)
print(f"Each person should pay : {people_share_formatted}")
