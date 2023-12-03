#MyName.py
#This Code is wriiten by Adejumo Adeyemi Oluwaseun as a course
#work in CPE811, Advanced Programming with Python
#The wrote method prints a quote by a famous person,
#Persomalized messages with my names in title-case,
#Upper-case and Lower-case
class MyName:#Class Declaration
    def __init__(self):  #OnInit
        self.buffered = ""
        self.mName = "Adejumo Adeyemi Oluwaseun" #Declare and initialize Variable 'mName' to hold my name
        self.famous_person = "Archimedes" #Declare variable 'famous_person' to hold the name of a famous person
        
        self.message = " stated that, The upward bouyant force "
        self.message1=" exerted on a body immersed in a fluid, whether fully"
        self.message2=" or partially, is equal to the weight of fluid that the"
        self.message3=" body displaces."
        #Declare and initialize a list object to hold the names of 4 classmates
        self.names=["Abbas","Ibrahim","Nuhu","shola"]
    
    #The write method prints messages about my name in Uppercase, Titlecase and Lowercase
    def write(self):
        text=self.mName
        
        self.buffered=text
      
        iasterisk = self.buffered.upper()
            
        print("Hello,",iasterisk,",I am taking some python classes" )
        
        iasterisk = self.buffered.lower()
        print("Hello,",iasterisk,",I am taking some python classes" )
        print("Hello,",text,",I am taking some python classes" )
        #The write method also prints a famous quote from a famous person
        print(self.famous_person+self.message+self.message1+self.message2+self.message3)
        #The Write method also accesses each element in the List object composed of names
        #of classmates in order to print personalized message on aech one of them
        print(self.names[0]," has been awarded a project topic on natural computing")
        print(self.names[1]," has been awarded a project topic on robotics")
        print(self.names[2]," has been awarded a project topic on artificial intelligence")
        print(self.names[3]," has been awarded a project topic on operating systems")

    def flush(self):
        #print(self.buffered)
        self.buffered = ""
    def __len__(self):  #This is a trick that I will add
        return len(self.buffered)


