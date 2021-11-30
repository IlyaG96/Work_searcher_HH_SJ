import requests


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


def get_response_sj(language, sjob_token):
    headers = {
        "X-Api-App-Id": sjob_token,
    }
    payload = {
        "count": 20,
        "page": 1,
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


def generate_vacancies_data_sj(languages, sjob_token):
    vacancies_sj = {}
    for language in languages:
        total_average_salary = 0
        total_vacancies_processed = 0
        sj_response = get_response_sj(language, sjob_token)
        vacancies = get_vacancies_sj(sj_response)
        vacancies_found = count_vacancies_found(sj_response)

        average_salary, processed_vacancies = count_average_salary_and_processed_vacancies(vacancies)

        total_average_salary += average_salary
        total_vacancies_processed += processed_vacancies

        vacancies_sj.update({
            language: {
                "vacancies_found": vacancies_found,
                "vacancies_processed": total_vacancies_processed,
                "average_salary": int(total_average_salary)}
        })

    return vacancies_sj
