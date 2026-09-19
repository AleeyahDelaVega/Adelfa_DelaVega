#------------------------------
# Name: Aleeyah P. Dela Vega
# Section: 8-Adelfa
# Title: Hands-on Activity 4 - PIN Validator
# Date: 09/19/26
#------------------------------

#--Get 6-digit pin from user--
pin = input("Create your 6-digit pin: ")

#--Determine if the inputted pin has 6 digits and are all digits--
if len(pin) == 6 and pin.isdigit():
    #--Display this if the pin met all the requirements--
    print("Valid PIN.")
else:
    #--Display this if the pin did not meet the requirements--
    print("Invalid PIN. Enter exactly 6 digits.")