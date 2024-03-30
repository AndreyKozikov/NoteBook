from Model.ExecuteOperation import ExecuteOperation
from Model.Note import Note
from Model.NoteModel import NoteModel


class DeleteNote(ExecuteOperation):

    def execute(self, *args):
        if args[0].getCount == 0:
            args[4](f"Не найдено ни одной заметки. Воспользуйтесь командой ADD.\n")
            return args[0]
        try:
            id = int(args[1]("Введите номер заметки для удаления: "))
        except ValueError:
            args[4](f"Ошибка данных. Номер заметки должен быть целым числом.\n")
            return args[0]
        if (args[0].getCount < id) or (id <=0):
            args[4](f"Ошибка данных. Номер заметки должен находиться в диапазоне от 1 до {args[0].getCount}.\n")
            return args[0]
        notes_to_keep = NoteModel()
        new_id = 1
        for value in args[0]:
            if value.id != id:
                notes_to_keep.record = Note(new_id, value.title, value.body, value.created_at)
                new_id += 1
        return notes_to_keep
