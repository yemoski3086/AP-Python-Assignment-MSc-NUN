# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 05:12:06 2023

@author: Admin

"""
# Part a: If statement

print ('\n\n', "---------------------Questin 5a-------------------------- ",'\n') 

alien_color = 'green'

if alien_color == 'green':
    print("Congratulations! You just earned 5 points.")
    
    
    
 # part b: Version that fails the if test (no output)   
print ('\n\n', "---------------------Questin 5b-------------------------- ",'\n') 

if alien_color != 'green':
    print("This won't be printed.")
    
alien_color = 'green'

if alien_color == 'green':
    print("Congratulations! You just earned 5 points.")
else:
    print("Congratulations! You just earned 10 points.")
    
        
# Part c: If-Elif-Else chain
print ('\n\n', "---------------------Questin 5c (green)-------------------------- ",'\n') 

alien_color = 'green'

# Version for green alien (prints message for 5 points)
if alien_color == 'green':
    print("Congratulations! You just earned 5 points.")
elif alien_color == 'yellow':
    print("Congratulations! You just earned 10 points.")
else:
    print("Congratulations! You just earned 15 points.")
    
    
# Version for yellow alien (prints message for 10 points)
print ('\n\n', "---------------------Questin 5c (yellow)-------------------------- ",'\n') 

alien_color = 'yellow'

if alien_color == 'green':
    print("Congratulations! You just earned 5 points.")
elif alien_color == 'yellow':
    print("Congratulations! You just earned 10 points.")
else:
    print("Congratulations! You just earned 15 points.")
    
# Version for red alien (prints message for 15 points)
print ('\n\n', "---------------------Questin 5c (red)-------------------------- ",'\n') 
  
alien_color = 'red'

if alien_color == 'green':
    print("Congratulations! You just earned 5 points.")
elif alien_color == 'yellow':
    print("Congratulations! You just earned 10 points.")
else:
    print("Congratulations! You just earned 15 points.")