def make_album(artist, title):
    album = {'artist': artist,'title': title,}
    return album
album1 = make_album('jcole' , 'sinner')
album2 = make_album('eminem' , 'encore')
album3 = make_album('drake', 'hyfr')
print (album1)
print (album2)
print (album3)
def make_album(artist, title, tracks=None):   
    album = {'artist': artist, 'title': title}
    if tracks: 
        album['tracks'] = tracks 
    return album
album4 = make_album('davido' , 'timeless', 10 )
print (album4)

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
    print(album) # Print the dictionary for the album

magicians = ['amina','barakat', 'aisha']
def show_magicians(magicians):
    for x in magicians:
        print(magicians)
show_magicians(magicians)
def make_great(magicians):
    # The function should take a list of magicians as an argument
    great_magicians = [] # Create an empty list to store the modified names
    while magicians: # Loop while the list of magicians is not empty
        magician = magicians.pop() # Pop a magician from the list
        great_magician = magician + ' the Great' # Add the phrase the Great to the magician's name
        great_magicians.append(great_magician) # Append the modified name to the new list
    for great_magician in great_magicians: # Loop through the new list of magicians
        magicians.append(great_magician) # Append the modified name back to the original list
    return magicians 
    make_great(magicians) 
    print(magicians)
    show_magicians(magicians)
    great_magicians = make_great(magicians[:])
