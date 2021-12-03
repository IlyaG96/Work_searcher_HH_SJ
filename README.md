# Work_searcher_HH_SJ
Скрипт для поиска средней зарплаты программистов на сайтах [hh.ru](hh.ru) и [superjob.ru](superjob.ru)
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
SJOB_TOKEN=Токен Вашего приложения на сайте SuperJob
LANGUAGES=Python Java C PHP C# Go
```
Переменная `LANGUAGES` содержит список языков, для которых будет найдена средняя зарплата. Запятые ставить не надо. Только пробелы

Простейший способ начать поиск средней зарплаты - 
```bash
$ python main.py
```
Программа получит данные по вакансиям с сайтов [hh.ru](hh.ru) и [superjob.ru](superjob.ru) и представит их в виде таблицы:

![](https://downloader.disk.yandex.ru/preview/9d7cb2350e69a64ce5b5bd38653befebab22977d3497486ccdd7d42b41dffa0a/61a70313/aiK_p35wptpfeBleZFkIbcGTbmx8tm2WQyXkxReSpPUATwBE7osJB0J4Akycf2TJJHynJtbni52cRJjF8j4nzA%3D%3D?uid=0&filename=%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-12-01%20%D0%B2%2012.03.22.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=512x512)

### headhunter.py
Содержит логику для работы с API headhunter

### superjob.py
Содержит логику для работы с API superjob
