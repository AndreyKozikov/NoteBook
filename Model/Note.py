import datetime

class Note:
    def __init__(self, note_id, title, body, created_at=None, updated_at=None):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.created_at = created_at or datetime.datetime.now()
        self.updated_at = updated_at or datetime.datetime.now()

    def __repr__(self):
        return f"Note(id={self.note_id}, title='{self.title}', created_at={self.created_at}, updated_at={self.updated_at})"
