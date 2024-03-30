import datetime

class Note:
    def __init__(self, id, title, body, created_at=None):
        self.id = id
        self.title = title
        self.body = body
        self.created_at = created_at or datetime.datetime.now().replace(microsecond=0)

    def __repr__(self):
        return f"Номер заметки: {self.id}, Заголовок: '{self.title}', Заметка: '{self.body}', Время создания/изменения: {self.created_at}"

    def __iter__(self):
        yield self.id
        yield self.title
        yield self.body
        yield self.created_at