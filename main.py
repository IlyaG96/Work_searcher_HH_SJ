import sys

from terminaltables import AsciiTable
from superjob import generate_vacancies_data_sj
from headhunter import generate_vacancies_data_hh
from dotenv import load_dotenv
import os


def fetch_vacancies(languages, sjob_token):
    try:
        vacancies = [
            generate_vacancies_data_sj(languages, sjob_token),
            generate_vacancies_data_hh(languages)
        ]
    except ZeroDivisionError:
        sys.exit("Попробуйте чуть позже или уменьшите количество языков в .env Ошибка может быть"
                 " связана с ограничением на количество запросов сайта superjob.ru")

    return vacancies


def print_table(vacancies, table_headers, table_titles):
    for num, vacancies_data in enumerate(vacancies):
        table_data = table_headers[:]
        for language, params in vacancies_data.items():
            stat = list(params.values())
            stat.insert(0, language)
            table_data.append(stat)
        table_instance = AsciiTable(table_data, table_titles[num])
        print(table_instance.table)

def main():
    load_dotenv()
    sjob_token = os.getenv("SJOB_TOKEN")
    languages = os.getenv("LANGUAGES").split()
    table_headers = [["Язык программирования", "Вакансий обработано", "Вакансий найдено", "Средняя зарплата"]]
    table_titles = ["SuperJob, Moscow", "HeadHunter, Moscow"]
    vacancies = fetch_vacancies(languages, sjob_token)
    print_table(vacancies, table_headers, table_titles)


if __name__ == "__main__":
    main()
