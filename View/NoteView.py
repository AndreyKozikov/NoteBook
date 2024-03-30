import sys
import time


class NoteView:
    def show_message(self, message):
        print(message)

    def show_error(self, message):
        sys.stderr.write(message)
        time.sleep(0.3)


    def display_notes(self, notes, id=-1):
        if id == -1:
            for note in notes:
                print(note)
        else:
            print(notes)

    def input_data(self, prompt):
        return input(prompt)
