class NoteView:
    def show_message(self, message):
        print(message)

    def show_error(self, message):
        print(f"Ошибка: {message}")

    def display_notes(self, notes):
        for note in notes:
            print(note)
