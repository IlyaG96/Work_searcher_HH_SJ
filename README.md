# telegram_space
Скрипт для поиска работы программистом на сайтех hh.ru и superjob.ru
## Установка
Вам понадобится установленный Python 3.6-3.9 и git.

Склонируйте репозиторий:
```bash
$ git clone git@github.com:IlyaG96/Work_searcher_HH_SJ.git
```

Создайте в этой папке виртуальное окружение:
```bash
$ python3 -m venv [полный путь до папки Work_searcher_HH_SJ] env
```

Активируйте виртуальное окружение и установите зависимости:
```bash
$ cd Work_searcher_HH_SJ
$ source env/bin/activate
$ pip install -r requirements.txt
```
## Использование
Заполните прилагающийся .env.exapmle файл и переименуйте его в .env или иным образом задайте переменные среды:

```bash
SJOB_TOKEN = Токен Вашего приложения на сайте SuperJob
LANGUAGES = ["Python", "Java", "C", "PHP", "C#", "Go"]
```
Переменная `LANGUAGES` содержит список языков, для которых будет найдена средняя зарплата

Простейший способ начать поиск средней зарплаты - 
```bash
$ python main.py
```
Программа получит данные по вакансиям с сайтов hh.ru и superjob.ru и представит их в виде таблицы:

### headhunter.py
Содержит логику для работы с API headhunter

### superjob.py
Содержит логику для работы с API superjob