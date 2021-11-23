from terminaltables import AsciiTable
from headhunter import main

vacancies_data = main()

"""vacancies_data = {'C': {'average_salary': 153897,
                    'vacancies_found': 41,
                    'vacancies_processed': 34},
              'java': {'average_salary': 221987,
                       'vacancies_found': 62,
                       'vacancies_processed': 39},
              'python': {'average_salary': 133637,
                         'vacancies_found': 72,
                         'vacancies_processed': 58}}"""

table_data = [["Язык программирования", "Средняя зарплата", "Вакансий обработано", "Вакансий найдено"]]
title = "HeadHunter, Moscow"
for language, params in vacancies_data.items():
    stat = list(params.values())
    stat.append(language)
    table_data.append(list(reversed(stat)))

table_instance = AsciiTable(table_data, title)
print(table_instance.table)
