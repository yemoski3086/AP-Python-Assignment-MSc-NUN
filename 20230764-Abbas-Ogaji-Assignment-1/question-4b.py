def is_valid_integer(input_str):
    try:
        int(input_str)
        return True
    except ValueError:
        return False

# Use a conditional test in the while statement to stop the loop.
def approach_one():
    while True:
        # Ask for artist name
        age = input("Enter your age (or enter `quit` to exit)")

        # Conditional test to break while loop
        if is_valid_integer(age) is False:
            print('Invalid age value provided')
            break

        age_value = int(age)
        if age_value < 3:
            print('Cost of your ticket is: Free')
        elif (age_value > 2 and age_value <= 12 ):
            print('Cost of your ticket is: N5,000')
        elif (age_value > 12 ):
            print('Cost of your ticket is: N12,000')

# Use an active variable to control how long the loop runs.
def approach_two():
    active = True
    while active:
        # Ask for artist name
        age = input("Enter your age")
        
        if is_valid_integer(age) is False:
            print('Invalid age value provided')
            active = False
            break

        age_value = int(age)
        if age_value < 3:
            print('Cost of your ticket is: Free')
        elif (age_value > 2 and age_value <= 12 ):
            print('Cost of your ticket is: N5,000')
        elif (age_value > 12 ):
            print('Cost of your ticket is: N12,000')

# Use a break statement to exit the loop when the user enters a 'quit' value.
def approach_three():
    while True:
        # Ask for artist name
        age = input("Enter your age (or enter `quit` to exit)")

        # Check if the user wants to quit
        if age.lower() == 'quit':
            break  # Exit the loop if 'q' is entered
        
        if is_valid_integer(age) is False:
            print('Invalid age value provided')
            continue

        age_value = int(age)
        if age_value < 3:
            print('Cost of your ticket is: Free')
        elif (age_value > 2 and age_value <= 12 ):
            print('Cost of your ticket is: N5,000')
        elif (age_value > 12 ):
            print('Cost of your ticket is: N12,000')
