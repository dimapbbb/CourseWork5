from abc import ABC, abstractmethod

import requests


class Parser(ABC):
    @abstractmethod
    def load_vacancies(self, keyword, quantity):
        pass

    @abstractmethod
    def load_employers(self, query):
        pass


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    """
    def __init__(self):
        self.url = 'https://api.hh.ru/'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 10}

    def load_vacancies(self, keyword, quantity):
        url = self.url + "vacancies/"
        self.params["text"] = keyword
        vacancies_list = []

        while self.params["page"] != quantity // 10 + 1:
            response = requests.get(url, headers=self.headers, params=self.params)
            vacancies = response.json()["items"]
            vacancies_list.extend(vacancies)
            self.params['page'] += 1
        return vacancies_list

    def load_employers(self, query):
        url = self.url + "employers/"
        self.params["text"] = query

        response = requests.get(url, headers=self.headers, params=self.params)
        employers = response.json()["items"]
        return employers

    def employer_vacancies(self, employer_id):
        """ Получение вакансий по ID работодателя """

        url = self.url + 'vacancies?employer_id=' + employer_id
        vacancies_list = []

        while self.params["page"] != 50:
            response = requests.get(url, headers=self.headers, params=self.params)
            vacancies = response.json()["items"]
            vacancies_list.extend(vacancies)
            self.params['page'] += 1
        return vacancies_list
