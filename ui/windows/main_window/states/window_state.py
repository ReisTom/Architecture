
from ui.windows.main_window.states.i_window_state import IMainWindowState


class WindowState(IMainWindowState):

    def __init__(self, model):
        super().__init__(model)

    def move_to_next_format(self):
        self.main_model.main_controller.maximize_window()
        self.main_model.main_controller.change_model_state(
            self.main_model.fullscreen_state)

    def on_drag(self):
        super().on_drag()