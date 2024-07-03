class Vacancy:
    def __init__(self, name, area, salary, url):
        self.name = self.__validation_data(name)
        self.area = self.__validation_data(area)
        self.url = self.__validation_data(url)
        self.salary = salary

    def __str__(self):
        return (f"{self.name}\n"
                f"Город: {self.area}\n"
                f"Зарплата: {self.salary if self.salary else 'Не указана'}\n"
                f"Ссылка: {self.url}")

    def __lt__(self, other):
        if not self.salary:
            return "Зарплата не указана"
        elif not other.salary:
            return "hi"
        elif self.salary < other.salary:
            return True
        else:
            return False

    @staticmethod
    def __validation_data(data):
        if data:
            return data
        else:
            return "Отсутсвует"

    @classmethod
    def new_vacancy(cls, vacancy):
        name = vacancy.get("name")
        area = vacancy.get("area").get("name")
        if vacancy.get("salary"):
            if vacancy.get("salary").get("from"):
                salary = vacancy.get("salary").get("from")
            else:
                salary = 0
        else:
            salary = 0
        url = vacancy.get("alternate_url")
        return cls(name, area, salary, url)
