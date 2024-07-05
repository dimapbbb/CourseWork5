from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from src.user_interactive.employer_screen import EmployerScreen
from src.user_interactive.main_screen import MainScreen
from src.user_interactive.saved_screen import SavedScreen
from src.user_interactive.vacancy_screen import VacancyScreen


class HHParser(App):
    title = "Парсер НН"
    icon = "data/icon.png"

    def build(self):
        my_app = ScreenManager()

        my_app.add_widget(MainScreen())
        my_app.add_widget(EmployerScreen())
        my_app.add_widget(VacancyScreen())
        my_app.add_widget(SavedScreen())

        return my_app


if __name__ == "__main__":
    HHParser().run()
