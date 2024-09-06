# Система управління музичною колекцією:
# Створіть клас "Пісня" з атрибутами: назва, виконавець, альбом, рік випуску, жанр, тривалість. Розробіть клас "Плейлист", який містить список пісень та має назву. Потім створіть клас "МузичнаБібліотека", який використовує словник для зберігання всіх пісень (ключ - унікальний ідентифікатор пісні) та список для зберігання плейлистів.
class Song:
    def __init__(self, title, artist, album, year, genre, duration):
        self.title = title
        self.artist = artist
        self.album = album
        self.year = year
        self.genre = genre
        self.duration = duration

    def __str__(self):
        return f"{self.title} від {self.artist} з альбому {self.album} ({self.year}) - {self.genre}, {self.duration} хвилин"

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        self.songs.remove(song)

    def __str__(self):
        return f"Плейлист: {self.name}, Пісні: {[str(song) for song in self.songs]}"

class MusicLibrary:
    def __init__(self):
        self.songs = {}
        self.playlists = []

    def add_song(self, song_id, song):
        self.songs[song_id] = song

    def remove_song(self, song_id):
        if song_id in self.songs:
            del self.songs[song_id]

    def create_playlist(self, name):
        playlist = Playlist(name)
        self.playlists.append(playlist)
        return playlist

    def __str__(self):
        return f"Музична бібліотека: Пісні: {list(self.songs.keys())}, Плейлисти: {[playlist.name for playlist in self.playlists]}"

song1 = Song("Назва1", "Автор1", "Альбом1", 1999, "phonk", 3.0)
song2 = Song("Назва2", "Автор2", "Альбом2", 1998, "phonk", 5.5)

library = MusicLibrary()
library.add_song(1, song1)
library.add_song(2, song2)

playlist = library.create_playlist("Улюблені")
playlist.add_song(song1)
playlist.add_song(song2)

print(library)
print(playlist)
