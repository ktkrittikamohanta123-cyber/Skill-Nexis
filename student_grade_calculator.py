# Assignment 2: Student Grade Calculator
# Calculate the average marks and assign a grade.

name = input("Enter student name: ")

m1 = float(input("Enter marks in Subject 1: "))
m2 = float(input("Enter marks in Subject 2: "))
m3 = float(input("Enter marks in Subject 3: "))
m4 = float(input("Enter marks in Subject 4: "))
m5 = float(input("Enter marks in Subject 5: "))

total = m1 + m2 + m3 + m4 + m5
average = total / 5

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Average Marks:", average)

if average >= 90:
    print("Grade: A+")
elif average >= 80:
    print("Grade: A")
elif average >= 70:
    print("Grade: B")
elif average >= 60:
    print("Grade: C")
elif average >= 40:
    print("Grade: D")
else:
    print("Grade: F")
