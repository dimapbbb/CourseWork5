import psycopg2

from src.file_worker import WorkWithSQL


class DBManager(WorkWithSQL):
    """
    Класс для работы с базой данных
    """
    def __init__(self):
        super().__init__()

    def get_companies_and_vacancies_count(self):
        """ получает список всех компаний и количество вакансий у каждой компании """
        with psycopg2.connect(**self.conn_params) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT employer_name, open_vacancies "
                            "FROM employers")
                return cur.fetchall()

    def get_all_vacancies(self):
        """ получает список всех вакансий с указанием названия компании,
        названия вакансии, зарплаты, ссылки на вакансию """
        with psycopg2.connect(**self.conn_params) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT vacancy_name, employers.employer_name, salary, vacancies.url "
                            "FROM vacancies "
                            "JOIN employers USING (employer_id)")
                return cur.fetchall()

    def get_avg_salary(self):
        """ получает среднюю зарплату по вакансиям """
        with psycopg2.connect(**self.conn_params) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT AVG(salary) FROM vacancies")
                return cur.fetchone()

    def get_vacancies_with_higher_salary(self):
        """ получает список всех вакансий, у которых зарплата выше средней по всем вакансиям """
        avg = list(self.get_avg_salary())
        query = f"SELECT * FROM vacancies WHERE salary > {avg[0]}"
        with psycopg2.connect(**self.conn_params) as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                return cur.fetchall()

    def get_vacancies_with_keyword(self, keyword):
        """ получает список всех вакансий, в названии которых содержатся переданные в метод слова """

        query = (f"SELECT * FROM vacancies "
                 f"WHERE vacancy_name LIKE '%{keyword}%'")
        with psycopg2.connect(**self.conn_params) as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                return cur.fetchall()

    def create_table(self, query):
        with psycopg2.connect(**self.conn_params) as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                conn.commit()
