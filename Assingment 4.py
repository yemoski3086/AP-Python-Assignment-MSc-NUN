# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 10:14:04 2023

@author: Admin
"""
# question (4)
print ('\n\n', "---------------------Questin 4a-------------------------- ",'\n')

# Using a for loop
print("--------------------------Using a for loop---------------------------",)

Lis = [1,2,3,4,5,6,7,8,9,10]
for i in Lis :
   print (i**3,)

# Using a list comprehension
print("-----------------------Using a list comprehension-----------------------")
copm =[i**3 for i in range(1,11)]
for x in copm:
    print (x)