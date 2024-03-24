from Model.NoteModel import NoteModel
from Presenter.NotePresenter import NotePresenter
from View.NoteView import NoteView

if __name__ == "__main__":
    model = NoteModel()
    presenter = NotePresenter(NoteView(), model)

    presenter.create_note("Заголовок 1", "Текст заметки 1")
    presenter.create_note("Заголовок 2", "Текст заметки 2")

    presenter.edit_note(1, "Новый заголовок 1", "Новый текст заметки 1")
    presenter.delete_note(2)

    presenter.load_notes()