import os
from pprint import pprint
import requests
from dotenv import load_dotenv
load_dotenv()
sjob_token = os.getenv("SJOB_TOKEN")


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


def get_response_sj():

    headers = {
        "X-Api-App-Id": sjob_token,
    }
    payload = {
        "town": "Москва",
        "keyword": "Программист"
    }
    url = "https://api.superjob.ru/2.0/vacancies/"
    response = requests.get(url, headers=headers, params=payload)
    response.raise_for_status()
    vacancies = response.json()
    return vacancies["objects"]


for number, vacancy in enumerate(get_response_sj()):
    profession = vacancy["profession"]
    town = vacancy["town"]["title"]
    salary = predict_rub_salary_sj(vacancy)
    print(f"{profession}, {town}, {salary}")

get_response_sj()