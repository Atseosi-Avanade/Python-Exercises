"""
Grade reporting simulation
"""
import sys
inputted_grade = None
looping = True
gradeDict = {90: "A*", 80: "A", 70: "B", 60: "C", 50: "D", 40: "E"}

while looping:
    inputted_grade = int(input("Input a numeric grade: "))
    if inputted_grade > 100 or inputted_grade < 0:
        print("This is invalid. Try again")
        continue
    for grade in gradeDict:
        if inputted_grade < 40:
            print("F!!!!!!!!!!!!!")
            break
        if inputted_grade >= grade:
            print(f"Your grade is {gradeDict[grade]}")
            break
    cont = input("Do you want to continue checking grades? Y/N: ")
    if cont == "Y" or cont == "y":
        continue
    else:
        print("Done")
        sys.exit(0)

print("Done")

