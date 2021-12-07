import requests
from salaries import predict_rub_salary_hh, count_sum_salary_and_processed_vacancies
from itertools import count


def get_vacancies_hh(language: str, page: int):

    headers = {
        "User-Agent": "api-test-agent"
    }
    payload = {
        "text": language,
        "area": 1,
        "per_page": 100,
        "page": page
    }
    url = "https://api.hh.ru/vacancies/"

    response = requests.get(url, headers=headers, params=payload)
    response.raise_for_status()
    vacancies = response.json()
    return vacancies


def process_hh_vacancies(languages: list):

    vacancies_payments = {}

    for language in languages:
        total_sum_salary = 0
        total_vacancies_processed = 0
        for page in count():
            hh_response = get_vacancies_hh(language, page)
            vacancies = hh_response.get("items")
            vacancies_found = hh_response.get("found")
            total_pages = hh_response.get("pages")
            sum_salary, vacancies_processed = \
                count_sum_salary_and_processed_vacancies(vacancies, predict_rub_salary_hh)

            total_sum_salary += sum_salary
            total_vacancies_processed += vacancies_processed

            if page >= total_pages-1:
                break

        vacancies_payments.update({
            language: {
                "vacancies_found": vacancies_found,
                "vacancies_processed": total_vacancies_processed,
                "average_salary": int(total_sum_salary/total_vacancies_processed)}
        })

    return vacancies_payments
