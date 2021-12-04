import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication

from ui.components.sidemenu.sidemenu_controller import SidemenuController
from ui.windows.main_window.main_window import Ui_MainWindow
from ui.windows.main_window.main_window_model import MainWindowModel

class MainWindowController:
    def __init__(self, app):
        self.app = app
        self.main_window_model = MainWindowModel(self)
        self.main_window_ui = Ui_MainWindow(self)
        self.sidemenu_controller = SidemenuController(self)

        # connenct the buttons 
        self.main_window_ui.btn_close.clicked.connect(lambda: self.close_app())
        self.main_window_ui.btn_maximise_restore.clicked.connect(lambda: self.change_window_format())
        self.main_window_ui.btn_minimize.clicked.connect(lambda: self.minimize_window())
        self.main_window_ui.btn_tgl_menu.clicked.connect(lambda: self.change_sidemenu())

    def get_centerlayout(self):
        return self.main_window_ui.get_centerlayout()

    def build_toolbutton(self):
        pass

    def toogle_toolbar(self):
        pass

    def close_app(self):
        sys.exit(self.app.exec_())  #ToDo is this right?

    def change_window_format(self):
        self.main_window_model.state.move_to_next_format()

    def restore_window(self):
        self.main_window_ui.restore()

    def maximize_window(self):
        self.main_window_ui.maximize()

    def minimize_window(self):
        self.main_window_ui.minimize()

    def on_drag_window(self):
        self.main_window_model.state.on_drag()

    def change_model_state(self, state):
        self.main_window_model.set_state(state)

    def change_sidemenu(self):
        self.sidemenu_controller.sidemenu_model.sidemenu_state.move_to_next_format()  #ToDo Frage: kann ich direkt auf die zugreifen oder soll ich in jeder klasse eine eigene Funktion einbinden die weiterleitet??