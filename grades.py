grade = float(input("enter grades"))
if grade != int(grade) or grade > 100:
    print("invalid")
elif grade >= 61 and grade <= 70 :
    print("D")
elif grade >= 71 and grade <= 80 :
    print("C")
elif grade >= 81 and grade <= 90 :
    print("B")
elif grade >= 91 and grade <= 100 :
    print("A")
elif grade <= 60 :
    print("F")

