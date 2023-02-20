student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if 90 < score <= 100:
        student_grades[student] = "Outstanding"
    elif 80 < score <= 90:
        student_grades[student] = "Exceeds Expectations"
    elif 70 < score <= 80:
        student_grades[student] = "Acceptable"
    elif score <= 70:
        student_grades[student] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)
