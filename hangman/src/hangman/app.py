"""
Hangman game
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, LEFT, RIGHT, ROW, Pack


class Hangman(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box()

        self.main_window = toga.MainWindow(title="Hangman")
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return Hangman()
