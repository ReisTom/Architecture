import sys

from PyQt5.QtWidgets import QApplication

from ui.windows.main_window.main_controller import MainWindowController


class Application:
    def __init__(self):
        self.main_controller = MainWindowController(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = Application()
    sys.exit(app.exec_())
