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
    """
    This class represents the user interface that allows you to play hangman.
    Consists of writing word phase: player 1 writes the word to be guessed
    and guessing phase: player 2 tries to guess player 1's word
    """

    def __init__(self):
        """
        introduces needed variables to use every button
        in the game and needed lists to store word information
        during the game and creates the keyboard
        """

        self.__MainWindow = Tk()
        self.__slipknot_graphic = SlipknotGraphics(self.__MainWindow)
        self.__MainWindow.title("Hangman")
        self.__reset_button = Button(self.__MainWindow, text="reset", command=self.stop, fg="#ffb3fe")
        self.__reset_button.grid(row=4, columnspan=2, column=0)
        self.__done_button = Button(self.__MainWindow, text="done", command=self.done_command, fg="#ffb3fe")
        self.__done_button.grid(row=4, column=9, columnspan=2)
        self.__backspace_button = Button(self.__MainWindow, text="⌫", command=self.backspace_command, fg="#ffb3fe")
        self.__backspace_button.grid(row=0, column=10)
        self.__text_window = Label(self.__MainWindow)
        self.__word = []
        self.__finished_word = []

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
        """
        handles the different phases of the game. Starts by checking if the game is in
        the guessing phase or the writing word phase by checking self.__word contents.
        If in writing word phase adds each character to a list containing
        word to be guessed (self.__word).
        If in guessing phase goes to handle_guess method.
        :param key: key in dict, represents the character of
        the recently pressed button
        """
        is_guessing_phase = " _" in self.__word
        if is_guessing_phase:
            self.handle_guess(key)
        else:
            self.__word.append(key)
            self.set_label()

    def handle_guess(self, key):
        """
        Disables pressed button. Then checks if guessed character is in word. if yes, replaces "_ " in self.__word
        with guessed character. If the whole word has been guessed, shows a win window and goes to stop method.
        if, no shows that you missed by calling on the graphic file's draw_next method.
        If draw_next method returns is_finished = True, shows lose window. Lose window doesn't start
        a new game so players can see the finished picture :)
        :param key: key in dict, represents the character of
        the recently pressed button
        :return: returns if game ends.
        """
        found = False
        for i in range(0, len(self.__word)):
            self.__buttons[key]["state"] = DISABLED
            if self.__finished_word[i] == key:
                self.__word[i] = key
                guess = "".join(self.__word)
                finished_word = "".join(self.__finished_word)
                found = True
                if guess == finished_word:
                    messagebox.showwarning("Information", f"Congratulations \n You Win! \n word: "
                                                          f"{''.join(self.__finished_word)}")
                    self.stop()
                    return

        self.set_label()

        if not found:
            is_finished = self.__slipknot_graphic.draw_next()
            if is_finished:
                time.sleep(0.5)
                messagebox.showwarning("Information", f"Congratulations \n You Lost! "
                                                      f"\n The word was: {''.join(self.__finished_word)}")

    def set_label(self):
        """
        First clears and then sets the label showed above the keyboard by showing self.__word.
        """
        self.__text_window.configure(text="")
        self.__text_window = Label(self.__MainWindow, text="".join(self.__word), fg="#ffb3fe")
        self.__text_window.grid(row=0, column=0, columnspan=10)

    def done_command(self):
        """
        changes the game to guessing phase. copies self.__word containing player 1's word to
        self.__finished_Word then changes every item in self.__word to "_ ". Disables backspace
        and done buttons
        """
        self.__finished_word = self.__word.copy()
        for i in range(0, len(self.__word)):
            self.__word[i] = " _"
        self.__backspace_button["state"] = DISABLED
        self.__done_button["state"] = DISABLED
        self.set_label()

    def backspace_command(self):
        """
        removes the most recent character on label above keyboard and
        self.__word during writing word phase. if only one letter,
        clears the label and self.__word.
        """
        if len(self.__word) > 1:
            self.__word.pop(-1)
            self.set_label()
        else:
            self.__word = self.__word.clear()
            self.__word = []
            self.__word.append("")
            self.set_label()
            self.__word = []

    def start(self):
        """
        Starts the mainloop.
        """
        self.__MainWindow.mainloop()

    def stop(self):
        """
        Ends the execution of the program and starts a new game
        by starting the execution of the program again.
        """
        self.__MainWindow.destroy()
        ui = UserInterface()
        ui.start()


def main():
    """
    starts the execution of the program
    """
    ui = UserInterface()
    ui.start()


if __name__ == "__main__":
    main()

