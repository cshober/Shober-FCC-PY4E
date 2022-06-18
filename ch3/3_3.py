# Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

def grader(grade):
    if grade >= 0 and grade <= 1:
        if grade >= .9:
            grade = 'A'
        elif grade >= .8 and grade < .9:
            grade = 'B'
        elif grade >= .7 and grade < .8:
            grade = 'C'
        elif grade >= .6 and grade < .7:
            grade = 'D'
        elif grade < .6:
            grade = 'F'
        else:
            grade = -1

        return grade
    else:
        return -2

while True:
    gradeInput = input('Enter score: ')

    try:
        gradeInput = float(gradeInput)
    except ValueError:
        print("Do not enter any words. Please enter your grade as a decimal between 0 and 1. Try again.")
        continue

    letterGrade = grader(gradeInput)

    if letterGrade == -1:
        print("Please enter your grade as a decimal between 0 and 1. Try again.")
        continue
    elif letterGrade == -2:
        print("Out of Range. Please enter your grade as a decimal between 0 and 1. Try again.")
        continue
    else:
        break

print(letterGrade)