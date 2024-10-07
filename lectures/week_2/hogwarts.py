# lists
# students = ["Hermione", "Harry", "Ron"]

# for student in students:
#     print(student)

# for i in range(len(students)):
#     print(students[i])

# for i in range(len(students)):
#     print(i + 1, students[i])

# Dictionaries
# students = {
#     "Hermione": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin"
#     }

# print(students["Hermione"])

# for student in students:
#     print(student, students[student], sep=": ")

students = [
    {"name": "Hermione", "House": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "House": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "House": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "House": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["House"], sep=", ")