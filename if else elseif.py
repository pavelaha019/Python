mark = float(input("Enter the CGPA : "))

if 0 <= mark <= 32:
    print("F")
elif 33 <= mark <= 39:
    print("D")
elif 40 <= mark <= 49:
    print("C")
elif 50 <= mark <= 59:
    print("B")
elif 60 <= mark <= 69:
    print("A-")
elif 70 <= mark <= 79:
    print("A")
elif 80 <= mark <= 100:
    print("A+")
else :
    print("Unvalid Mark")
    