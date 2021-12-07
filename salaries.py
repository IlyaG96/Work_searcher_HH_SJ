def predict_rub_salary_hh(vacancy: dict):

    if vacancy.get("salary") and vacancy.get("salary").get("currency") == "RUR":
        min_salary = vacancy.get("salary").get("from")
        max_salary = vacancy.get("salary").get("to")
        salary = predict_salary(min_salary, max_salary)
        return salary
    return None


def predict_rub_salary_sj(vacancy: dict):

    min_salary = vacancy.get("payment_from")
    max_salary = vacancy.get("payment_to")

    if not vacancy.get("currency") == "rub":
        return None

    salary = predict_salary(min_salary, max_salary)
    return salary


def predict_salary(salary_from: int, salary_to: int):

    if not salary_from and not salary_to:
        return None
    if not salary_from:
        return salary_to*0.8
    elif not salary_to:
        return salary_from*1.2
    return (salary_from+salary_to) / 2
