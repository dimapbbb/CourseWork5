class Employer:
    """
    Класс описывающий работодателя
    """
    def __init__(self, employer_id, name, open_vacancies, vacancies_url):
        self.employer_id = employer_id
        self.name = name
        self.open_vacancies = open_vacancies
        self.vacancies_url = self.__validation_data(vacancies_url)

    def __str__(self):
        return (f"{self.employer_id}\n"
                f"{self.name}\n"
                f"{self.open_vacancies}\n"
                f"{self.vacancies_url}")

    @staticmethod
    def __validation_data(data):
        if data:
            return data
        else:
            return "NULL"

    @classmethod
    def new_employer(cls, employer):
        employer_id = employer.get("id")
        name = employer.get("name")
        open_vacancies = employer.get("open_vacancies")
        vacancies_url = employer.get("vacancies_url")
        return cls(employer_id, name, open_vacancies, vacancies_url)
