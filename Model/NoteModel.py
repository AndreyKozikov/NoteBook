import datetime
from Model.Note import Note


class NoteModel:
    def __init__(self):
        self.__values = []

    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, values):
        self.__values = values
