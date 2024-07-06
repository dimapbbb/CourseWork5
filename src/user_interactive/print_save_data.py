from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.carousel import Carousel
from kivy.uix.label import Label
from kivy.uix.modalview import ModalView


class PrintSaveWindow(ModalView):
    def __init__(self, content, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(PrintSaveWidget(content))


class PrintSaveWidget(BoxLayout):
    def __init__(self, content, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        self.add_widget(PrintBox(content))
        self.add_widget(NavigationBox())
        self.add_widget(QuitButton())


class PrintBox(Carousel):
    def __init__(self, content, **kwargs):
        super().__init__(**kwargs)

        for row in range(len(content)):
            self.add_widget(PrintRow(content[row]))


class PrintRow(BoxLayout):
    def __init__(self, row, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        for value in range(len(row)):
            self.add_widget(Label(text=str(row[value])))


class NavigationBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (1, .2)

        self.add_widget(NavigationButtons(index="left", text="<--", font_size=100))
        self.add_widget(NavigationButtons(index="delete", text="Delete"))
        self.add_widget(NavigationButtons(index="right", text="-->", font_size=100))


class NavigationButtons(Button):
    def __init__(self, index, **kwargs):
        super().__init__(**kwargs)
        self.index = index

    def on_press(self):
        if self.index == "delete":
            self.text = "В разработке..."
            self.disabled = True
        elif self.index == "left":
            self.parent.parent.children[2].load_previous()
        elif self.index == "right":
            self.parent.parent.children[2].load_next()


class QuitButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = "back"
        self.size_hint = (1, .2)

    def on_press(self):
        self.parent.parent.dismiss()
