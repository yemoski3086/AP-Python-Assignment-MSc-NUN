#4a
cubes = [] #create an empty list
for number in range(1, 11): #loop the range 1-10
    cube = number ** 3 # Calculate the cube of the number
    cubes.append(cube) # Add the cube to the list

for cube in cubes:
    print(cube)
cubes = [number ** 3 for number in range(1, 11)]
print(cubes)

#4b
# Use a conditional test in the while statement to stop the loop.
age = input("Enter your age or 'quit' to exit: ")
while age != 'quit':   
    age = int(age) 
    if age < 3:  
        print("Your ticket is free.")
    elif age <= 12:  
        print("Your ticket is N5,000.") 
    else:    
        print("Your ticket is N10,000.")
    age = input("Enter your age or ‘quit’ to exit: ")


#Use an active variable to control how long the loop runs.
active = True # Set the active variable to True while active: # Loop while the active variable is true
age = input("Enter your age or ‘quit’ to exit: ") # Ask the user for their age 
if age == 'quit': # If the user enters ‘quit’ 
    active = False # Set the active variable to False 
else: # If the user enters an age 
        age = int(age) # Convert the age to an integer 
if age < 3: # If the age is less than 3 
    print("Your ticket is free.") # The ticket is free 
elif age <= 12: # If the age is between 3 and 12 
    print("Your ticket is N5,000.") # The ticket is N5,000 
else: # If the age is over 12 
    print("Your ticket is N10,000.") # The ticket is N10,000



# Use a break statement to exit the loop when the user enters a 'quit' value.
while True: # Loop indefinitely 
    age = input("Enter your age or ‘quit’ to exit: ") # Ask the user for their age 
    if age == 'quit': # If the user enters ‘quit’ 
        break # Break out of the loop 
    age = int(age) # Convert the age to an integer 
    if age < 3: # If the age is less than 3 
        print("Your ticket is free.") # The ticket is free 
    elif age <= 12: # If the age is between 3 and 12 
        print("Your ticket is N5,000.") # The ticket is N5,000 
    else: # If the age is over 12 
        print("Your ticket is N10,000.") # The ticket is N10,000
