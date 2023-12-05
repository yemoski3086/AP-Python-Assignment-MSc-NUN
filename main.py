#main.py
#This main class was written by Adejumo Adeyemi Oluwaseun
#with Nile university ID Number nun20232809
#This main class instantiates and used the methods
#of 5 different classes by imperting them to the main 
#Class file
from MyName import MyName 
from GradList import GradList
from DictAlbum import DictAlbum
from DictAlbum import ChildDictAlbum
from CubeandMovieTheater import CubeandMovieTheater
from AlienColor import AlienColor
from random import randint

a = MyName()#Instantiate the class of MyName
a.write()#Prints personalized messages of a famous person, myself and 4 classmates
a.flush()#Flush all variables and re-initialize them
print(".....................................................................")
b = GradList()# Instantiate the GradList Class
b.invite()# method to invite guests to the Graduation ceremony
print(".....................................................................")
b.voidInvite() #Method to void invitations previously given out
print(".....................................................................")
b.replaceInvite() #Method te replace some of those originally invited for the Graduation
print(".....................................................................")
b.allowedMoreInvite() #Methos to invite more persons for the Graduation
print(".....................................................................")
b.newGuest() #Method to add more guests to the invitation list of those invited
print(".....................................................................")
b.reduceInvite() #Method to remove some names of on the list of those invited for the Graduation ceremony
print(".....................................................................")
b.changeOrder() #Method to change the order of thise invited alphabetically and reverse
print(".....................................................................")
b.emptyList() #Method to empty the List
print(".....................................................................")
c = DictAlbum() #Create an instance of Dictionary AlbumS
album = c.make_album() #Class make_Album() method and stores the return value in Dictionary object
print(album) #Prints the Dictionary object which is a record of Artist and Albums
album1 = c.make_album([15,20,30]) #Calls an overloaded function, by adding number of tracks to each Album
print(album1)
print(".....................................................................")
albumz=c.promptUserz() #Creates a Dictionary of Records from User Inputs
print(albumz)
album1 = c.make_album #Calls make_album() method
print(".....................................................................")
c.show_magicians()#Method to print the names of magicians
d = ChildDictAlbum() #method to invoke the method of a parent class from the child class 
d.make_great() #method to modify the original list object of Magicians
print(".....................................................................")
e = CubeandMovieTheater() #Instantiating a class object
e.calculateTenCubes() #Method to calculate the cube values of first ten integers by using List Expression
e.loopforTenCubes() #Method to calculate the cube values of first ten integers by using FOR-LOOP
print(".....................................................................")
e.conditionWhileTest() #Movie ticket cost categorization by age using while condition while getting input from Users
print(".....................................................................")
e.activeVariableTest() #Movie ticket cost categorization by age using active variable while getting input from Users
print(".....................................................................")
e.breakStatementTest() #Movie ticket cost categorization by age using BREAK while getting input from Users
print(".....................................................................")
f = AlienColor() #Instantiating the class object
f.colorTest() #Method version one about shooting different colors of Alien while print out corresponding score of the Gamer
f.anotherColorTest() #Method version two about shooting different colors of Alien while print out corresponding score of the Gamer
f.anotherAnotherColorTest() #Method version three about shooting different colors of Alien while print out corresponding score of the Gamer
