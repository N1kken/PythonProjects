class Song(object):
    def __init__(self, lyrics):
        print(lyrics)
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print (line)

happy_bday = Song(["Sto lat sto lat", "sto lat sto lat", "no starczy"])
inna = Song(["balbllablba", "saofkoasfkof", "safoksfkoaf"])

happy_bday.sing_me_a_song()
#inna.sing_me_a_song()

