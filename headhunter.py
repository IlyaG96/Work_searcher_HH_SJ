import requests
from pprint import pprint

languages = ["python", "java", "C"]



"""{'C': {'average_salary': 190334,
       'vacancies_found': 13572,
       'vacancies_processed': 314},
 'java': {'average_salary': 265234,
          'vacancies_found': 5231,
          'vacancies_processed': 248},
 'python': {'average_salary': 210452,
            'vacancies_found': 6997,
            'vacancies_processed': 201}}"""

headers = {
    "User-Agent": "api-test-agent"
}


# {
# vacancies_found: 6695
# vacancies_processed 13
# average_salary: 9988}


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


def main():
    vacancies_hh = {}
    total_pages = 5
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

    pprint(vacancies_hh)

# main()
