from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput

from src.parser import HH
from src.user_interactive.result_window import ResultWindow


class EmployerScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.name = "emp_scr"

        self.add_widget(EmployerWidget())


class EmployerWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        self.add_widget(Label(text="Введите запрос:", font_size=100))
        self.add_widget(QueryInput())
        self.add_widget(SearchButton())
        self.add_widget(QuitButton())


class QueryInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (1, .2)
        self.font_size = 50
        self.multiline = False
        self.query = ""

    def on_text_validate(self):
        self.query = self.text

    def search_query(self):
        parsing = HH()
        result = ResultWindow(parsing.load_employers(self.query))
        return result.open()


class SearchButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = "Поиск"
        self.size_hint = (1, .2)

    def on_press(self):
        self.parent.children[2].on_text_validate()

    def on_release(self):
        self.parent.children[2].search_query()


class QuitButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = "back"
        self.size_hint = (1, .2)

    def on_press(self):
        self.parent.parent.manager.current = "main_scr"
