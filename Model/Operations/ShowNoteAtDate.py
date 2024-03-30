from Model.ExecuteOperation import ExecuteOperation
from datetime import datetime

from Model.Note import Note
from Model.NoteModel import NoteModel


class ShowNoteAtDate(ExecuteOperation):

    def execute(self, *args):
        if args[0].getCount == 0:
            args[4](f"Не найдено ни одной заметки. Воспользуйтесь командой ADD.\n")
            return args[0]
        notes_by_date = NoteModel()
        date_str = args[1]("Введите дату в формате дд.мм.гггг для выборки заметок: ")
        try:
            # Преобразуем дату в формат "YYYY-mm-dd"
            target_date = datetime.strptime(date_str, "%d.%m.%Y").date().strftime("%Y-%m-%d")
            for note in args[0]:
                if note.created_at.strftime("%Y-%m-%d") == target_date:
                    notes_by_date.record = Note(*note)
        except ValueError:
            args[4]("Ошибка: Неверный формат даты. Используйте формат dd.mm.YYYY.\n")
            return args[0]
        if notes_by_date != 0:
            args[3](notes_by_date)
        else:
            args[2](f"Нет заметокб созданных или отредактированных {date_str}")
        return args[0]
