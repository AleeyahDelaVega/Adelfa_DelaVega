#------------------------------
# Name: Aleeyah P. Dela Vega
# Section: 8-Adelfa
# Title: Hands-on Activity 3 - Payment Method Checker
# Date: 09/17/26
#------------------------------

#--Import regular expressions for the re.fullmatch() function--
import re

#--Ask the user for their student ID number--
student_id = input("Enter Student ID: ")

#--Assign the required pattern
pattern = r'\d{4}-\d{4}'

#--Output each result based on their student ID, if it's valid or invalid--
if re.fullmatch(pattern, student_id):
    print("Valid Student ID.")
else:
    print("Invalid Student ID.")