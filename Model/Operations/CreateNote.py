from Model.ExecuteOperation import ExecuteOperation
from Model.Note import Note



class CreateNote(ExecuteOperation):
    def execute(self, notes, callback):
        title = callback("Введите заголовок заметки: ")
        body = callback("Введите текст заметки: ")
        notes = notes.values
        note_id = len(notes) + 1
        note = Note(note_id, title, body)
        notes.append(note)

