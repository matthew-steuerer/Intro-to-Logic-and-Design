# First and Last Python Program
# Author: Matthew Steuerer
# Date 4/6/2020 
# COMP 126 Spring 2020 

#Describe program's purpose
print("This program can tell the user which name comes first and last alphabetically, given a list from the user.\n")

#Prompt user for input and store in our working variable
currentName = input("We will enter those names now. Please enter the first name in the list with the first letter capitalized: \n")

#Initialize results to the first name entered before loop so that they aren't empty 
alphaFirstName = currentName
alphaLastName = currentName
sentinel = "DONE"

#Condition controlled loop to perform our name comparisons
while currentName != sentinel:
	if currentName < alphaFirstName:
		alphaFirstName = currentName
	elif currentName > alphaLastName:
		alphaLastName = currentName

	#The loop will also be where we ask for further names 	
	print("Please enter another name. Remember: ONLY CAPITALIZE THE FIRST LETTER!")
	currentName = input("Enter the word \"DONE\" (without quotes) once all names have been entered.\n")

#Print out desired output according to specs 
print("The first name that appears in the list alphabetically is: " + alphaFirstName)
print("The last name that appears in the list alphabetically is: " + alphaLastName)
print("Thank you for names! Please execute this script again for another list!")









