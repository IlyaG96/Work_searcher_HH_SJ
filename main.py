from terminaltables import AsciiTable
from superjob import generate_vacancies_data_sj
from headhunter import generate_vacancies_data_hh
from dotenv import load_dotenv
import os


def main():
    languages = ["Python", "Java", "C", "PHP", "C#", "Go"]
    load_dotenv()
    sjob_token = os.getenv("SJOB_TOKEN")
    table_headers = [["Язык программирования", "Средняя зарплата", "Вакансий обработано", "Вакансий найдено"]]
    table_titles = ["SuperJob, Moscow", "HeadHunter, Moscow"]
    vacancies = [
        generate_vacancies_data_sj(languages, sjob_token),
        generate_vacancies_data_hh(languages)
    ]
    for num, vacancies_data in enumerate(vacancies):
        table_data = table_headers[:]
        for language, params in vacancies_data.items():
            stat = list(params.values())
            stat.append(language)
            table_data.append(list(reversed(stat)))
        table_instance = AsciiTable(table_data, table_titles[num])
        print(table_instance.table)
        table_data.clear()


if __name__ == '__main__':
    main()
