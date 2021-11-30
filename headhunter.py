import requests


def count_vacancies_found(vacancies):
    return vacancies["found"]


def count_average_salary_and_processed_vacancies(vacancies):
    salaries = []
    for vacancy in vacancies["items"]:
        salary = predict_rub_salary_hh(vacancy)
        if salary:
            salaries.append(salary)
    return int(sum(salaries) / len(salaries)), len(salaries)


def predict_rub_salary_hh(vacancy):
    if vacancy["salary"] and vacancy["salary"]["currency"] == "RUR":
        min_salary = vacancy["salary"]["from"]
        max_salary = vacancy["salary"]["to"]
        if not min_salary:
            return max_salary
        elif not max_salary:
            return min_salary
        else:
            return (min_salary + max_salary) / 2
    return None


def get_vacancies_hh(language, page):
    headers = {
        "User-Agent": "api-test-agent"
    }
    payload = {
        "text": f"{language}",
        "area": 1,
        "per_page": 100,
        "page": f"{page}"
    }
    url = "https://api.hh.ru/vacancies/"
    response = requests.get(url, headers=headers, params=payload)
    response.raise_for_status()
    vacancies = response.json()
    return vacancies


def generate_vacancies_data_hh(languages):
    vacancies_hh = {}
    total_pages = 3
    pages = range(total_pages)

    for language in languages:
        total_average_salary = 0
        total_vacancies_processed = 0
        for page in pages:
            vacancies = get_vacancies_hh(language, page)
            vacancies_found = count_vacancies_found(vacancies)
            average_salary, vacancies_processed = count_average_salary_and_processed_vacancies(vacancies)

            total_average_salary += average_salary
            total_vacancies_processed += vacancies_processed

            vacancies_hh.update({
                language: {
                    "vacancies_found": vacancies_found,
                    "vacancies_processed": total_vacancies_processed,
                    "average_salary": int(total_average_salary/total_pages)}
            })
    return vacancies_hh
