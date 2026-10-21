def make_album(artist_name, album_name, track_count=None):
    album_dict = {
            'artist': artist_name.title(), 
            'album': album_name.title()
            }
    if track_count:
        album_dict['track_count'] = track_count
    return album_dict

album = make_album('metallica', 'ride the lightning')
print(album)

album = make_album('beethoven', 'ninth symphony')
print(album)

album = make_album('willie nelson', 'red-headed stranger')
print(album)

album = make_album('iron maiden', 'piece of mind', track_count=8)
print(album)