from Model.Operations.CreateNote import CreateNote
from Model.Operations.EditNote import EditNote
from Model.Operations.DeleteNote import DeleteNote
from Model.Operations.ShowMenu import ShowMenu
from Model.Operations.ShowSelectedNote import ShowSelectedNote
from Model.Operations.ShowNoteAtDate import ShowNoteAtDate
from Model.Operations.ExitNotes import ExitNotes
from Model.Operations.ListNote import ListNote

class OperationsList:
    _operation_map = {}

    @staticmethod
    def get_operation(operation):
        return OperationsList.operation_map.get(operation)


OperationsList.operation_map = {
    'ADD': CreateNote(),
    'EDIT': EditNote(),
    'DELETE': DeleteNote(),
    'SHOW': ShowSelectedNote(),
    'DATE': ShowNoteAtDate(),
    'LIST': ListNote(),
    'HELP': ShowMenu(),
    'EXIT': ExitNotes()
}
