from Model.ExecuteOperation import ExecuteOperation
from datetime import datetime


class ShowNoteAtDate(ExecuteOperation):
    __notes = []

    def execute(self, notes, callback):
        notes_by_date = []
        self.__notes = notes.values
        date_str = callback("Введите дату в формате дд.мм.гггг для выборки заметок:")
        try:
            # Преобразуем дату в формат "YYYY-mm-dd"
            target_date = datetime.strptime(date_str, "%d.%m.%Y").date().strftime("%Y-%m-%d")
            for note in self.__notes:
                if note.created_at.strftime("%Y-%m-%d") == target_date:
                    notes_by_date.append(note)
        except ValueError:
            print("Ошибка: Неверный формат даты. Используйте формат dd.mm.YYYY.")
        print(notes_by_date)  # Перенести в презентер
