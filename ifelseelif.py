students = ["Mohmmad", "abrahim", "john", "Aaqid"]


allowed_students = []

# for student in students:
#     if student == "john":
#         continue
#     allowed_students.append(student)


for student in students:
    if student != "john":
        allowed_students.append(student)

print(allowed_students)