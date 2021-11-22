import requests
from pprint import pprint

languages = ["python", "java", "C"]

headers = {
    "User-Agent": "api-test-agent"
}


# {
# vacancies_found: 6695
# vacancies_processed 13
# average_salary: 9988}


def count_vacancies_found(vacancies):
    return vacancies["found"]


def count_average_salary(vacancies):
    salaries = []
    for vacancy in vacancies["items"]:
        salary = predict_rub_salary(vacancy)
        if salary:
            salaries.append(int(salary))
    return int(sum(salaries) / len(salaries)), len(salaries)


def predict_rub_salary(vacancy):
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


def get_vacancies_hh(language):
    payload = {
        "text": f"{language}",
        "area": "1",
    }
    url = f"https://api.hh.ru/vacancies/"
    response = requests.get(url, headers=headers, params=payload)
    response.raise_for_status()
    vacancies = response.json()
    return vacancies


def main():
    vacancies_hh = {}
    for language in languages:
        vacancies = get_vacancies_hh(language)
        average_salary, vacancies_processed = count_average_salary(vacancies)
        vacancies_found = count_vacancies_found(vacancies)
        vacancies_hh.update({
            language: {
                "vacancies_found": vacancies_found,
                "vacancies_processed": vacancies_processed,
                "average_salary": average_salary, }
        })

    print(vacancies_hh)
main()
