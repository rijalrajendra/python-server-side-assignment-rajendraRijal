class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def show(self):
        print("Name is:", self.name)
        print("Roll is:", self.roll)
        print("Marks are:", self.marks)

name=input("Enter name")
rollno=int(input("enter roll no="))
marks=float(input("enter marks="))
obj=Student(name, rollno, marks)
obj.show()