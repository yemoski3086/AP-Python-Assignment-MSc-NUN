def make_album(artist_name, album_title, number_of_tracks = None):
    album = {'artist_name': artist_name, 'album_title': album_title}
    if number_of_tracks is not None:
        album['number_of_tracks'] = number_of_tracks
    
    return album

print(make_album('Olamide', 'Woske'))
print(make_album('Wizkid', 'Lagos'))
print(make_album('Akon', 'Cvs', 2))



while True:
    # Ask for artist name
    artist = input("Enter the artist name (or 'q' to quit): ")

    # Check if the user wants to quit
    if artist.lower() == 'q':
        break  # Exit the loop if 'q' is entered

    # Ask for album title
    album = input("Enter the album title (or 'q' to quit): ")
    
    # Check if the user wants to quit
    if album.lower() == 'q':
        break  # Exit the loop if 'q' is entered

    print(make_album(artist, album))

