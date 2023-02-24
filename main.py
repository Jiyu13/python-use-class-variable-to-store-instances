class Song:

    # create a class attribute to keep track of all created songs /instance
    all = []

    def __init__(self, name):
        self.name = name

        # the class attr "all" is handled by instance method -- __init__()
        # # but it's better it's handled by class methods
        # Song.all.append(self)

        # call the class method when initialise a new instance, pass in the object "self" as arg
        Song.add_song_to_all(self)

    # create a class method to add new instance to "all" class attribute
    @classmethod
    def add_song_to_all(cls, song):
        cls.all.append(song)

    # create a class method that show all the names in all
    @classmethod
    def show_song_names(cls):
        print([song.name for song in cls.all])


# create new songs / instances
big_energy = Song("Big Energy")
out_of_touch = Song("Out of Touch")

print(Song.all)
# [<__main__.Song object at 0x0000019C33DAAFA0>, <__main__.Song object at 0x0000019C33DAAEE0>]

Song.show_song_names()
# ['Big Energy', 'Out of Touch']
