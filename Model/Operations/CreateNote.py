from Model.ExecuteOperation import ExecuteOperation
from Model.Note import Note
from Model.NoteModel import NoteModel


class CreateNote(ExecuteOperation):
    def execute(self, *args):
        args[2]("Создаем новую заметку. Вводимые поля не должны быть пустыми.")
        title = args[1]("Введите заголовок заметки: ")
        body = args[1]("Введите текст заметки: ")
        if (title == "") or (body == ""):
            args[4]("Ошибка данных. Вы ввели пустые поля.\n")
            return args[0]
        note_id = args[0].getCount + 1
        notes_create = args[0]
        notes_create.record = Note(note_id, title, body)
        return notes_create
