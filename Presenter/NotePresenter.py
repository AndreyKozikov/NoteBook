class NotePresenter:
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def create_note(self, title, body):
        note = self.model.create_note(title, body)
        self.view.show_message(f"Заметка '{note.title}' успешно создана.")

    def edit_note(self, note_id, new_title, new_body):
        if self.model.edit_note(note_id, new_title, new_body):
            self.view.show_message("Заметка успешно отредактирована.")
        else:
            self.view.show_error("Заметка не найдена.")

    def delete_note(self, note_id):
        if self.model.delete_note(note_id):
            self.view.show_message("Заметка успешно удалена.")
        else:
            self.view.show_error("Заметка не найдена.")

    def load_notes(self):
        notes = self.model.get_notes()
        self.view.display_notes(notes)
