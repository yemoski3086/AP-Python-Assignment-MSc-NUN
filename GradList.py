#This GradList class is written by Adejumo Adeyemi Oluwaseun for
# Advance Programming Course with Python. It basically prints 
# out messages to the user of the program about personalized
#messages about my graduation ceremony as enumerated in the
#various methods contained in the class
class GradList:
    def __init__(self):  #OnInit
        self.Invited_Persons = [] #A List Object of Invited Persons
        self.NewlyInvited_Persons = [] #A List Object of newly invited persons
        self.Invited_Persons.append("Akinwumi Rafiu Adejumo")# Initilaize the first Element of invited person List object
        self.Invited_Persons.append("Sinmiat Moji Adejumo")# Initilaize the second Element of invited person List object
        self.Invited_Persons.append("Adeyinka Abiola Adejumo") # Initilaize the Third Element of invited person List object

        self.NewlyInvited_Persons.append("Chidi Enwerem")# Initilaize the first Element of newly invited person List object
        self.NewlyInvited_Persons.append("Kilyobas Binga")# Initilaize the second Element of invited person List object
        self.NewlyInvited_Persons.append("Valentine Ikpo Chibueze") # Initilaize the Third Element of invited person List object

        
    def emptyList(self):#Method to empty list of Invited Persons List Object
        del self.Invited_Persons[0]
        del self.Invited_Persons[0]
        if len(self.Invited_Persons) == 0:
            print("The list is empty")

    def changeOrder(self):#Method to sort List object alphabetically and reverse
        alpha_bet = sorted(self.Invited_Persons)
        print(alpha_bet)
        alpha_bet.reverse()
        print(alpha_bet)
    def reduceInvite(self):#Method to reduce number of invited persons
        first_person = self.Invited_Persons.pop(2)
        print("Sorry, ",first_person," I cannot invite you to the graduation ceremony.")
        second_person = self.Invited_Persons.pop(2)
        print("Sorry, ",second_person," I cannot invite you to the graduation ceremony.")
        third_person = self.Invited_Persons.pop(2)
        print("Sorry, ",third_person," I cannot invite you to the graduation ceremony.")
        fourth_person = self.Invited_Persons.pop(2)
        print("Sorry, ",fourth_person," I cannot invite you to the graduation ceremony.")
        print(self.Invited_Persons[0],", you are still invited to the graduation ceremony holding on the 25th March, 2025.")
        print(self.Invited_Persons[1],", you are still invited to the graduation ceremony holding on the 25th March, 2025.")
    def newGuest(self):# Method to add newly invited persons
        self.Invited_Persons.insert(0,self.NewlyInvited_Persons[0])
        self.Invited_Persons.insert(2,self.NewlyInvited_Persons[1])
        self.Invited_Persons.append(self.NewlyInvited_Persons[2])
        i = 0
        while i < len(self.Invited_Persons):
        #for i in self.Invited_Persons:
            print("Sorry, ",self.Invited_Persons[i],", I can invite only teo persons to the graduation")
            i += 1
    def invite(self): #Method to send a print message for those persons still invited
        i = 0
        while i < len(self.Invited_Persons):
        #for i in self.Invited_Persons:
            print(self.Invited_Persons[i],", you are hereby invited to my graduation at Nile University on 17th March, 2025")
            i += 1
    def replaceInvite(self): #Method to replace invitation
        self.Invited_Persons.append("Adebola Adenike Adejumo")
        i = 0
        while i < len(self.Invited_Persons):
        #for i in self.Invited_Persons:
            print(self.Invited_Persons[i],", you are hereby invited to my graduation at Nile University on 17th March, 2025")
            i += 1
    def allowedMoreInvite(self): #Method to allow more invites
        i = 0
        while i < len(self.NewlyInvited_Persons):
        #for i in self.Invited_Persons:
            print(self.NewlyInvited_Persons[i],", you are hereby invited to my graduation at Nile University on 17th March, 2025")
            i += 1
        
    def voidInvite(self): #Method to void invitation
        print(self.Invited_Persons[1]," could not make it to the graduation ceremony")
        self.Invited_Persons.remove("Sinmiat Moji Adejumo")
      
   
