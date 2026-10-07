import csv
import json

students = [
    [1, "Kartik", "CSE", 89, 88, 98],
    [2, "Guilliman", "CSE", 99, 100, 99],
    [3, "Jonson", "CSE", 60, 79, 75]
]

with open("student.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Roll No.", "Name", "Branch",
        "math marks", "science marks", "python marks"
    ])
    writer.writerows(students)

Result = []

with open("student.csv", "r") as file:
    data = csv.DictReader(file)

    for row in data:
        m1 = int(row["math marks"])
        m2 = int(row["science marks"])
        m3 = int(row["python marks"])

        total = m1 + m2 + m3
        percentage = (total / 300) * 100

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 75:
            grade = "B+"
        elif percentage >= 65:
            grade = "B"
        elif percentage >= 55:
            grade = "C+"
        elif percentage >= 45:
            grade = "D"
        else:
            grade = "Fail"

        student = {
            "Roll No": row["Roll No."],
            "Name": row["Name"],
            "Total Marks": total,
            "Percentage": percentage,
            "Grade": grade
        }

        Result.append(student)

print(Result)

with open("students.json", "w") as file:
    json.dump(Result,file,indent = 4)