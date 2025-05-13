data = [(1, 90), (2, 50), (1, 60), (2, 66), (3, 87)]
students = {}

for rollno, marks in data:
    total = students.get(rollno, 0)
    students[rollno] = total + marks

print(students)
