from Model.ExecuteOperation import ExecuteOperation


class ListNote(ExecuteOperation):
    def execute(self, *args):
        if args[0].getCount == 0:
            args[4](f"Не найдено ни одной заметки. Воспользуйтесь командой ADD.\n")
            return args[0]
        args[3](args[0])
        return args[0]
