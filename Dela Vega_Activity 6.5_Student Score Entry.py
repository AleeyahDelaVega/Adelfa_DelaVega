#------------------------------
# Name: Aleeyah P. Dela Vega
# Section: 8-Adelfa
# Title: Hands-on Activity 5 - Student Score Entry
# Date: 09/19/26
#------------------------------

try:
    #--Ask the student for their score--
    student_score = int(input("Enter examination score: "))
    #--Display each result based according to their score, if it's within the range (valid) or beyond the range
    if 0 <= student_score <= 100:
        print("Valid score.")
    else:
        print("Invalid score. Grade must be between 0 and 100.")
except ValueError:
    #--Display this if the user inputted something else instead of a number--
    print("Invalid input. Please enter a number.")