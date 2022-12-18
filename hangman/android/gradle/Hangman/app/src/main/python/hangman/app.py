"""
Hangman game
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, LEFT, RIGHT, CENTER, ROW, Pack, TOP, BOTTOM
from functools import partial

class Hangman(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        theword = list("apple")
        self.lets = ["_" for x in theword]
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

        def val(value):
            if len(value) > 1:
                self.main_window.error_dialog("Invalid Input!","Only one letter!")
            elif value not in chars:
                self.main_window.error_dialog("Invalid Input!", "Not a letter!")
            else:
                return True
            return False
                #setoldval(value)
        def OK(widget):
            global selflets, selfword
            print(char_in.value)
            if val(char_in.value):
                if char_in.value in theword:
                    for x in range(len(theword)):
                        if theword[x] == char_in.value:
                            self.lets[x] = char_in.value
                            self.word.text = " ".join(self.lets)
            if self.word.text == " ".join(theword):
                self.main_window.info_dialog("You Won", f'The word was "{"".join(theword)}".')
                self.exit()
        main_box = toga.Box()
        main_box.style.update(direction=COLUMN, alignment=CENTER, padding=10)
        word_box = toga.Box()
        self.word = toga.Label(" ".join(self.lets))
        self.word.style.update(padding=10, alignment=CENTER)
        word_box.add(self.word)
        char_in = toga.TextInput()
        char_in.style.update(padding=10)
        but_box = toga.Box()
        but = toga.Button("OK",on_press=OK)
        but.style.update(padding=10)
        but_box.add(but)
        main_box.add(word_box)
        main_box.add(char_in)
        main_box.add(but_box)

        self.main_window = toga.MainWindow(title="Hangman")
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return Hangman()
