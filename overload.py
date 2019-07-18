class Student:
    def __init__(self, last_name, first_name, student_id, gpa):
        self.last_name = last_name
        self.first_name = first_name
        self.student_id = student_id
        self.gpa = gpa

    def __lt__(self, other):
        if self.gpa < other.gpa:
            return True
        return False

    def __gt__(self, other):
        if self.gpa > other.gpa:
            return True
        return False

    def __eq__(self, other):
        if self.last_name == other.last_name and self.first_name == other.first_name and self.student_id == other.student_id:
            return True
        return False

    def __str__(self):
        return('Student\'s name is: %s %s\nStudent\'s id is: %d \nStudent\'s gpa is: %2f' %(self.last_name, self.first_name, self.student_id, self.gpa))


s1 = Student(last_name='David', first_name='Yan', student_id=20001220, gpa=3.9)
s2 = Student(last_name='Leo', first_name='Liu', student_id=20000802, gpa=3.7)

if s1 > s2:
    print('David has a better gpa')
elif s1 < s2:
    print('Leo has a better gpa')
else:
    print('It is not clear whose gpa is better...')

print(s1)
print(s2)


