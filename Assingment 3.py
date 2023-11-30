# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 10:00:59 2023

@author: Admin
"""

def make_album(artist, title, tracks=None):
    album = {"artist": artist, "title": title}
    if tracks:
        album["tracks"] = tracks
    return album

# Step 1: Create three dictionaries representing different albums
album1 = make_album("Artist1", "Album1", 10)
album2 = make_album("Artist2", "Album2")
album3 = make_album("Artist3", "Album3", 15)

# Step 2: Print each return value to show the dictionaries are storing the information correctly
print(album1)
print(album2)
print(album3)

# Step 3: Use a while loop to allow users to enter album artist and title
while True:
    artist_input = input("Enter the album artist (or type 'quit' to exit): ")
    if artist_input.lower() == 'quit':
        break
    title_input = input("Enter the album title: ")
    tracks_input = input("Enter the number of tracks (press Enter if unknown): ")
    
    # Call make_album() with user input and print the created dictionary
    user_album = make_album(artist_input, title_input, int(tracks_input) if tracks_input.isdigit() else None)
    print(user_album)

