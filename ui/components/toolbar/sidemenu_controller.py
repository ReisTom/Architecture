from ui.components.toolbar import sidemenu_view
from ui.components.toolbar.sidemenu_model import SidemenuModel
from ui.components.toolbar.sidemenu_view import SidemenuView


class SidemenuController:
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.sidemenu_model = SidemenuModel(self)
        self.sidemenu_view = SidemenuView(self.main_controller.get_centerlayout())



    def extend_sidemenu(self):
        self.sidemenu_view.extend("here goes the names")

    def minimize_sidemenu(self):
        self.sidemenu_view.minimize()