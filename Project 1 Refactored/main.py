# Matthew Steuerer 
#
# April 24, 2020
#
# COMP 126-004RL 
#
# Project 1: Unit Conversion Python Program


# Input module called "myInput" because the word "input" is an inherent function in Python
# Attempting to use the term "input" for this function definition can cause confusion to 
# the programmer as well as the interpreter since it typically executes the inherent input function
def myInput():

	# Welcome Prompt When Program is Executed. 
	print("Welcome to the Knot Conversion Tool!")
	print("This program can convert the speed of an object (in feet per second) to knots!")

	# Input prompts for the calculation.
	feetPerSecond = float(input("Please provide the speed traveled (in feet per second) by the object in question: "))

	# Give the input the user entered to the main module 
	return feetPerSecond;

# conversionCalculation function 
def conversionCalculation(feetPerSecond):
	#Calculate Total Knots 
	# Constant value kept local to where the calculations are performed 
	CONVERSION_FACTOR = 0.592484

	# Perform the calculation 
	knots = feetPerSecond * CONVERSION_FACTOR

	# Give the result back to main for output 
	return knots

# Output function
def output(knots):
	# Print the passed knots value so that it can be printed to the user 
	print ("The equivalent speed measured in knots is: ", knots)
	#Terminate Program
	print("Thanks for using the Knot Conversion Tool!")
	print("To calculate another speed, please execute this program again.")
	print("Goodbye!")

# Main module from which all other functions are run 
def main():
	userEntered = myInput()
	result = conversionCalculation(userEntered)
	output(result)

# Necessary to run the main module in a python program 
# According to sources online, this is due to the interpreter automatically 
# assigning the value of "__main__" when the script is run through a shell environment
# such as terminal (what I use to run and debug scripts) 
# Benefits of this would include the fact that this script is only run directly and not 
# inadvertantly - it further modularizes the code for improved readability 
if __name__ == "__main__":
	main()
