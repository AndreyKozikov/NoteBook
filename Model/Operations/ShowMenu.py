from Model.ExecuteOperation import ExecuteOperation


class ShowMenu(ExecuteOperation):

    def execute(self, *args):
        args[2]("Поддерживаются следующие команды:\n"
                "ADD: Добавить заметку\n"
                "EDIT: Редактировать заметку по номеру\n"
                "DELETE: Удалить заметку по номеру\n"
                "SHOW: Показать заметку по номеру\n"
                "DATE: Показать все заметки с указанной датой\n"
                "LIST: Показать все заметки\n"
                "HELP: Показать поддерживаемые команды\n"
                "EXIT: Завершение работы\n")
