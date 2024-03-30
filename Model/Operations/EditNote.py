import datetime
from Model.ExecuteOperation import ExecuteOperation
from Model.Note import Note
from Model.NoteModel import NoteModel


class EditNote(ExecuteOperation):
    def execute(self, *args):
        if args[0].getCount == 0:
            args[4](f"Не найдено ни одной заметки. Воспользуйтесь командой ADD.\n")
            return args[0]
        try:
            id = int(args[1]("Введите номер заметки для редактирования: "))
        except ValueError:
            args[4](f"Ошибка данных. Номер заметки должен быть целым числом.\n")
            return args[0]
        if (args[0].getCount < id) or (id <=0):
            args[4](f"Ошибка данных. Номер заметки должен находиться в диапазоне от 1 до {args[0].getCount}.\n")
            return args[0]
        args[2]("При вводе в поле пустого значения будет сохранено его предыдущее содержание.")
        notes_insert = NoteModel()
        for note in args[0]:
            if note.id == id:
                title = args[1]("Введите новый заголовок заметки: ")
                if title == "":
                    title = note.title
                body = args[1]("Введите новый текст заметки: ")
                if title == "":
                    body = note.body
                created_at = datetime.datetime.now().replace(microsecond=0)
                notes_insert.record = Note(id, title, body, created_at)
            else:
                notes_insert.record = Note(*note)
        return notes_insert
