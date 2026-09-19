#------------------------------
# Name: Aleeyah P. Dela Vega
# Section: 8-Adelfa
# Title: Hands-on Activity 1 - Payment Method Checker
# Date: 09/17/26
#------------------------------

#--Assign allowed/acceptable values--
valid_payment_method = ["Cash", "GCash", "Card"]

#--Ask user for their payment method--
payment_method = str(input("Enter your payment method: "))

#--Check if the payment method the user inputted is valid--
if payment_method in valid_payment_method:
    #--Output this result if the payment method is valid--
    print("Valid payment method.")
else:
    #--Output this if the payment method is invalid--
    print("Invalid payment method.")