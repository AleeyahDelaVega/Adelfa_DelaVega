#------------------------------
# Name: Aleeyah P. Dela Vega
# Section: 8-Adelfa
# Title: Hands-on Activity 2 - Grade Checker
# Date: 09/17/26
#------------------------------

#--Ask user for their grade--
grade = int(input("Enter your grade: "))

#--Check if their grade is valid or not--
if 0 <= grade <= 100:
    #--Display this result if their grade is valid--
    print("Valid grade")
else:
    #--Display this if their grade is invalid--
    print("Invalid grade. Grade must be between 0 and 100.")