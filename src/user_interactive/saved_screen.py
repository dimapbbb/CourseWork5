from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen


class SavedScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.name = "save_scr"

        self.add_widget(QuitButton())


class QuitButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = "В разработке..."
        self.font_size = 100

    def on_press(self):
        self.parent.manager.current = "main_scr"

