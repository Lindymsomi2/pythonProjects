# Python While Loop Challenge
import math
# Initialize a variable 
current_number = 1
square = current_number * current_number

# Print the square of numbers until the square is greater than 20
while square <= 20:
    print("The square of %d is %d" %(current_number, square))
    current_number += 1
    square = current_number * current_number
    
else: 
    print("Loop completed")