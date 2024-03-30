from Model.Operation import OperationsList
from Model.NoteModel import NoteModel
from Model.FileOperations import FileOperations


class NotePresenter():

    def __init__(self, view):
        self.view = view
        self.notes = NoteModel()
        self.fo = FileOperations()

    def user_input_callback(self, prompt):
        return self.view.input_data(prompt)

    def __get_command(self):
        while True:
            command = self.view.input_data("Введите команду: ").upper()
            operation = OperationsList.get_operation(command)
            if operation is not None:
                break
            else:
                self.view.show_message(
                    "В данный момент команда " + command + " не поддерживается. Используйте help для списка команд.")
        return operation

    def run(self):
        self.view.show_message(
            "Добро пожаловать в приложение Заметки.\nИспользуйте команду help для отображения команд.")
        self.notes = self.fo.load_notes_from_file("notes.json")
        operation = self.__get_command()
        while True:
            self.notes = operation.execute(self.notes, self.user_input_callback, self.view.show_message,
                                           self.view.display_notes, self.view.show_error)
            operation = self.__get_command()
