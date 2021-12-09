import requests
from salaries import predict_rub_salary_sj, count_sum_salary_and_processed_vacancies
from itertools import count


def get_response(language: str, sjob_token: str, page: int):

    headers = {
        "X-Api-App-Id": sjob_token,
    }
    payload = {
        "count": 100,
        "page": page,
        "town": "Москва",
        "keyword": language
    }
    url = "https://api.superjob.ru/2.0/vacancies/"

    response = requests.get(url, headers=headers, params=payload)
    response.raise_for_status()
    sj_response = response.json()
    return sj_response


def process_sj_vacancies(languages: list, sjob_token: str):

    vacancies_payments = {}
    for language in languages:
        total_sum_salary = 0
        total_vacancies_processed = 0
        for page in count():
            response = get_response(language, sjob_token, page)
            more_vacancies = response["more"]
            vacancies = response["objects"]
            vacancies_found = response["total"]

            sum_salary, processed_vacancies =\
                count_sum_salary_and_processed_vacancies(vacancies, predict_rub_salary_sj)

            total_sum_salary += sum_salary
            total_vacancies_processed += processed_vacancies

            if not more_vacancies:
                break

        vacancies_payments.update({
            language: {
                "vacancies_found": vacancies_found,
                "vacancies_processed": total_vacancies_processed,
                "average_salary": int(total_sum_salary/total_vacancies_processed)}
        })

    return vacancies_payments
