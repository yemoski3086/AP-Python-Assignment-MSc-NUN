# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 09:47:38 2023

@author: Admin
"""

# Step 1: Create a list of people to invite to graduation
guest_list = ["Umar Yahaya", "Shehu Tilli", "Nuhu Aliyu"]

# Step 2: Print invitation messages for each person
for person in guest_list:
    print(f"Dear {person},\n\tYou are invited to my graduation. Please join us on that special day!\n")

# Step 3: One guest can't make it, print their name
guest_cant_make_it = "Umar Yahaya"
print(f"Unfortunately, {guest_cant_make_it} can't make it to the graduation.\n")

# Step 4: Replace the name of the guest who can't make it with a new person
new_guest = "Ibrahim Zannah"
guest_list[guest_list.index(guest_cant_make_it)] = new_guest

# Step 5: Print a second set of invitation messages
for person in guest_list:
    print(f"Dear {person},\n\tYou are invited to my graduation. Please join us on that special day!\n")

# Step 6: Allow more guests, think of three more people to invite
print("Good news! More space is available, so additional guests are invited.\n")
additional_guests = ["Najeeb Ahmad", "Blus Tarwada", "Kashema Bahago"]
guest_list.extend(additional_guests)

# Step 7: Use insert() to add new guests to the list
guest_list.insert(0, "Maryam Umar")   # Add to the beginning
guest_list.insert(len(guest_list)//2, "Ibrahim Umar")   # Add to the middle
guest_list.append("Stephen John")   # Add to the end

# Step 8: Print new invitation messages
for person in guest_list:
    print(f"Dear {person},\n\tYou are invited to my graduation. Please join us on that special day!\n")

# Step 9: Organizational issues, can only invite two people
print("Due to organizational issues, I can only invite two people to the graduation.\n")

# Step 10: Use pop() to remove guests until only two names remain
while len(guest_list) > 2:
    removed_person = guest_list.pop()
    print(f"Sorry, {removed_person}, I can't invite you to the graduation.")

# Step 11: Print a message to the two remaining people
for person in guest_list:
    print(f"Dear {person},\n\tYou are still invited to my graduation. Please join us on that special day!\n")

# Step 12: Sort the remaining guest list alphabetically
guest_list.sort()
print("Guest list in alphabetical order:")
print(guest_list)

# Step 13: Reverse the order of the guest list
guest_list.reverse()
print("Guest list in reverse order:")
print(guest_list)

# Step 14: Use del to remove the last two names, making an empty list
del guest_list[-2:]
print("Guest list after removing the last two names:", guest_list)