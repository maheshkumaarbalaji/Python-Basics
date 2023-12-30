student = {
    'name': 'Mahesh',
    'age': 26,
    'ethnicity': 'asian',
    'IsVeteran': False
}

student_keys = student.keys()
student_values = student.values()

if "name" in student_keys:
    print("Name is present in the dictionary.")
else:
    print("Name is not present in the dictionary.")

print(student.get("name"))
print(student.pop("name"))
print(student)

for key in student_keys:
    print(key)