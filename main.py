import os
from dotenv import load_dotenv
from terminaltables import AsciiTable
from superjob import process_sj_vacancies
from headhunter import process_hh_vacancies


def make_table(vacancy: dict, table_headers: list, table_title: str):

    table_content = table_headers[:]

    for language, params in vacancy.items():
        language_stats = list(params.values())
        language_stats.insert(0, language)
        table_content.append(language_stats)
    table_instance = AsciiTable(table_content, table_title)

    return table_instance.table


def main():

    load_dotenv()
    sjob_token = os.getenv("SJOB_TOKEN")
    languages = os.getenv("LANGUAGES").split()
    table_headers = [["Язык программирования", "Вакансий найдено", "Вакансий обработано" , "Средняя зарплата"]]
    table_titles = ["SuperJob, Moscow", "HeadHunter, Moscow"]

    vacancies = [
        process_sj_vacancies(languages, sjob_token),
        process_hh_vacancies(languages)
    ]

    for title, vacancy in enumerate(vacancies):
        print(make_table(vacancy, table_headers, table_titles[title]))


if __name__ == "__main__":
    main()
