students_height = input("Input a list of student heights ").split()
sum = 0
for height in students_height:
    sum += int(height)

print(round(sum / len(students_height)))
