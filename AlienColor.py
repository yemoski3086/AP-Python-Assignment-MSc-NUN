#AlienColor.py
# This class was written by Adejumo Adeyemi Oluwaseun
# by using a random number generator to simulate and
# Alien Shooting Game and printing the corresponding
# reward to the Game Player
from random import randint

class AlienColor:
    def __init__(self):

        
        self.alien_color=["green","yellow","red"]
        self.randomNumber=randint(0, 2)
        self.anotherRandomNumber=randint(0, 2)
    def colorTest(self):
        if(self.alien_color[self.randomNumber]=="green"):
            print("You just earned 5 points")
            
        
    def anotherColorTest(self):
        if(self.alien_color[self.randomNumber]=="green"):
            print("You just earned 5 points")
        else:
            print("You just earned 10 points")


    def anotherAnotherColorTest(self):
        if(self.alien_color[self.randomNumber]=="green"):
            print("You just earned 5 points")
        elif(self.alien_color[self.randomNumber]!="yellow"):
            print("You just earned 10 points")
        else:
            print("You just earned 15 points")
        

   

        
        
    
        
       
                
                

               
          
    
    
                    
          



   
     
        

