def make_album(artist_name, album_title):
    album_dict = {
        'artist': artist_name.title(),
        'album': album_title.title(),
    }
    return album_dict

while True:
    print("\n(enter 'q' at any time to quit)")
    artist = input('Enter your artist name: ')
    if artist == 'q':
        break
    title = input('\nEnter your album name: ')
    if title == 'q':
        break

    album = make_album(artist, title)
    print(album)