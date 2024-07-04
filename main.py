from kivy.app import App

from src.user_inteactiv import MainWidget


class HHParser(App):
    title = "Парсер НН"
    icon = "data/icon.png"

    def build(self):
        return MainWidget()


if __name__ == "__main__":
    HHParser().run()
