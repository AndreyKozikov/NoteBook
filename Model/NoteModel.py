import datetime
from Model.Note import Note

class NoteModel:
    def __init__(self):
        self.notes = []

    def create_note(self, title, body):
        note_id = len(self.notes) + 1
        note = Note(note_id, title, body)
        self.notes.append(note)
        return note

    def edit_note(self, note_id, new_title, new_body):
        for note in self.notes:
            if note.note_id == note_id:
                note.title = new_title
                note.body = new_body
                note.updated_at = datetime.datetime.now()
                return True
        return False

    def delete_note(self, note_id):
        for note in self.notes:
            if note.note_id == note_id:
                self.notes.remove(note)
                return True
        return False

    def get_notes(self):
        return self.notes
