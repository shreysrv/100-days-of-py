height = float(input("Enter height in m : "))
weight = float(input("Enter weight in kg : "))

bmi = round(weight / height ** 2)
print(f"Your bmi is {bmi}")
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal Weight")
elif bmi < 30:
    print("Overweight")
elif bmi < 35:
    print("Obese")
else:
    print("Clinically Obese")
