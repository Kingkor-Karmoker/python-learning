# code for problem 8.7:
def make_album(artist_name, music_album, no_songs_in_album= None):
    info = {'artist': artist_name,
            'album': music_album
            }
    if no_songs_in_album is not None:
        info['no_songs_in_album'] = no_songs_in_album
    return info

album= make_album('Balam', 'Ki Nesha')
print(album)
album= make_album('Imagine Dragons', 'Believer')
print(album)
album= make_album('Michael Jackson', 'Beat It')
print(album)

album= make_album('Eminem', 'Rap god', 10)
print(album)
