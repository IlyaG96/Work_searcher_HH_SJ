def predict_rub_salary_hh(vacancy: dict):

    if vacancy["salary"] and vacancy["salary"]["currency"] == "RUR":
        min_salary = vacancy["salary"]["from"]
        max_salary = vacancy["salary"]["to"]
        salary = predict_salary(min_salary, max_salary)
        return salary
    return None


def predict_rub_salary_sj(vacancy: dict):

    min_salary = vacancy["payment_from"]
    max_salary = vacancy["payment_to"]
    if not vacancy["currency"] == "rub" or not (min_salary or max_salary):
        return None
    else:
        salary = predict_salary(min_salary, max_salary)
        return salary


def predict_salary(salary_from: int, salary_to: int):

    if not salary_from:
        return salary_to*0.8
    elif not salary_to:
        return salary_from*1.2
    else:
        return (salary_from+salary_to) / 2
