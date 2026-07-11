# code for problem 8.8:
# copied code from 8.7:
def make_album(artist_name, music_album):
    info = {'artist': artist_name,
            'album': music_album
            }
    return info

promt = "Write down artists name and music albums name \n(if you want to quit press q)"
while True:
    print(promt)
    artist = input("Enter artist: ")
    if artist.title() == 'Q':
        break  # we can also use flag to break the while loop instead of break
    album = input("Enter album: ")
    if album.title() == 'Q':
        break  # we can also use flag to break the while loop instead of break

    album = make_album(artist, album)
    print(album)
