import requests
from salaries import predict_rub_salary_hh, count_sum_salary_and_processed_vacancies
from itertools import count


def get_vacancies(language: str, page: int):

    moscow_area = 1

    headers = {
        "User-Agent": "api-test-agent"
    }
    payload = {
        "text": language,
        "area": moscow_area,
        "per_page": 100,
        "page": page
    }
    url = "https://api.hh.ru/vacancies/"

    response = requests.get(url, headers=headers, params=payload)
    response.raise_for_status()
    vacancies = response.json()
    return vacancies


def process_language(language):

    total_sum_salary = 0
    total_vacancies_processed = 0
    for page in count():
        response = get_vacancies(language, page)
        vacancies = response["items"]
        vacancies_found = response["found"]
        total_pages = response["pages"]
        sum_salary, vacancies_processed = \
            count_sum_salary_and_processed_vacancies(vacancies, predict_rub_salary_hh)

        total_sum_salary += sum_salary
        total_vacancies_processed += vacancies_processed

        if page >= total_pages-1:
            break

    language_statistics = {
        "vacancies_found": vacancies_found,
        "vacancies_processed": total_vacancies_processed,
        "average_salary": int(total_sum_salary/total_vacancies_processed)
    }

    return language_statistics


def process_hh_vacancies(languages: list):

    vacancies_payments = {}

    for language in languages:
        language_statistics = process_language(language)
        vacancies_payments.update({language: language_statistics})
    return vacancies_payments
