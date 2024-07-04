from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class MainWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        self.add_widget(MainLabel())
        self.add_widget(SelectionButtons())


class MainLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = "Вас приветсвует парсер по вакансиям с hh.ru"
        self.font_size = 30


class SelectionButtons(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (1, .2)

        self.add_widget(MainButton(text="Поиск по вакансиям"))
        self.add_widget(MainButton(text="Поиск по работодателям"))


class MainButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_press(self):
        pass
