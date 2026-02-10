m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))

avg = (m1 + m2 + m3) / 3
print("\nAverage Marks Scored=", avg)

if avg >= 90 and avg <= 100:
    grade = "A"
elif avg >= 80:
    grade = "B"
elif avg >= 70:
    grade = "C"
elif avg >= 60:
    grade = "D"
else:
    grade = "F"

print("Grade Obtained=", grade)