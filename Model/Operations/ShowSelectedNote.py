import datetime
from Model.ExecuteOperation import ExecuteOperation
from Model.Note import Note


class ShowSelectedNote(ExecuteOperation):
    def execute(self, *args):
        if args[0].getCount == 0:
            args[4](f"Не найдено ни одной заметки. Воспользуйтесь командой ADD.\n")
            return args[0]
        try:
            id = int(args[1]("Введите номер заметки для вывода на экран: "))
        except ValueError:
            args[4](f"Ошибка данных. Номер заметки должен быть целым числом.\n")
            return args[0]

        if (args[0].getCount < id) or (id <= 0):
            args[4](f"Ошибка данных. Номер заметки должен находиться в диапазоне от 1 до {args[0].getCount}.\n")
            return args[0]

        for note in args[0]:
            if note.id == id:
                args[3](note, id)
        return args[0]
