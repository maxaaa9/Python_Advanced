student_dict = {}
for students in range(int(input())):
    student, grade = input().split()
    if student not in student_dict:
        student_dict[student] = []
    student_dict[student].append(float(grade))

for name, grades in student_dict.items():
    average_grade = sum(grades) / len(grades)
    formatted_grades = [f"{x:.2f}" for x in grades]
    print(f"{name} -> {' '.join(formatted_grades)} (avg: {average_grade:.2f})")

