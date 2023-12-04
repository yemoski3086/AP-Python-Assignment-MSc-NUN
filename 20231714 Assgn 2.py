# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 19:42:24 2023

@author: oibikunle
"""

class Gradlist:
    def __init__(self): #OnInit
        self.Invited_Persons = []
        self.NewlyInvited_Persons =[]
        self.Invited_Persons.append ("Akinwumi Rafiu Adejumo")
        self.Invited_Persons.append ("Sinmiat Moji Adejumo") 
        self.Invited_Persons.append ("Adeyinka Abiola Adejumo") 
        
        self.NewlyInvited_Persons.append ("Chidi Enwerem")
        self.NewlyInvited_Persons.append ("Kilyobas Binga")
        self.NewlyInvited_Persons.append ("Valentine Ikpo Chibueze")
        
    def emptyList (self):
        del self.Invited_Persons[0]
        del self.Invited_Person[0]
        if len(self.Invited_Persons) == 0:
            print("The list is empty")
            
    def ChangeOrder(self):
        alpha_bet = sorted(self.Invited_Persons)
        print (alpha_bet)
        alpha_bet.reverse()
        print(alpha_bet)
    def reduceInvited (self):
        first_person = self.Inivted_Persons.pop(2)
        print("Sorry,",first_person," I cannot invite you to the graduation ceremony,")
        second_person = self.Inivted_Persons.pop(2)
        print("Sorry,",second_person," I cannot invite you to the graduation ceremony,")
        third_person = self.Inivted_Persons.pop(2)
        print("Sorry,",third_person," I cannot invite you to the graduation ceremony,")
        fourth_person = self.Inivted_Persons.pop(2)
        print("Sorry,",fourth_person," I cannot invite you to the graduation ceremony,")
        print(self.Invited_Persons[0],", you are still invited to the graduation ceremonyholding on the 25th March, 2025.")
        print(self.Invited_Persons[1],", you are still invited to the graduation ceremonyholding on the 25th March, 2025.")
    def newGuest(self):
        self.Invited_Persons.insert(0,self.NewlyInvited_Persons[0])
        self.Invited_Persons.insert(2,self.NewlyInvited_Persons[1])
        self.Invited_Persons.append(self.NewlyInvited_Persons[2])
        i = 0
        while i < len(self.Invited_Persons):
        #for i in self.Ivited_Persons:
            print("Sorry,",self.Invited_Persons[i],", I can invite only two persons to the graduation")
            i += 1
    def invite(self):
        i = 0
        while i < len(self.Invited_Persons):
        #for i in self.Inivted_Persons:
            print(self.Invited_Persons[i],", you are hereby invited to my Nile University on 17th March, 2025")          
            i += 1
    def replaceInvited(self):
        self.Invited_Persons.append("Adebola Adenike Adejumo")
        i = 0
        while i < len(self.Invited_Persons):
        #for i in self.Invited_Persons:
            print(self.NewlyInvited_Persons[1],",you are hereby invited to my graduation on 17th March, 2025")
            i += 1
    def allowedMoreInvite(self):
        i = 0
        while i < len(self.NewlyInvited_Person):
        #for i in self.Invited_Persons:
            print(self.NewlyInvited_Persons[i],", you are hereby invited to my graduation on 17th March, 2025")
            i += 1
        
        def voidInvite(self):
            print(self.Invited_Persons[i]," could not make it to the graduation ceremony")
            self.Invited_Persons.remove("Sinmiat Moji Adejumo")
        
            
            
            