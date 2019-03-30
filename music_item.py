# encoding=utf8
class MusicItem(object):
    """docstring for MusicItem"""

    def __init__(self, id, name):
        self.name = name
        self.id = id

    def __repr__(self):
        return "id: " + str(self.id) + " name: " + self.name
