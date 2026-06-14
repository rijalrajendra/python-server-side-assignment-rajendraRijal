student={}
print("Choose your option")
print("1. Add Student")
print("2. Search Student")
print("3. Display all student")
choice= input("enter your choice")
if choice=="1":
    name=input("Enter Student Name=")
    rollno=int(input("Enter roll number="))
    marks=float(input("Enter marks="))
    contact=input("Enter Contact number=")
    student = {
        "name": name,
        "roll": rollno,
        "marks": marks,
        "contact": contact
    }
elif choice=="2":
    rollno =input("enter roll number to search student")
    if rollno in student:
        print(student[rollno])
    else:
        print("Not Found!")
elif choice=="3":
    print(student)
else:
    print("invalid!")