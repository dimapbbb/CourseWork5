from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.carousel import Carousel
from kivy.uix.label import Label
from kivy.uix.modalview import ModalView

from src.employer import Employer
from src.file_worker import WorkWithSQL
from src.vacancy import Vacancy


class ResultWindow(ModalView):
    def __init__(self, query, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(ResultWidget(query))


class ResultWidget(BoxLayout):
    def __init__(self, query, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        self.add_widget(LabelInfo(len(query[0])))
        self.add_widget(ResultBox(query))
        self.add_widget(NavigationBox())
        self.add_widget(FileWorkBox())


class LabelInfo(Label):
    def __init__(self, quantity_results, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (1, .1)
        self.font_size = 40
        self.text = f"Найдено {quantity_results} результатов"


class ResultBox(Carousel):
    def __init__(self, query, **kwargs):
        super().__init__(**kwargs)

        if query[1] == "emp":
            for i in range(len(query[0])):
                employer = Employer.new_employer(query[0][i])
                self.add_widget(PrintResult(text=str(employer), content=employer))
        elif query[1] == "vac":
            for i in range(len(query[0])):
                vacancy = Vacancy.new_vacancy(query[0][i])
                self.add_widget(PrintResult(text=str(vacancy), content=vacancy))


class PrintResult(Label):
    def __init__(self, content, **kwargs):
        super().__init__(**kwargs)
        self.font_size = 25
        self.content = content


class NavigationBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(NavigationButtons(index="left", text="<--", font_size=100))
        self.add_widget(NavigationButtons(index="new_query", text="новый запрос"))
        self.add_widget(NavigationButtons(index="right", text="-->", font_size=100))


class NavigationButtons(Button):
    def __init__(self, index, **kwargs):
        super().__init__(**kwargs)
        self.index = index

    def on_press(self):
        if self.index == "new_query":
            self.parent.parent.parent.dismiss()
        elif self.index == "left":
            self.parent.parent.children[2].load_previous()
        elif self.index == "right":
            self.parent.parent.children[2].load_next()


class FileWorkBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(FileWorkButtons(text="Save"))


class FileWorkButtons(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_press(self):
        user = WorkWithSQL()
        content = self.parent.parent.children[2].current_slide.content
        if isinstance(content, Vacancy):
            user.save_vacancy(content)
        elif isinstance(content, Employer):
            user.save_employer(content)
