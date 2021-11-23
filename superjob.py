import os
from pprint import pprint
import requests
from dotenv import load_dotenv
load_dotenv()
sjob_token = os.getenv("SJOB_TOKEN")


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

def count_average_salary_and_processed_vacancies(vacancies):
    salaries = []
    for number, vacancy in enumerate(vacancies):
        salary = predict_rub_salary_sj(vacancy)
        if salary:
            salaries.append(salary)
    return int(sum(salaries) / len(salaries)), len(salaries)


def predict_rub_salary_sj(vacancy):
    min_salary = vacancy["payment_from"]
    max_salary = vacancy["payment_to"]

    if not vacancy["currency"] == "rub" or not (min_salary or max_salary):
        return None
    elif not min_salary:
        return max_salary
    elif not max_salary:
        return min_salary
    else:
        return (min_salary + max_salary) / 2


def get_response_sj(language, page):

    headers = {
        "X-Api-App-Id": sjob_token,
    }
    payload = {
        "count": 100,
        "page": {page},
        "town": "Москва",
        "keyword": f"Программист {language}"
    }
    url = "https://api.superjob.ru/2.0/vacancies/"
    response = requests.get(url, headers=headers, params=payload)
    response.raise_for_status()
    sj_response = response.json()
    return sj_response


def get_vacancies_sj(sj_response):
    return sj_response["objects"]


def count_vacancies_found(sj_response):
    return sj_response["total"]

#for number, vacancy in enumerate(get_vacancies_sj()):
#    profession = vacancy["profession"]
#    town = vacancy["town"]["title"]
#    salary = predict_rub_salary_sj(vacancy)
#    print(f"{profession}, {town}, {salary}")


def main():
    languages = ["python", "java", "C"]
    vacancies_sj = {}
    total_pages = 1
    pages = range(total_pages)
    for language in languages:
        total_average_salary = 0
        total_vacancies_processed = 0
        for page in pages:
            sj_response = get_response_sj(language, page)

            vacancies = get_vacancies_sj(sj_response)
            vacancies_found = count_vacancies_found(sj_response)

            average_salary, processed_vacancies = count_average_salary_and_processed_vacancies(vacancies)

            total_average_salary += average_salary
            total_vacancies_processed += processed_vacancies

            vacancies_sj.update({
                language: {
                    "vacancies_found": vacancies_found,
                    "vacancies_processed": total_vacancies_processed,
                    "average_salary": int(total_average_salary/total_pages)}
            })

    pprint(vacancies_sj)


# main()