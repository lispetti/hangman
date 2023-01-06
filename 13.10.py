"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
StudentId: 151254255
Name:      Liisa Piirainen
Email:     liisa.i.piirainen@tuni.fi

...
"""

from tkinter import *
from tkinter import messagebox
from Graphics import *
import time


class UserInterface:

    def __init__(self):

        self.__MainWindow = Tk()
        self.__slipknot = SlipknotGraphics(self.__MainWindow)
        self.__MainWindow.title("Hangman")
        self.__word = []
        self.__finished_word = []
        self.__stop_button = Button(self.__MainWindow, text="reset", command=self.stop, fg="#ffb3fe")
        self.__stop_button.grid(row=4, columnspan=2, column=0)
        self.__done_button = Button(self.__MainWindow, text="done", command=self.done_writing_word_command, fg="#ffb3fe")
        self.__done_button.grid(row=4, column=9, columnspan=2)
        self.__backspace_button = Button(self.__MainWindow, text="⌫", command=self.backspace_command, fg="#ffb3fe")
        self.__backspace_button.grid(row=0, column=10)

        keyboard_1st_row = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "å"]
        keyboard_2nd_row = ["a", "s", "d", "f", "g", "h", "j", "k", "l", "ö", "ä"]
        keyboard_3rd_row = ["z", "x", "c", "v", "b", "n", "m"]
        keyboard_rows = [keyboard_1st_row, keyboard_2nd_row, keyboard_3rd_row]

        row_counter = 1
        self.__buttons = {}
        for row in keyboard_rows:
            if row_counter == 3:
                column_counter = 2
            else:
                column_counter = 0
            row_counter += 1

            for key in row:
                button = Button(self.__MainWindow, text=key,
                                         command=lambda pressed=key: self.keyboard_command(pressed),
                                         width=3, height=3, fg="#ffb3fe", activeforeground="red")
                button.grid(row=row_counter, column=column_counter)
                column_counter += 1
                self.__buttons[key] = button

    def keyboard_command(self, key):
        is_guessing_phase = "_ " in self.__word
        if is_guessing_phase:
            self.handle_guess(key)
        else:
            self.__word.append(key)
            self.set_label()

    def handle_guess(self, key):
        found = False
        for i in range(0, len(self.__word)):
            self.__buttons[key]["state"] = DISABLED
            if self.__finished_word[i] == key:
                self.__word[i] = key
                guess = "".join(self.__word)
                finished_word = "".join(self.__finished_word)
                found = True
                if guess == finished_word:
                    messagebox.showwarning("Information", f"Congratulations \n You Win! \n word: {''.join(self.__finished_word)}")
                    self.stop()

        self.set_label()

        if not found:
            is_finished = self.__slipknot.draw_next()
            if is_finished:
                time.sleep(0.5)
                messagebox.showwarning("Information", f"Congratulations \n You Lost! \n The word was: {''.join(self.__finished_word)}")
                self.stop()

    def set_label(self):
        self.__text_window = Label(self.__MainWindow, text="".join(self.__word), fg="#ffb3fe")
        self.__text_window.grid(row=0, column=0, columnspan=10)

    def done_writing_word_command(self):
        self.__finished_word = self.__word.copy()
        for i in range(0, len(self.__word)):
            self.__word[i] = "_ "
        self.__backspace_button["state"] = DISABLED
        self.__done_button["state"] = DISABLED
        self.set_label()

    def backspace_command(self):
        if len(self.__word) > 1:
            self.__word.pop(-1)
            self.set_label()
        else:
            self.__word = self.__word.clear()
            self.__text_window = Label(self.__MainWindow, text=self.__word, fg="#ffb3fe")
            self.__text_window.grid(row=0, columnspan=30)
            self.__word = []

    def start(self):
        """
        Starts the mainloop.
        """
        self.__MainWindow.mainloop()

    def stop(self):
        """
        Ends the execution of the program.
        """
        self.__MainWindow.destroy()
        ui = UserInterface()
        ui.start()


def main():

    ui = UserInterface()
    ui.start()


if __name__ == "__main__":
    main()
