from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen

from src.user_interactive.create_table import CreateTableWindow


class SavedScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.name = "save_scr"

        self.add_widget(SavedWidget())


class SavedWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        self.add_widget(CreateTable())
        self.add_widget(QuitButton())


class CreateTable(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = "Создать таблицу PostgreSQL"

    def on_press(self):
        CreateTableWindow().open()


class QuitButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = "back"

    def on_press(self):
        self.parent.parent.manager.current = "main_scr"

