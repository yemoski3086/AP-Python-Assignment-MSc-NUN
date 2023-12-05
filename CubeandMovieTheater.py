#CubeandMovieTheater.py
#This class was written by Adejumo Adeyemi Oluwaseun
#For evaluating Mathematical expression for the cube
#of the first ten integers using List Expressions
#and FOR-LOOP
#Also this class does movie ticket costing using
#Age categorization and cinditional loops to get user
#Inputs
import time

class CubeandMovieTheater:
    def __init__(self):

        self.buffered = ""
        
    #Method to calculate the cube values of first ten integers by using List Expression
    def calculateTenCubes(self):
        x=1
        y=2
        a=3
        b=4
        c=5
        d=6
        e=7
        f=8
        g=9
        h=10
        
        self.FirstTenCubes=['x**3','y**3','a**3','b**3','c**3','d**3','e**3','f**3','g**3','h**3']
        Number_of_calcs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print(eval(self.FirstTenCubes[0],{"x":x}))
        print(eval(self.FirstTenCubes[1],{"y":y}))
        print(eval(self.FirstTenCubes[2],{"a":a}))
        print(eval(self.FirstTenCubes[3],{"b":b}))
        print(eval(self.FirstTenCubes[4],{"c":c}))
        print(eval(self.FirstTenCubes[5],{"d":d}))
        print(eval(self.FirstTenCubes[6],{"e":e}))
        print(eval(self.FirstTenCubes[7],{"f":f}))
        print(eval(self.FirstTenCubes[8],{"g":g}))
        print(eval(self.FirstTenCubes[9],{"h":h}))

    #Method to calculate the cube values of first ten integers by using FOR-LOOP
    def loopforTenCubes(self):

        i=0
        n=10
        self.FirstTenCubes=['1**3','2**3','3**3','4**3','5**3','6**3','7**3','8**3','9**3','10**3']
        for i in range(n):
            
            print(eval(self.FirstTenCubes[i]))

    #First version method of theatre ticket ticket calculation using WHILE-LOOP
    def conditionWhileTest(self):
       
        while(True):
            print("How old are you? ")
            print("Enter number 0 of the alphabet to quit")
            self.age = int(input())
            if(self.age==0):
                break
            elif(self.age<=3 and self.age>0):
                print("your movie ticket is free")
            elif(self.age>=3 and self.age<=12):
                print("your movie ticket costs 5000 naira")
            elif(self.age>12):
                print("your movie ticket costs 10,000 naira")
            
    #Second version method of theatre ticket ticket calculation using COUNTDOWN    
    def activeVariableTest(self):
        
        countdown = 3
        while(countdown > 0):
            
            print("How old are you? ")
            self.age = int(input())
            countdown -= 1
            if(self.age<3):
                print("your movie ticket is free")
            elif(self.age>=3 and self.age<=12):
                print("your movie ticket costs 5000 naira")
            elif(self.age>12):
                print("your movie ticket costs 10,000 naira")
            else:
                                
                (self.age)
                print("Enter a valid input")
     
    #First version method of theatre ticket ticket calculation using BREAK
    def breakStatementTest(self):
       
        
        while True:
                                   
            print("How old are you? ")
            print("enter number 0 to quit")
            self.age = int(input())
            if(self.age == 0):
                break
            elif(self.age<3):
                         
                  print("your movie ticket is free")
            elif(self.age>=3 and self.age<=12):
                  print("your movie ticket costs 5000 naira")
            elif(self.age>12):
                  print("your movie ticket costs 10,000 naira")
       

   

        
        
    
        
       
                
                

               
          
    
    
                    
          



   
     
        

