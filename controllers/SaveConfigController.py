class SaveConfigController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def open_view(self):
        print("I should open save config")
