# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 10:29:44 2023

@author: Admin
"""

while True:
    try:
        # Get the user's age as input
        age = int(input("Enter your age (or type 'quit' to exit): "))

        # Check if the user wants to exit
        if age == 'quit':
            break

        # Determine the ticket price based on age
        if age < 3:
            ticket_price = 0  # Ticket is free for ages under 3
        elif 3 <= age <= 12:
            ticket_price = 5000  # Ticket is N5,000 for ages 3 to 12
        else:
            ticket_price = 10000  # Ticket is N10,000 for ages over 12

        # Display the ticket price to the user
        print(f"The cost of your movie ticket is N",ticket_price, "\n" )

    except ValueError:
        print("Please enter a valid age or 'quit' to exit.\n")
        