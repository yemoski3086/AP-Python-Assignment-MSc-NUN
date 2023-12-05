#4b
magicians = ['Sheriff Kiri', 'Abdu', 'ibrahim'] # Create a list of magician's names

def show_magicians(magicians):
    # The function should take a list of magicians as an argument
    for magician in magicians: # Loop through the list of magicians
        print(magician) # Print the name of each magician

show_magicians(magicians) # Call the function with the list of magicians
# Write a function called make_great() that modifies the list of magicians by adding the phrase the Great to each magician’s name
def make_great(magicians):
    # The function should take a list of magicians as an argument
    great_magicians = [] # Create an empty list to store the modified names
    while magicians: # Loop while the list of magicians is not empty
        magician = magicians.pop() # Pop a magician from the list
        great_magician = magician + ' the Great' # Add the phrase the Great to the magician's name
        great_magicians.append(great_magician) # Append the modified name to the new list
    for great_magician in great_magicians: # Loop through the new list of magicians
        magicians.append(great_magician) # Append the modified name back to the original list
    return magicians # Return the modified list

# Call the function make_great() with the list of magicians
make_great(magicians) # Call the function with the list of magicians

# Call show_magicians() to see that the list has actually been modified
show_magicians(magicians) # Call the function with the modified list of magicians

# Call the function make_great() with a copy of the list of magicians’ names
great_magicians = make_great(magicians[:]) # Call the function with a copy of the list of magicians and store the result in a separate list

# Call show_magicians() with each list to show that you have one list of the original names and one list with the Great added to each magician’s name
show_magicians(magicians) # Call the function with the original list of magicians
show_magicians(great_magicians) # Call the function with the new list of magicians# Write a function called make_album() that builds a dictionary describing a music album





#4a
def make_album(artist, title, tracks=None):
    # The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information
    album = {'artist': artist, 'title': title}
    # If the calling line includes a value for the number of tracks, add that value to the album's dictionary
    if tracks: # If the tracks parameter is not None
        album['tracks'] = tracks # Add the tracks key and value to the dictionary
    return album # Return the dictionary
album_1 = make_album('Taylor Swift', 'Red') # Make a dictionary for the album 'Red' by Taylor Swift
album_2 = make_album('Ed Sheeran', 'Divide') # Make a dictionary for the album 'Divide' by Ed Sheeran
album_3 = make_album('Adele', '25') # Make a dictionary for the album '25' by Adele

print(album_1,"\n",album_2,"\n",album_3)
while True: # Loop indefinitely
    print("\nEnter the artist and title of an album, or 'quit' to exit.") # Print a prompt for the user
    artist = input("Artist: ") # Ask the user for the artist name
    if artist == 'quit': # If the user enters 'quit'
        break # Break out of the loop
    title = input("Title: ") # Ask the user for the album title
    if title == 'quit': # If the user enters 'quit'
        break # Break out of the loop
    # Ask the user for the number of tracks on the album
    tracks = input("Number of tracks (optional): ") # Ask the user for the number of tracks
    if tracks == 'quit': # If the user enters 'quit'
        break # Break out of the loop
    elif tracks == '': # If the user enters nothing
        tracks = None # Set the tracks parameter to None
    else: # If the user enters a number
        tracks = int(tracks) # Convert the tracks parameter to an integer
    # Once you have that information, call make_album() with the user’s input
    album = make_album(artist, title, tracks) # Call the function with the user's input
    # Print the dictionary that’s created
    print(album) # Print the dictionary for the albumd

