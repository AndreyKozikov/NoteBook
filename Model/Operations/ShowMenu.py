from Model.ExecuteOperation import ExecuteOperation
from Model.FileOperations import FileOperations


class ShowMenu(ExecuteOperation):

    def execute(self, notes, callback):
        fo = FileOperations()
        serializable_notes = [
            {"id": note.id, "title": note.title, "body": note.body, "date": note.created_at.strftime("%Y-%m-%d "
                                                                                                         "%H:%M:%S")}
            for
            note in notes.values]
        fo.save_notes_to_file("notes.json", serializable_notes)