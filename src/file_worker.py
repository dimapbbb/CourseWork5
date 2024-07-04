import json

from os.path import abspath
from abc import ABC, abstractmethod


class FileWork(ABC):

    @abstractmethod
    def read_employers(self):
        pass

    @abstractmethod
    def save_employer(self, employer):
        pass

    @abstractmethod
    def delete_employers(self):
        pass


class FileWorkJson(FileWork):
    def __init__(self):
        self.path_to_emp = abspath("data/employers.json")
        self.path_to_vac = abspath("data/vacancies.json")

    def read_employers(self):
        with open(self.path_to_emp, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def save_employer(self, employer):
        with open(self.path_to_emp, "r", encoding="utf-8") as file:
            data = json.load(file)

        data.append(employer.__dict__)

        with open(self.path_to_emp, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def delete_employers(self):
        with open(self.path_to_emp, "w", encoding="utf-8") as file:
            file.write("[]")

    def read_vacancies(self):
        with open(self.path_to_vac, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def save_vacancy(self, vacancy):
        with open(self.path_to_vac, "r", encoding="utf-8") as file:
            data = json.load(file)

        data.append(vacancy.__dict__)

        with open(self.path_to_vac, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def delete_vacancies(self):
        with open(self.path_to_vac, "w", encoding="utf-8") as file:
            file.write("[]")
