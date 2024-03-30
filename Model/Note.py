import datetime

class Note:
    def __init__(self, id, title, body, created_at=None):
        self.id = id
        self.title = title
        self.body = body
        self.created_at = created_at or datetime.datetime.now()

    def __repr__(self):
        return f"Note(Номер заметки: {self.id}, Заголовок: '{self.title}', Заметка: '{self.body}', Время создания/изменения: {self.created_at})"
