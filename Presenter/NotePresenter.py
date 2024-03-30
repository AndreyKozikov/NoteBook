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
                print("В данный момент команда ", command, " не поддерживается. Используйте help для списка команд.")
        return operation

    def run(self):
        print("Добро пожаловать в приложение Заметки. Для вызова списка команд используйте help.")
        self.notes.values = self.fo.load_notes_from_file("notes.json")
        command = None
        while command != 'EXIT':
            operation = self.__get_command()
            if operation == 'LIST':
                self.view.display_notes(self.notes.values)
            elif operation == "HELP":
                self.view.show_message("Поддерживаются следующие команды:\n"
                                       "ADD: Добавить заметку\n"
                                        "EDIT: Редактировать заметку по номеру\n"
                                        "DELETE: Удалить заметку по номеру\n"
                                        "SHOW: Показать заметку по номеру\n"
                                        "DATE: Показать все заметки с указанной датой\n"
                                        "LIST: Показать все заметки\n"
                                        "HELP: Показать поддерживаемые команды\n"
                                        "EXIT': Завершение работы\n")

            else:
                operation.execute(self.notes, self.user_input_callback)
                print("Для вызова списка команд используйте help.")
