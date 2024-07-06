from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.modalview import ModalView
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput

from src.DBManager import DBManager
from src.file_worker import WorkWithSQL
from src.user_interactive.create_table import CreateTableWindow
from src.user_interactive.print_save_data import PrintSaveWindow


class SavedScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.name = "DBM_scr"

        self.add_widget(SavedWidget())


class SavedWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        self.add_widget(WorkTable(text="Создать таблицу", ind=0))
        self.add_widget(WorkTable(text="Сохраненые вакансии", ind=1))
        self.add_widget(WorkTable(text="Сохраненые работодатели", ind=2))
        self.add_widget(DBM(text="get_companies_and_vacancies_count", ind=0))
        self.add_widget(DBM(text="get_all_vacancies", ind=1))
        self.add_widget(DBM(text="get_vacancies_with_higher_salary", ind=2))
        self.add_widget(DBM(text="get_vacancies_with_keyword", ind=3))

        self.add_widget(QuitButton())


class WorkTable(Button):
    def __init__(self, ind, **kwargs):
        super().__init__(**kwargs)
        self.ind = ind
        self.user = WorkWithSQL()

    def on_press(self):
        if self.ind == 0:
            CreateTableWindow().open()
        elif self.ind == 1:
            PrintSaveWindow(self.user.read_vacancies()).open()
        elif self.ind == 2:
            PrintSaveWindow(self.user.read_employers()).open()


class DBM(Button):
    def __init__(self, ind, **kwargs):
        super().__init__(**kwargs)
        self.ind = ind
        self.user = DBManager()

    def on_press(self):
        if self.ind == 0:
            PrintSaveWindow(self.user.get_companies_and_vacancies_count()).open()
        elif self.ind == 1:
            PrintSaveWindow(self.user.get_all_vacancies()).open()
        elif self.ind == 2:
            PrintSaveWindow(self.user.get_vacancies_with_higher_salary()).open()
        elif self.ind == 3:
            KeywordInput(self.user).open()


class KeywordInput(ModalView):
    def __init__(self, user, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (1, .2)

        self.add_widget(KeywordWidget(user))


class KeywordWidget(BoxLayout):
    def __init__(self, user, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(TextInput(hint_text="Keyword"))
        self.add_widget(GoButton(user))


class GoButton(Button):
    def __init__(self, user, **kwargs):
        super().__init__(**kwargs)
        self.text = "GO"
        self.user = user
        self.size_hint = (.3, 1)

    def on_press(self):
        keyword = self.parent.children[1].text
        PrintSaveWindow(self.user.get_vacancies_with_keyword(keyword)).open()


class QuitButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = "back"

    def on_press(self):
        self.parent.parent.manager.current = "main_scr"
