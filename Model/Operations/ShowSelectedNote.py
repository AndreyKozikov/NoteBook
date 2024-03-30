import datetime
from Model.ExecuteOperation import ExecuteOperation
from Model.Note import Note


class ShowSelectedNote(ExecuteOperation):
    def execute(self, notes, callback):
        id = int(callback("Введите номер заметки для вывода на экран: "))
        values = notes.values
        for note in values:
            if note.id == id:
                print(note) #Перенести в презентер
