from Model.ExecuteOperation import ExecuteOperation



class DeleteNote(ExecuteOperation):

    def execute(self, notes, callback):
        id = int(callback("Введите номер заметки для удаления: "))
        note = notes.values
        for value in note:
            if value.id == id:
                note.remove(value)
        notes.values = note

