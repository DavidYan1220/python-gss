class Student:
    def __init__(self):
        self.name = ""
        self.gpa = 0
        self.student_id = 0


    def read_student(self):
        while True:
            try:
                self.name = input("Please enter student's name:")
                self.gpa = float(input("Please enter student's gpa:"))
                self.student_id = int(input("Please enter student's student id:"))
                return
            except:
                print('Enter the right info again.\n')


    def print_info(self):
        print("Student's name is", self.name)
        print("Student's gpa is", self.gpa)
        print("Student's id is", self.student_id)

def get_all_students_from_keyboard():
    student_list = []
    for i in range(5):
        s1 = Student()
        s1.read_student()
        student_list.append(s1)
    return student_list

l = get_all_students_from_keyboard()
for i in l:
    i.print_info()

