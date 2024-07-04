import json
import psycopg2

from os.path import abspath
from abc import ABC, abstractmethod

from src.parser import HH
from src.vacancy import Vacancy


class FileWork(ABC):

    @abstractmethod
    def read_employers(self):
        """ Чтение сохраненых работодателей """
        pass

    @abstractmethod
    def save_employer(self, employer):
        """ Сохранение работодателя """
        pass

    @abstractmethod
    def delete_employers(self):
        """ Очитска всех работодателей """
        pass

    @abstractmethod
    def read_vacancies(self):
        """ Чтение сохраненых вакансии """
        pass

    @abstractmethod
    def save_vacancy(self, vacancy):
        """ Сохранение вакансии """
        pass

    @abstractmethod
    def delete_vacancies(self):
        """ Очистка сохранных вакансий"""
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


class WorkWithSQL(FileWork):
    def __init__(self):
        self.conn_params = {"host": "localhost",
                            "dbname": "CourseWork5",
                            "user": "postgres",
                            "password": "12345"}

    def read_employers(self):
        with psycopg2.connect(**self.conn_params) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM employers")
                employers = cur.fetchall()
        return employers

    def save_employer(self, employer):
        query = (f"INSERT INTO employers VALUES ("
                 f"'{employer.employer_id}', "
                 f"'{employer.name}', "
                 f"'{employer.open_vacancies}', "
                 f"'{employer.vacancies_url}')")
        with psycopg2.connect(**self.conn_params) as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                conn.commit()
        # Сохранение открытых вакансий работодателя
        exam = HH()
        vacancies = exam.employer_vacancies(employer.employer_id)
        for vacancy in vacancies:
            vac = Vacancy.new_vacancy(vacancy)
            self.save_vacancy(vac)

    def delete_employers(self):
        with psycopg2.connect(**self.conn_params) as conn:
            with conn.cursor() as cur:
                cur.execute("TRUNCATE TABLE employers")
                conn.commit()

    def read_vacancies(self):
        with psycopg2.connect(**self.conn_params) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM vacancies")
                return cur.fetchall()

    def save_vacancy(self, vacancy):
        query = (f"INSERT INTO vacancies VALUES ("
                 f"'{vacancy.name}', "
                 f"'{vacancy.area}', "
                 f"'{vacancy.salary}', "
                 f"'{vacancy.url}', "
                 f"'{vacancy.employer_id}')")
        with psycopg2.connect(**self.conn_params) as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                conn.commit()

    def delete_vacancies(self):
        with psycopg2.connect(**self.conn_params) as conn:
            with conn.cursor() as cur:
                cur.execute("TRUNCATE TABLE vacancies")
                conn.commit()
