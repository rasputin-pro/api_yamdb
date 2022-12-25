# API YaMDB

![Python](https://img.shields.io/badge/python-3670A0?logo=python&logoColor=ffdd54)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?logo=django&logoColor=white&color=ff1709&labelColor=gray)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?logo=sqlite&logoColor=white)
___
Учебный проект на базе фреймворка **Django** и **Django REST**.

API YaMDb — собирает отзывы пользователей на произведения. 
Авторизованные пользователи оставляют к произведениям текстовые 
отзывы (Review) и ставят оценку в диапазоне от одного до 
десяти. Из пользовательских оценок формируется рейтинг. На одно произведение 
пользователь может оставить только один отзыв.

Сами произведения (Title) в проекте не хранятся, здесь нельзя посмотреть 
фильм или послушать музыку. Но создавая отзыв, 
пользователь указывает название произведения, назначает ему категорию 
(Category), и может указать несколько жанров (Genre) из предустановленных. 
Новые жанры может создавать только администратор.

## Стек технологий:
- Python 3.7
- Django 2.2.28
- Django REST
- SQLite

## Как запустить проект:
<details>
    <summary><b>Клонируйте репозиторий</b></summary>

```commandline
git clone git@github.com:rasputin-pro/api_yamdb.git

cd api_yamdb
```
</details>

<details>
    <summary><b>Создайте и активируйте виртуальное окружение</b></summary>

```shell
# Linux/MacOS
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip

# Windows
python -m venv venv
source venv/scripts/activate
python -m pip install --upgrade pip
```
> В проекте используется **Python** версии **3.7**
</details>

<details>
    <summary>
        <b>Установите зависимости из файла <code>requirements.txt</code></b>
    </summary>

```shell
pip install -r requirements.txt
```
</details>

<details>
    <summary><b>Примените миграции</b></summary>

```shell
# Linux/MacOS
python3 api_yamdb/manage.py migrate

# Windows
python api_yamdb/manage.py migrate
```
</details>

<details>
    <summary><b>Запустите программу</b></summary>

```shell
python3 api_yamdb/manage.py runserver
```
</details>

<details>
    <summary><b>Для загрузки тестовых данных из csv-файлов выполните команду
    </b></summary>

```commandline
python3 api_yamdb/manage.py loadcsv
```
</details>


## Самостоятельная регистрация пользователей
1. Пользователь отправляет POST-запрос на добавление нового пользователя с 
параметрами `email` и `username` на эндпоинт `/api/v1/auth/signup/`: 
```json
{
    "username": "user",
    "email": "user@mail.ru"
}
```
2. Пользователю приходит письмо с кодом подтверждения `confirmation_code` на 
адрес `email`;
3. Пользователь отправляет POST-запрос с параметрами `username` и 
`confirmation_code` на эндпоинт `/api/v1/auth/token/`, в ответе на запрос ему 
приходит `token` (JWT-токен):
```json
{
    "username": "user",
    "confirmation_code": "ae6c10d0-0b13-554c-b976-a05d8a18f0cc"
}
```
4. При желании пользователь отправляет PATCH-запрос на эндпоинт 
`/api/v1/users/me/` и заполняет поля в своём профайле.



## Создание пользователя администратором
Пользователя может создать администратор — через админ-зону сайта или через 
POST-запрос на специальный эндпоинт `/api/v1/users/` В этот момент письмо с 
кодом подтверждения пользователю не отправляется.

После этого пользователь должен самостоятельно отправить свой `email` и 
`username` на эндпоинт `/api/v1/auth/signup/`, в ответ ему должно прийти 
письмо с кодом подтверждения.

Далее пользователь отправляет POST-запрос с параметрами `username` и 
`confirmation_code` на эндпоинт `/api/v1/auth/token/`, в ответе на запрос ему 
приходит `token` (JWT-токен), как и при самостоятельной регистрации.


## Ресурсы API YaMDb
- **auth**: аутентификация.
- **users**: пользователи.
- **titles**: произведения, к которым пишут отзывы (определённый фильм, 
  книга или песенка).
- **categories**: категории (типы) произведений («Фильмы», «Книги», 
  «Музыка»).
- **genres**: жанры произведений. Одно произведение может быть привязано 
  к нескольким жанрам.
- **reviews**: отзывы на произведения. Отзыв привязан к определённому 
  произведению.
- **comments**: комментарии к отзывам. Комментарий привязан к 
  определённому отзыву.


## Документация
После запуска программы документация будет доступна по адресу:

[http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)


## Над проектом работали:
- [Андрей Распутин](https://github.com/rasputin-pro)
- [Кирилл Сухарев](https://github.com/Soliton80)
- [Александр Корнеев](https://github.com/rtx4090)
