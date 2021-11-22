import requests
from pprint import pprint
languages = ["python"]

headers = {
    "User-Agent": "api-test-agent"
}

#{
# vacancies_found: 6695
# vacancies_processed 13
# average_salary: 9988}

def count_vacancies_found(vacancies):
    pass


def count_average_salary(salary):
    pass



def predict_rub_salary(vacancy):
    if vacancy["salary"] and vacancy["salary"]["currency"] == "RUR":
        min_salary = vacancy["salary"]["from"]
        max_salary = vacancy["salary"]["to"]
        if not min_salary:
            return max_salary
        elif not max_salary:
            return min_salary
        else:
            return (min_salary+max_salary)/2
    return None


def get_response_hh():
    for language in languages:
        payload = {
            "text": f"{language}",
            "area": "1",
        }
        url = f"https://api.hh.ru/vacancies/"
        response = requests.get(url, headers=headers, params=payload)
        response.raise_for_status()
        vacancies = response.json()
      #  pprint(vacancies) #["items"]
        return vacancies
   # for vacancy in vacancies:
    #    print(vacancy)
    #    print(predict_rub_salary(vacancy))

def main():
    vacancies = get_response_hh()
    for vacancy in vacancies:
        salaries = [salary for salary in predict_rub_salary(vacancy) if not None]
        print(salaries)
        print("222")



main()
