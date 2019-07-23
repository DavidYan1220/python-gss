class Employee:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.eID = 0
        self.e_duration = 0
        self.salary_per_day = 0

    def print(self):
        print("First name:", self.first_name)
        print("Last name:", self.last_name)
        print("eID:", self.eID)
        print("eDuration:", self.e_duration)
        print("Salary per day:", self.salary_per_day)


my_file = open("input.txt")
my_output_file = open("output.txt", "w")
employee_list = []
for l in my_file:
    l2 = l.split(",")
    print(l2)
    e1 = Employee()
    e1.first_name = l2[0]
    e1.last_name = l2[1]
    e1.eID = int(l2[2])
    e1.e_duration = int(l2[3])
    e1.salary_per_day = int(l2[4])
    e1.salary = e1.salary_per_day * e1.e_duration
    employee_list.append(e1)
    my_output_file.write(str(e1.first_name) + " " + str(e1.last_name) + " " + str(e1.eID) + " " + str(e1.e_duration) + " " + str(e1.salary_per_day) + "\n")
    my_output_file.write("The total amount of money that the company paid for " + e1.first_name + " is " + "$" + str(e1.salary) + "\n")
my_file.close()

for i in employee_list:
    i.print()


