from ui.windows.main_window.states.fullscreen_state import FullscreenState
from ui.windows.main_window.states.window_state import WindowState


class MainWindowModel:
    def __init__(self, controller):
        self.main_controller = controller
        self.window_state = WindowState(self)
        self.fullscreen_state = FullscreenState(self)
        self.state = self.window_state

    def set_state(self, state):
        self.state = state


