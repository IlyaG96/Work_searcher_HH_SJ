import requests
from salaries import predict_rub_salary_sj
from itertools import count
from pprint import pprint


def count_average_salary_and_processed_vacancies(vacancies):
    salaries = []
    for number, vacancy in enumerate(vacancies):
        salary = predict_rub_salary_sj(vacancy)
        if salary:
            salaries.append(salary)
    return sum(salaries), len(salaries)


def get_response_sj(language, sjob_token, page):
    headers = {
        "X-Api-App-Id": sjob_token,
    }
    payload = {
        "count": 100,
        "page": page,
        "town": "Москва",
        "keyword": f"{language}"
    }
    url = "https://api.superjob.ru/2.0/vacancies/"
    response = requests.get(url, headers=headers, params=payload)
    response.raise_for_status()
    sj_response = response.json()
    return sj_response


def get_vacancies_sj(sj_response):
    return sj_response["objects"]


def generate_vacancies_data_sj(languages, sjob_token):
    vacancies_sj = {}
    for language in languages:
        total_average_salary = 0
        total_vacancies_processed = 0
        for page in count():
            sj_response = get_response_sj(language, sjob_token, page)
            more_vacancies = sj_response["more"]
            vacancies = get_vacancies_sj(sj_response)
            vacancies_found = sj_response["total"]

            average_salary, processed_vacancies = count_average_salary_and_processed_vacancies(vacancies)

            total_average_salary += average_salary
            total_vacancies_processed += processed_vacancies

            vacancies_sj.update({
                language: {
                    "vacancies_found": vacancies_found,
                    "vacancies_processed": total_vacancies_processed,
                    "average_salary": int(total_average_salary/total_vacancies_processed)}
            })
            if not more_vacancies:
                break

    return vacancies_sj
