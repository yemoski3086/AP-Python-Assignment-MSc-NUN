# -*- coding: utf-8 -*-


#MyName.py
class MyName:
    def __init__(self): #OnInit
        self.buffered = ""
        self.mName = "Olusola Ibikunle"
        self.famous_person = "Archimedes"
        self.message = " stated that, The upward bouyant force "
        self.message1=" exerted on a body immersed in a fluid, whether fully"
        self.message2=" or partially, is equal to the weight of fluid that the"
        self.message3=" body displaces."
        self.names=["Abbas","Ibrahim","Nuhu","shola"]
    #def write(self, text):
    def write(self):
        text=self.mName
        #self._buffered += text
        self.buffered=text
        # if "*" in self._buffered:
            #iasterisk = self._buffered.find("*") + 1
        iasterisk = self.buffered.upper()
        #print(self._buffered[0:iasterisk])
        print("Hello,",iasterisk,",I am taking some python classes" )
        #self._buffered = self._buffered[iasterisk:]
        #self._buffered = self._buffered[iasterisk:]
        iasterisk = self.buffered.lower()
        print("Hello,",iasterisk,",I am taking some python classes" )
        print("Hello,",text,",I am taking some python classes" )
        print(self.famous_person+self.message+self.message1+self.message2+self.message3)
        print(self.names[0]," has been awarded a project topic on natural computing")
        print(self.names[1]," has been awarded a project topic on robotics")
        print(self.names[2]," has been awarded a project topic on artificial intelligence")
        print(self.names[3]," has been awarded a project topic on operating systems")
        
    def flush(self):
        #print(self.buffered)
        self.buffered = ""
    def __len__(self): #This is a trick that I will add
        return len(self.buffered)
    
    #buffer = MyName() #a new StringBuffer is made
    #buffer.write("apple")
    #buffer.write("sauce*drum") #prints applesauce
    #buffer.write("sticks")
    
    #print len(buffer) #is 10
    
    #buffer.write("*leftovers") #prints drumsticks
    #buffer.flush() #prints leftovers


    #print len(buffer) #after flush, is 0