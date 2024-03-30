
from Presenter.NotePresenter import NotePresenter
from View.NoteView import NoteView

if __name__ == "__main__":

    presenter = NotePresenter(NoteView())
    presenter.run()