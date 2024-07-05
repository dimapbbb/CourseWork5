from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen


class MainScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.name = "main_scr"

        self.add_widget(MainWidget())


class MainWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        self.add_widget(MainLabel())
        self.add_widget(MainButtons(index=0, text="По вакансиям"))
        self.add_widget(MainButtons(index=1, text="По работодателям"))


class MainLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = "Вас приветсвует парсер по вакансиям с hh.ru"
        self.font_size = 30


class MainButtons(Button):
    def __init__(self, index, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (1, .2)
        self.index = index

    def on_press(self):
        if self.index:
            self.parent.parent.manager.current = "emp_scr"
        elif not self.index:
            self.parent.parent.manager.current = "vac_scr"

