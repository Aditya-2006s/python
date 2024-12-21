marks = float(input("Enter the marks: "))

if marks >= 90 and marks <= 100:
    grade = 'A'
elif marks >= 80 and marks < 90:
    grade = 'B'
elif marks >= 70 and marks < 80:
    grade = 'C'
else:
    grade = 'Fail'
print(f"The grade is: {grade}")
