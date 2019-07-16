class Student:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.list_of_grades = []
        self.gpa = 0
        self.graduation_day = ""
        self.graduation_month = ""
        self.graduation_year = ""

    def read_student(self):
        self.name = input("Please enter student's name:")
        self.age = int(input("Please enter student's age:"))
        for i in range(0, 5):
            self.list_of_grades.append(int(input("Please enter student's grades:")))
        self.graduation_day = input("Please enter student's graduation day:")
        self.graduation_month = input("Please enter student's graduation month:")
        self.graduation_year = input("Please enter student's graduation year:")

    def find_gpa(self):
        self.gpa = sum(self.list_of_grades)/len(self.list_of_grades)


    def print_info(self):
        print("Student's name is", self.name)
        print("Student's age is", self.age)
        print("Student's gpa is", self.gpa)
        print("Student's graduation day is", self.graduation_day)
        print("Student's graduation month is", self.graduation_month)
        print("Student's graduation year is", self.graduation_year)


t = Student()
t.read_student()
t.find_gpa()
t.print_info()
