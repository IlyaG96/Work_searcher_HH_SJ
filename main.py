import os
from dotenv import load_dotenv
from terminaltables import AsciiTable
from superjob import generate_vacancies_data_sj
from headhunter import generate_vacancies_data_hh


def made_table(vacancy: dict, table_headers: list, table_title: str):

    table_data = table_headers[:]

    for language, params in vacancy.items():
        language_stats = list(params.values())
        language_stats.insert(0, language)
        table_data.append(language_stats)
    table_instance = AsciiTable(table_data, table_title)

    return table_instance.table


def main():

    load_dotenv()
    sjob_token = os.getenv("SJOB_TOKEN")
    languages = os.getenv("LANGUAGES").split()
    table_headers = [["Язык программирования", "Вакансий найдено", "Вакансий обработано" , "Средняя зарплата"]]
    table_titles = ["SuperJob, Moscow", "HeadHunter, Moscow"]

    vacancies = [
        generate_vacancies_data_sj(languages, sjob_token),
        generate_vacancies_data_hh(languages)
    ]
    for title, vacancy in enumerate(vacancies):
        print(made_table(vacancy, table_headers, table_titles[title]))


if __name__ == "__main__":
    main()
