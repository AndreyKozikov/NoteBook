import datetime
from Model.Note import Note


class NoteModel:
    def __init__(self):
        self.__record = []
        self.__id_count = 0

    @property
    def getCount(self):
        return self.__id_count
    @property
    def record(self):
        return self.__record

    @record.setter
    def record(self, values):
        self.__record.append(values)
        self.__id_count += 1

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self.record):
            note_data = self.record[self._index]
            self._index += 1
            note = Note(*note_data)
            return note
        else:
            raise StopIteration
