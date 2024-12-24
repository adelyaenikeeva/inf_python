# 1. Музыкальный плейлист:
#    Создайте класс Song, который будет представлять отдельную песню со следующими атрибутами:
# __name — название песни;
# __artist — исполнитель песни;
# __duration — продолжительность песни в минутах.
# Затем создайте класс Playlist, который будет инкапсулировать список песен, состоящий из объектов класса Song.
# В классе Playlist необходимо реализовать следующие методы:
#    - Напишите методы для добавления, удаления песен и получения информации о всей очереди.
#    - Реализуйте метод для подсчета общей продолжительности плейлиста.



class Song:
    def __init__(self, name, artist, duration):
        self.__name = name
        self.__artist = artist
        self.__duration = duration

    @property
    def name(self):
        return self.__name

    @property
    def artist(self):
        return self.__artist

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration):
        if duration > 0:
            self.__duration = duration
        else:
            print('Недопустимое значение')

    def __str__(self):
        return f"{self.__name} - {self.__artist} ({self.__duration})"


class Playlist:
    def __init__(self):
        self.__songs = []

    def add_song(self, song):
        if isinstance(song, Song):
            self.__songs.append(song)
            print(f'Добавлена песня: {song}')

    def remove_song(self, song_name):
        for song in self.__songs:
            if song.name == song_name:
                self.__songs.remove(song)
                print(f'Удалена песня: {song}')

    def show_playlist(self):
        if self.__songs:
            print('Список песен в плейлисте:')
            for song in self.__songs:
                print(song)
        else:
            print('Плейлист пуст')

    def total_duration(self):
        total = sum(song.duration for song in self.__songs)
        return total


if __name__ == '__main__':
    playlist = Playlist()

    song1 = Song('Yesterday', 'The Beatles', 2.05)
    song2 = Song('Imagine', 'John Lennon', 3.03)

    # song1.duration = -2.00

    playlist.add_song(song1)
    playlist.add_song(song2)

    playlist.show_playlist()

    print(f'Общая продолжительность плейлиста: {playlist.total_duration()}')

    playlist.remove_song('Imagine')
    playlist.show_playlist()

    print(f'Общая продолжительность плейлиста после удаления песни: {playlist.total_duration()}')