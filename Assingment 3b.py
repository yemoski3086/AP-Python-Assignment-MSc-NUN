# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 08:04:46 2023

@author: Admin
"""
print ('\n',"---------------------THE MAGICIANS IN THE LIST-------------------------- ",'\n')

magicians = ["Habib", "Ola", "Okeke"]

# Write a function called show_magicians() to print the names
def show_magicians(magicians_list):
    for magician in magicians_list:
        print(magician)

# Call show_magicians() with the list of magician's names
show_magicians(magicians)
print ('\n',"---------------------THE GRATE (MODIFIED) MAGICIANS LIST-------------------------- ",'\n')


# Write a function called make_great() to modify the list by adding "the Great" to each name
def make_great(magicians_list):
    great_magicians = [magician + " the Great" for magician in magicians_list]
    return great_magicians

# Call make_great() and show the modified list
modified_magicians = make_great(magicians.copy())
show_magicians(modified_magicians)

# Call make_great() with a copy of the original list and store the new list in a separate variable
new_magicians_list = make_great(magicians.copy())

# Show both lists to demonstrate one with the original names and one with "the Great" added
print ('\n',"---------------------THE ORIGINAL AND THE MODIFIED LIST-------------------------- ",'\n')


show_magicians(magicians)

show_magicians(new_magicians_list)