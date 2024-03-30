import datetime
from Model.ExecuteOperation import ExecuteOperation
from Model.Note import Note


class EditNote(ExecuteOperation):
    def execute(self, notes, callback):
        id = int(callback("Введите номер заметки для редактирования: "))
        values = notes.values
        for note in values:
            if note.id == id:
                print(note)
                title = callback("Введите новый заголовок заметки: ")
                body = callback("Введите новый текст заметки: ")
                created_at = datetime.datetime.now()
                values.remove(note)
                note = Note(id, title, body, created_at)
                values.insert(id - 1, note)
        notes.values = values
