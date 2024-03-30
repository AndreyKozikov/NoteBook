from Model.ExecuteOperation import ExecuteOperation
from Model.FileOperations import FileOperations


class ExitNotes(ExecuteOperation):

    def execute(self, *args):
        fo = FileOperations()
        serializable_notes = [
            {"id": note.id, "title": note.title, "body": note.body, "date": note.created_at.strftime("%Y-%m-%d "
                                                                                                         "%H:%M:%S")}
            for
            note in args[0]]
        fo.save_notes_to_file("notes.json", serializable_notes)
        args[2]("Программа завершена. Данные сохранены. Хорошего дня.")
        exit(0)
