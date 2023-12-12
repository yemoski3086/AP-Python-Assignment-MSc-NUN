#Restaurant.py

class Restaurant: #Decalaration of Restaurant Class
    def __init__(self, restaurant_name, cuisine_type, number_served=0): #Constructor for Restaurant Class
        self._restaurant_name = restaurant_name
        self._cuisine_type = cuisine_type
        self._number_served = number_served
        

    def getRestaurantName( self ):
        return self._restaurant_name

    def getCuisineType ( self ):
        return self._cuisine_type
    
    def describe_restaurant(self):#Method to describe Restaurant
        print (self._restaurant_name," is specialized in " \
              + self._cuisine_type)

    def open_restaurant(self):#Method to send a personalized message that Restaurant is opened
        print("The Restaurant is opened")

    def set_number_served(self, number_served):#Method to set the number of Clients Served
        self._number_served = number_served
        return self._number_served

    def increment_number_served(self, increase):#Method to increment the number of Customers served
        self._number_served += increase
        return self._number_served


class IceCreamStand(Restaurant): #Class IceCreamStand class inherits from Restaurant Class
    
   
    
    def __init__(self, restaurant_name, cuisine_type, number_served): #Constructor of IceCreamStand Class
        super().__init__(restaurant_name, cuisine_type, number_served=0)
        flavors = ["Vanilla","Strawberry","Chocolate","Pistachio"]
        self._flavors = flavors
       

    def displayIcecreamFlavor( self ): #Method to display IceCream Flavor
        for i in range(len(self._flavors)):
            print("The list at index", i, "contains a", self._flavors[i])


 
restaurant = Restaurant("First Place", "African Yoruba Continental Dishes")
print (restaurant.getRestaurantName())
print (restaurant.getCuisineType())
restaurant.describe_restaurant()
restaurant.open_restaurant()
print("-----------------------------------------------------")
restaurant1 = Restaurant("Tasty Bite", "Sea Foods Delicacies")
restaurant2 = Restaurant("Jirade Foods", "Chinese Food")
restaurant3 = Restaurant("Licking Fingers Restaurant", "English Breakfast")
print("-----------------------------------------------------")
restaurant1.describe_restaurant()
print("-----------------------------------------------------")
restaurant2.describe_restaurant()
print("-----------------------------------------------------")
restaurant3.describe_restaurant()
print("-----------------------------------------------------")
restaurant4 = Restaurant("Jugger Nut", "Vegetarian Restaurant")
print(restaurant4._number_served)
print("-----------------------------------------------------")
restaurant4._number_served = 5
print(restaurant4._number_served)
print("-----------------------------------------------------")
restaurant4.set_number_served(9)
print(restaurant4._number_served)
print("-----------------------------------------------------")
restaurant4.increment_number_served(6)
print(restaurant4._number_served)
print("-----------------------------------------------------")
icecreamObject = IceCreamStand("Icre Cream Delight", "Ice Cream", 5)
icecreamObject.displayIcecreamFlavor()
