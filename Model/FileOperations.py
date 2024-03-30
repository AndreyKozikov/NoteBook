import json
from datetime import datetime
from Model.NoteModel import NoteModel
from Model.Note import Note

class FileOperations:

    __notes = NoteModel()

    def save_notes_to_file(self, filename, notes):
        with open(filename, 'w') as file:
            json.dump([note for note in notes], file, indent=4)

    def load_notes_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                notes_file = json.load(file)
                for note_data in notes_file:
                    note_data['date'] = datetime.strptime(note_data['date'], "%Y-%m-%d %H:%M:%S")
                    self.__notes.record = Note(note_data["id"], note_data["title"], note_data["body"], note_data["date"])
                return self.__notes
        except FileNotFoundError:
            print("Файл с заметками не найден. Файл будет создан вновь.")
            return NoteModel()
        except json.JSONDecodeError:
            print("Ошибка при чтении файла с заметками. Файл будет создан заново.")
            return NoteModel()
