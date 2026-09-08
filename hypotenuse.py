#------------------------------
#Name: Aleeyah Dela Vega
#Section: 8-Adelfa
#Title: Pythagorean Theorem Calculator
#Date: 08/27/26
#------------------------------

#--Import math for the square root and power function--
import math

#--Title of the program--
print("PYTHAGOREAN THEOREM CALCULATOR")

#--Ask user for the length of side a and b--
aSide = float(input("Enter the length of side a: "))
bSide = float(input("Enter the length of side b: "))

#--Get the power of 2 of side a and b--
aPower = pow(aSide, 2)
bPower = pow(bSide, 2)

#--Calculate side c (hypotenuse) using the Pythagorean Theorem--
cSide = math.sqrt(aPower + bPower)

#--Output the result--
print(f"The hypotenuse is: {cSide:.2f}")