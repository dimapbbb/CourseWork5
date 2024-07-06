from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.carousel import Carousel
from kivy.uix.modalview import ModalView
from kivy.uix.textinput import TextInput

from src.DBManager import DBManager


class CreateTableWindow(ModalView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.auto_dismiss = False

        self.add_widget(CreateTableWidget())


class CreateTableWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        self.add_widget(TableName())
        self.add_widget(QuantityColumns())
        self.add_widget(NextButton())
        self.add_widget(QuitButton())


class TableName(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hint_text = "Enter table name (NOT NULL, str, 1_word)"
        self.size_hint = (1, .2)
        self.multiline = False


class QuantityColumns(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hint_text = "Введите колличество колонок (NOT NUll, int)"
        self.size_hint = (1, .2)
        self.multiline = False


class NextButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = "Next"
        self.size_hint = (1, .2)

    def on_press(self):
        quantity = self.parent.children[2].text
        table_name = self.parent.children[3].text
        if quantity and table_name and quantity.isdigit() and len(table_name.split()) == 1:
            ColumnNamesWindow(quantity, table_name).open()


class ColumnNamesWindow(ModalView):
    def __init__(self, quantity, table_name, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(ColumnNamesBox(quantity, table_name))


class ColumnNamesBox(BoxLayout):
    def __init__(self, quantity, table_name, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        self.add_widget(ColumnsInput(quantity))
        self.add_widget(NavigationBox())
        self.add_widget(CreateTableButton(table_name))


class ColumnsInput(Carousel):
    def __init__(self, quantity, **kwargs):
        super().__init__(**kwargs)

        self.columns_input = ["" for _ in range(int(quantity))]

        for i in range(int(quantity)):
            self.columns_input[i] = ColumnInput()
            self.add_widget(self.columns_input[i])


class ColumnInput(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        self.add_widget(TextInput(hint_text="Column name (default = column)", multiline=False))
        self.add_widget(TextInput(hint_text="Column type (default = text)", multiline=False))


class NavigationBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (1, .2)

        self.add_widget(NavigationButtons(index="left", text="<--", font_size=100))

        self.add_widget(NavigationButtons(index="right", text="-->", font_size=100))


class NavigationButtons(Button):
    def __init__(self, index, **kwargs):
        super().__init__(**kwargs)
        self.index = index

    def on_press(self):
        if self.index == "left":
            self.parent.parent.children[2].load_previous()
        elif self.index == "right":
            self.parent.parent.children[2].load_next()


class CreateTableButton(Button):
    def __init__(self, table_name, **kwargs):
        super().__init__(**kwargs)
        self.text = "Create table"
        self.size_hint = (1, .3)

        self.table_name = table_name

    def on_press(self):
        columns = []
        for i, column_input in enumerate(self.parent.children[1].columns_input):

            column_text = column_input.children[1].text
            column_name = column_text if column_text else f"column_{i}"

            column_type = column_input.children[0].text
            column_type = column_type if column_type else "text"

            column = column_name + " " + column_type
            columns.append(column)

        query = f"CREATE TABLE {self.table_name} ({', '.join(columns)})"
        bd = DBManager()
        bd.create_table(query)

    def on_release(self):
        self.parent.parent.dismiss()


class QuitButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = "back"
        self.size_hint = (1, .2)

    def on_press(self):
        self.parent.parent.dismiss()
