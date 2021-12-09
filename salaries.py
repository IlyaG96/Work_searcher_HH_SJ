def predict_rub_salary_hh(vacancy: dict):

    if vacancy.get("salary") and vacancy["salary"]["currency"] == "RUR":
        min_salary = vacancy["salary"]["from"]
        max_salary = vacancy["salary"]["to"]
        salary = count_salary(min_salary, max_salary)
        return salary
    return None


def predict_rub_salary_sj(vacancy: dict):

    if not vacancy.get("currency") == "rub":
        return None

    min_salary = vacancy.get("payment_from")
    max_salary = vacancy.get("payment_to")

    salary = count_salary(min_salary, max_salary)
    return salary


def count_salary(salary_from: int, salary_to: int):

    if not salary_from and not salary_to:
        return None
    if not salary_from:
        return salary_to*0.8
    elif not salary_to:
        return salary_from*1.2
    return (salary_from+salary_to) / 2


def count_sum_salary_and_processed_vacancies(vacancies, process_vacancy):

    salaries = []
    for vacancy in vacancies:
        salary = process_vacancy(vacancy)
        if salary:
            salaries.append(salary)
    return sum(salaries), len(salaries)