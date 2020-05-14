# Matthew Steuerer 
#
# March 6, 2020
#
# COMP 126-004RL 
#
# Homework 2: Software Licenses Sales Program
#
# A program that will ask the user for a hypothetical amount of software licenses they wish to purchase.
# Demonstrates use of nested if structures, relational operators, and string formatting in python. 

# Variable Declarations and Initializations
# NOTE: In python, variables do not need to be declared or initialized, and are often created when needed. 
#        

numLicenses = 0 # Number of licenses to purchase entered by user 
discount = 0 # Discount customer might be eligible for based on number of licenses they purchase
unitPrice = 0.0 # Price per license, after discounts are applied 
totalAmountDue = 0.0 # The total price of all licenses together, after discount is applied  
totalWithoutDiscount = 0.0 # The total price of all licenses if no discounts were applied 
totalAmountSaved = 0.0 # The total amount of money saved with the discount on the purchase 
LICENSE_PRICE = 99 # Representing a constant price advertised for one software license 


# Welcome Prompt When Program is Executed
print("Welcome to The Best Software Company!")
print("This program will take your order for licenses you wish to purchase!")

# Asking for User Input, the number of licensese they would like to purchase 
numLicenses = int(input("Please provide the number of software licenses you would like to buy: "))

#Calculate any discounts the customer might be eligible for
if numLicenses >= 100:
	discount = 0.5
elif numLicenses >= 10 and numLicenses <= 19:
	discount = 0.2
elif numLicenses >= 20 and numLicenses <= 49:
	discount = 0.3
elif numLicenses >= 50 and numLicenses <= 99:
	discount = 0.4
else:
	discount = 0

# Calculate all variables to determine unit price, total amount due, and total amount saved 

if discount > 0:
	unitPrice = LICENSE_PRICE - LICENSE_PRICE * discount 
else:
	unitPrice = LICENSE_PRICE

totalAmountDue = unitPrice * numLicenses
totalWithoutDiscount = LICENSE_PRICE * numLicenses
totalAmountSaved = totalWithoutDiscount - totalAmountDue
discountPercentage = discount * 100


# Display all calculated outputs 
print ("Your purchase qualifies for a discount!")
print ("Your total discount is: {}%".format(discountPercentage))
print ("Your total price per license is: ${:,.2f}".format(unitPrice))
print ("Your total amount due is: ${:,.2f}".format(totalAmountDue))

# Check if anything was saved 
if totalAmountSaved > 0:
	print ("Your total amount saved is: ${:,.2f}".format(totalAmountSaved))

#Terminate Program
print("Thank you for your order at The Best Software Company!")
print("To make another order, please run the program again!")
print("Goodbye!")
