#!/usr/bin/env python
# coding: utf-8

# In[14]:


a="Shehu Kakale Tilli"
c = "shehu kakale tilli"
b = "SHEHU KAKALE TLLLI"
print("Hello", a,"i am taking some python classes")
print(b)
print(c)
print(a)
print("Hello", a,"i am taking some python classes")
famous_person = "Godluck Ebele Jonathan once said"
message = '"Small stealing is not a corruption"'
print(famous_person,message)
names = ["Sunshine,","Timi,","Rukayya,","Maryam,","Fatima"]
print(names[0],names[1],names[2],names[3],names[4], )
    


# In[105]:


graduation = ["Sunshine,","Timi,","Rukayya,","Maryam,","Fatima"]
print("i am inviting",graduation[0],"to our graduation ceremony")
print("i am inviting",graduation[1],"to our graduation ceremony")
grad = "Timi"
print("the guest that can not make is",grad)
graduation[1] = "Hauwa"
print(graduation)
print("i am inviting",graduation[0],"to our graduation ceremony")
print("i am inviting",graduation[1],"to our graduation ceremony")
print("i am inviting",graduation[2],"to our graduation ceremony")
print("i am inviting",graduation[3],"to our graduation ceremony")
print("i am inviting",graduation[4],"to our graduation ceremony")
print("i am here to inform you that i am allow to invite more guest")
graduation.insert(0, "Rabi")
graduation.insert(3, "Aisha")
graduation.append("Salamatu")
print(graduation)
print("i am inviting",graduation[0],"to our graduation ceremony")
print("i am inviting",graduation[1],"to our graduation ceremony")
print("i am inviting",graduation[2],"to our graduation ceremony")
print("i am inviting",graduation[3],"to our graduation ceremony")
print("i am inviting",graduation[4],"to our graduation ceremony")
print("i am inviting",graduation[5],"to our graduation ceremony")
print("i am inviting",graduation[6],"to our graduation ceremony")
print("i am inviting",graduation[7],"to our graduation ceremony")
print("Due to the organazational issues that affected the graduation i am only allow to invite two people")
graduation.pop(0)
print("sorry i cant invite you to graduation",graduation.pop(0))
graduation.pop(1)
print("sorry i cant invite you to graduation",graduation.pop(1))
graduation.pop(2)
print("sorry i cant invite you to graduation",graduation.pop(2))
print(graduation[0],"you are invited to graduation ceremony")
print(graduation[1],"you are invited to graduation ceremony")
print(graduation)
graduation.sort()
print(graduation)
graduation.reverse()
print(graduation)
del graduation[0]
print(graduation)
del graduation[0]
print(graduation)


# In[10]:


def make_album(artist, title):
    p_squre = artist  
    Game_Over = title  
    return p_square
    print()


# In[1]:


cubes = []
for num in range(1,11):
    cube = num**3
    cubes.append(cube)
    print(cube)
    

cubes_lc = [i**3 for i in range(1,11)]
print(cubes_lc)


# In[2]:


while True:
    age = input("Enter your age (type 'quit' to exit): ")
    
    if age.lower() == 'quit':
        break  # Exit the loop if the user enters 'quit'
    
    age = int(age)
    
    if age < 3:
        print("Your ticket is free.")
    elif 3 <= age <= 12:
        print("Your ticket costs 5000.")
    else:
        print("Your ticket costs 10000.")


# In[3]:


active = True

while active:
    age = input("Enter your age (type 'quit' to exit): ")
    
    if age.lower() == 'quit':
        active = False  # Set active to False to exit the loop
    else:
        age = int(age)
        
        if age < 3:
            print("Your ticket is free.")
        elif 3 <= age <= 12:
            print("Your ticket costs 5000.")
        else:
            print("Your ticket costs 10000.")


# In[ ]:


while True:
    age = input("Enter your age (type 'quit' to exit): ")
    
    if age.lower() == 'quit':
        break  # Exit the loop if the user enters 'quit'
    
    age = int(age)
    
    if age < 3:
        print("Your ticket is free.")
    elif 3 <= age <= 12:
        print("Your ticket costs 5000.")
    else:
        print("Your ticket costs 10000.")


# In[ ]:


def make_album(artist, title, tracks=None):
    album = {'artist': artist, 'title': title}
    if tracks:
        album['tracks'] = tracks
    return album

# Make three dictionaries representing different albums
album1 = make_album('Artist1', 'Album1', 10)
album2 = make_album('Artist2', 'Album2')
album3 = make_album('Artist3', 'Album3', 15)

# Print each return value to show that the dictionaries are storing the album information correctly
print(album1)
print(album2)
print(album3)

# Write a while loop that allows users to enter an album's artist and title
while True:
    artist_input = input("Enter the artist (type 'quit' to exit): ")
    if artist_input.lower() == 'quit':
        break
    
    title_input = input("Enter the album title: ")
    
    # Call make_album() with the user's input and print the created dictionary
    user_album = make_album(artist_input, title_input)
    print(user_album)


# In[1]:


def show_musicians(musicians):
    for musician in musicians:
        print(musician)

def make_great(musicians):
    great_musicians = [f"Great {musician}" for musician in musicians]
    return great_musicians

# List of musicians
musicians_list = ["John", "Paul", "George", "Ringo"]

# Call show_musicians to display original list
print("Original List:")
show_musicians(musicians_list)

# Call make_great function and store the result in a new list
new_list = make_great(musicians_list.copy())

# Call show_musicians to display modified list
print("\nList with 'Great' added:")
show_musicians(new_list)

# Call show_musicians to display the original list again
print("\nOriginal List (unchanged):")
show_musicians(musicians_list)


# In[1]:


alien_color = "green"

if alien_color == "green":
    print("Congratulations! You just earned 5 points.")

#### Version Failing the If Test:
# Version Failing the If Test
alien_color = "red"  # You can change this to "yellow" for a different failing scenario

if alien_color == "green":
    print("Congratulations! You just earned 5 points.")


# In[1]:


alien_color = "green"
if alien_color=="green":
    print("congratulation you earned 5 point for shooting the the alien")


# In[6]:


alien_color = "red"
if alien_color=="green":
    print("congratulation you earned 5 point for shooting the the alien")
else:
    print("congratulation you earned 10 point for shooting the the alien")
    


# In[2]:


alien_color = "green"
if alien_color=="green":
    print("congratulation you earned 5 point for shooting the the alien")
elif alien_color =="yellow":
    print("congratulation you earned 10 point for shooting the the alien")
else:
    print("congratulation you earned 15 point for shooting the the alien")


# In[1]:


alien_color = "yellow"
if alien_color=="green":
    print("congratulation you earned 5 point for shooting the the alien")
elif alien_color =="yellow":
    print("congratulation you earned 10 point for shooting the the alien")
else:
    print("congratulation you earned 15 point for shooting the the alien")


# In[5]:


alien_color = "red"
if alien_color=="green":
    print("congratulation you earned 5 point for shooting the the alien")
elif alien_color =="yellow":
    print("congratulation you earned 10 point for shooting the the alien")
else:
    print("congratulation you earned 15 point for shooting the the alien")


# In[ ]:




