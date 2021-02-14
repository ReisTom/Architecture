from ui.windows.main_window.states.i_window_state import IMainWindowState



class FullscreenState(IMainWindowState):

    def __init__(self, model):
        super().__init__(model)

    def move_to_next_format(self):
        self.main_model.main_controller.restore_window()
        self.main_model.main_controller.change_model_state(
            self.main_model.window_state)

    def on_drag(self):
        self.main_model.main_controller.restore_window()
        self.main_model.main_controller.change_model_state(
            self.main_model.window_state)
