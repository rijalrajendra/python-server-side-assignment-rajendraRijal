student=[]
n = int(input("Enter number of students: "))

with open("students.txt", "w") as file:
    for i in range(n):
        name = input("Enter student name: ")
        file.write(name)

with open("students.txt", "r") as file:
    content=file.readlines()
    for line in content:
        print(line.strip())