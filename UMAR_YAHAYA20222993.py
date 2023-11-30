#!/usr/bin/env python
# coding: utf-8

# In[20]:


A = "Umar Yahaya"
B = "Umar Yahaya"
C = "UMAR YAHAYA"
print("Hello I'm Taking Some Python Classes")
print(A)
print(B)
print(C)
print("Hello I'm Taking Some Python Classes")
famous_person = "T. J. Watson 1943 Said"
message = '"I think there is a world market for may be five Computers."'
print(famous_person,message)
names = ["Nuhu,","Shehu,","Sadiq,","Ibrahim,","Najibullah"]
print(names[0],names[1],names[2],names[3],names[4], )


# In[68]:


convocation = ["Nuhu,","Shehu,","Sadiq,","Ibrahim,","Najibullah"]
print("I'm Inviting",convocation[0],"To Our Graduation Ceremony")
print("I'm Inviting",convocation[1],"To Our Graduation Ceremony")
print("I'm Inviting",convocation[2],"To Our Graduation Ceremony")
print("I'm Inviting",convocation[3],"To Our Graduation Ceremony")
print("I'm Inviting",convocation[4],"To Our Graduation Ceremony")
convoc = "Shehu"
print("The Guest That can't Make it is",convoc)
convocation[1] = "Abdulhamid"
print(convocation)
print("I'm Inviting",convocation[0],"To Our Graduation Ceremony")
print("I'm Inviting",convocation[1],"To Our Graduation Ceremony")
print("I'm Inviting",convocation[2],"To Our Graduation Ceremony")
print("I'm Inviting",convocation[3],"To Our Graduation Ceremony")
print("I'm Inviting",convocation[4],"To Our Graduation Ceremony")
convocation.insert(0, "Mahadi")
convocation.insert(3, "Sanusi")
convocation.append("Saedu")
print(convocation)
print("I'm Inviting",convocation[0],"To Our Graduation Ceremony")
print("I'm Inviting",convocation[1],"To Our Graduation Ceremony")
print("I'm Inviting",convocation[2],"To Our Graduation Ceremony")
print("I'm Inviting",convocation[3],"To Our Graduation Ceremony")
print("I'm Inviting",convocation[4],"To Our Graduation Ceremony")
print("I'm Inviting",convocation[5],"To Our Graduation Ceremony")
print("I'm Inviting",convocation[6],"To Our Graduation Ceremony")
print("I'm Inviting",convocation[7],"To Our Graduation Ceremony")
print(convocation)
print("Due to the Organazational issue that Affected the Graduation ceremony I'm only Allowed to Invite two People")
convocation.pop(0)
print("Sorry I can't Invite you to Graduation Cremony",convocation.pop(0))
print(convocation)
convocation.pop(1)
print("Sorry I can't Invite you to Graduation Cremony",convocation.pop(1))
print(convocation)
convocation.pop(2)
print("Sorry I can't Invite you to Graduation Cremony",convocation.pop(2))
print(convocation)
print(convocation[0],"You are Invited to Graduation Ceremony")
print(convocation[1],"You are Invited to Graduation Ceremony")
convocation.sort()
print(convocation)
convocation.reverse()
print(convocation)
del convocation[0]
print(convocation)
del convocation[0]
print(convocation)






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


# In[2]:


alien_color = "green"

if alien_color == "green":
    print("Congratulations! You just earned 5 points.")

#### Version Failing the If Test:
# Version Failing the If Test
alien_color = "red"  # You can change this to "yellow" for a different failing scenario

if alien_color == "green":
    print("Congratulations! You just earned 5 points.")


# In[3]:


alien_color = "green"
if alien_color=="green":
    print("congratulation you earned 5 point for shooting the the alien")


# In[4]:


alien_color = "red"
if alien_color=="green":
    print("congratulation you earned 5 point for shooting the the alien")
else:
    print("congratulation you earned 10 point for shooting the the alien")


# In[5]:


alien_color = "green"
if alien_color=="green":
    print("congratulation you earned 5 point for shooting the the alien")
elif alien_color =="yellow":
    print("congratulation you earned 10 point for shooting the the alien")
else:
    print("congratulation you earned 15 point for shooting the the alien")


# In[6]:


alien_color = "yellow"
if alien_color=="green":
    print("congratulation you earned 5 point for shooting the the alien")
elif alien_color =="yellow":
    print("congratulation you earned 10 point for shooting the the alien")
else:
    print("congratulation you earned 15 point for shooting the the alien")


# In[7]:


alien_color = "red"
if alien_color=="green":
    print("congratulation you earned 5 point for shooting the the alien")
elif alien_color =="yellow":
    print("congratulation you earned 10 point for shooting the the alien")
else:
    print("congratulation you earned 15 point for shooting the the alien")


# In[8]:


cubes = []
for num in range(1,11):
    cube = num**3
    cubes.append(cube)
    print(cube)
    

cubes_lc = [i**3 for i in range(1,11)]
print(cubes_lc)


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


# In[1]:


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


# In[ ]:




