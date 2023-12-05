# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 22:37:35 2023

@author: oibikunle
"""

#DictAlbum.py

class DictAlbum:
    def __init__(self):

        self.magician_names=["Abbas","Ibrahim","Nuhu","shola"]
        self.magician_namez=["Abbas","Ibrahim","Nuhu","shola"]
        self.artistName = ""
        self.albumTitle = ""
       
                   
       
    def promptUserz(self):
        
        
        i = 0
        #self.album=[]
        self.album = dict()
        self.buffered = ""
        
        while(True):
            
            print("Please put Artist Name and Album: ")
            self.artistName = input()
            print("Please put Artist Name and Album: ")
            self.albumTitle = input()
            #self.artistName = [int(i) for i in input("Artist Name(seperated by spaces): ").split("\n")]
            #self.albumTitle = [int(i) for i in input("Album Title(seperated by spaces): ").split("\n")]
            quitz = input("Enter 'Q' to QUIT, but enter any other letter to continue: ")
            if(quitz == 'Q'):
                
                

                         
                                    
                break
                               
            else:
                self.album[self.artistName] = self.albumTitle
                self.buffered += self.artistName
                self.buffered += ":"
                self.buffered += self.albumTitle
                self.buffered += ","
                #self.album.append({self.artistName : self.albumTitle})
                #i+1
                if "," in self.buffered:
                    iasterik = self.buffered.find(",")+1
                    me = self.buffered[0:iasterik]
                    print(me)
                    
                    self.buffered= self.buffered[iasterik:]
            
                    #print(self.buffered)
        for artistName in self.album:
                    print(artistName, "=", self.album[artistName])
        return self.album
    
    def make_album(self, numberTracks=None):
        self.album = dict()
        self.numberTracks = []
        if(numberTracks == None):
            self.album["JayZ" ] = "BluePrint 3" 
            self.album["RKelly"] = "TP2.COM" 
            self.album["Shina Peters"] = "Afro Juju"
        else:
            self.album["JayZ" ] = "BluePrint 3", numberTracks[0] 
            self.album["RKelly"] = "TP2.COM", numberTracks[1]
            self.album["Shina Peters"] = "Afro Juju", numberTracks[2]
            
        #self.album2 = promptUserz(self)
        #self.album |= self.album2
        return self.album

    def show_magicians(self):
        print(self.magician_names[0])
        print(self.magician_names[1])
        print(self.magician_names[2])
        print(self.magician_names[3])

        print(self.magician_namez[0])
        print(self.magician_namez[1])
        print(self.magician_namez[2])
        print(self.magician_namez[3])


class ChildDictAlbum(DictAlbum):

    
    def make_great(self):
        self.magician_names[0]= "The Great "+ self.magician_names[0]
        self.magician_names[1]= "The Great "+ self.magician_names[1]
        self.magician_names[2]= "The Great "+ self.magician_names[2]
        self.magician_names[3]= "The Great "+ self.magician_names[3]

        self.show_magicians()
