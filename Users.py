#User.py
from random import randint

class User:


    def __init__(self, first_name, last_name, login_attempts=0):#Constructor for the user class
        self._first_name = first_name #first_name attribute
        self._last_name = last_name #last_name attribute
        self._login_attempts = login_attempts #login_attempts attribute
        self.gender=["Male","Female"] #User Gender Attribute
        self.random_gender_index = randint(0, 1)
        self.randomAge=randint(0, 120) #User Age Attribute
        self.anotherRandomHeight=randint(0, 11) #User Height Attribute

    def describe_User( self ): #Method to describe a User
        #return self._restaurant_name
        print("My Name is : "+ self._first_name + " " +self._last_name)
        print("My Age is : ", self.randomAge)
        print("My Gender is: "+ self.gender[self.random_gender_index])
        print("My Height is: ", self.anotherRandomHeight)

    def greet_User(self) : #Method to print a personalized message to the User
        print("You are welcome " + self._first_name + " " +self._last_name)
    
    def reset_login_attempts(self): #Method to reset the number of login attempts
        self._login_attempts = 0
        return self._login_attempts

    def increment_login_attempts(self): #Method to increment the nuber of login attempts
        self._login_attempts += 1
        return self._login_attempts
        




class Admin(User): #Admin Class that inherits from the User Class
    
    def __init__(self, first_name, last_name): #Constructor of Admin Class
        super().__init__(self, first_name, last_name)
        privileges = ["Can add Post","Can delete Post","Can ban User"]
        self._privileges = privileges
       

    def show_privileges( self ): #Method to list the privileges of an Admin User
        for i in range(len(self._privileges)):
            print("These are the privileges of Admin", i, " such as ", self._privileges[i])


class Privileges: #Privileges Class
    
    def __init__(self, first_name, last_name):
        super().__init__(self, first_name, last_name)
        privileges = ["Can add Post","Can delete Post","Can ban User"]
        self._privileges = privileges
       

    def show_privileges( self ):
        for i in range(len(self._privileges)):
            print("These are the privileges of Admin", i, " such as ", self._privileges[i])




 
userz  = User("Adejumo", "Adeyemi")
userz.describe_User()
userz.greet_User()
print("--------------------------------------")
userz1  = User("Fagha", "Faloughi")
userz1.describe_User()
userz1.greet_User()
print("--------------------------------------")
userz2  = User("Datola", "Daviez")
userz2.describe_User()
userz2.greet_User()
print("--------------------------------------")
userz3  = User("urene", "Ezekiel")
userz3.describe_User()
userz3.greet_User()
print("--------------------------------------")
userLogin  = User("John", "Bull")
print(userLogin.increment_login_attempts())
print(userLogin.increment_login_attempts())
print(userLogin.reset_login_attempts())
print("--------------------------------------")
admin = Admin("Bammy", "Fakzy")
admin.show_privileges()
