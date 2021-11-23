import terminaltables
from terminaltables import AsciiTable, DoubleTable, SingleTable

"""{'C': {'average_salary': 190334,
       'vacancies_found': 13572,
       'vacancies_processed': 314},
 'java': {'average_salary': 265234,
          'vacancies_found': 5231,
          'vacancies_processed': 248},
 'python': {'average_salary': 210452,
            'vacancies_found': 6997,
            'vacancies_processed': 201}}"""

"""
{'C': {'average_salary': 153897,
       'vacancies_found': 41,
       'vacancies_processed': 34},
 'java': {'average_salary': 221987,
          'vacancies_found': 62,
          'vacancies_processed': 39},
 'python': {'average_salary': 133637,
            'vacancies_found': 72,
            'vacancies_processed': 58}}
"""

table_data = [{'C': {'average_salary': 153897,
                    'vacancies_found': 41,
                    'vacancies_processed': 34},
              'java': {'average_salary': 221987,
                       'vacancies_found': 62,
                       'vacancies_processed': 39},
              'python': {'average_salary': 133637,
                         'vacancies_found': 72,
                         'vacancies_processed': 58}}]

title = "HeadHunter, Moscow"

table_instance = AsciiTable(table_data, title)
table_instance.justify_columns[2] = 'right'

print(table_instance.table)
