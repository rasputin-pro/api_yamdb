# API YaMDB (TODO!!!)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
___
REST API для блога Yatube в рамках учебного проекта на курсе 
"**Python-разработчик плюс!**" от Яндекс.Практикум.

API реализован в отдельном приложении под названием **api**. Данные в формате 
**JSON**. Авторизация по **JWT** токену. Авторизованный 
пользователь может создавать, редактировать и удалять свой контент. 
В остальных случаях доступ предоставляется только для чтения.


## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:rasputin-pro/api_yatube.git
```

```commandline
cd yatube_api
```

Cоздать и активировать виртуальное окружение:

```commandline
python3 -m venv env
```

```commandline
source env/bin/activate
```

```commandline
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```commandline
pip install -r requirements.txt
```

Выполнить миграции:

```commandline
python3 manage.py migrate
```

Запустить проект:

```commandline
python3 manage.py runserver
```


## Эндпойнты
| Эндпойнты                           | Разрешенные запросы             |
|-------------------------------------|---------------------------------|
| `/api/v1/posts/`                    | `GET`, `POST`                   |
| `/api/v1/posts/{id}/`               | `GET`, `PUT`, `PATCH`, `DELETE` |
| `/api/v1/posts/{id}/comments/`      | `GET`, `POST`                   |
| `/api/v1/posts/{id}/comments/{id}/` | `GET`, `PUT`, `PATCH`, `DELETE` |
| `/api/v1/groups/`                   | `GET`                           |
| `/api/v1/groups/{id}/`              | `GET`                           |
| `/api/v1/follow/`                   | `GET`, `POST`                   |
| `/api/v1/jwt/create/`               | `POST`                          |
| `/api/v1/jwt/refresh/`              | `POST`                          |
| `/api/v1/jwt/verify/`               | `POST`                          |


## Получение токена
На странице `/api/v1/jwt/create/` передать в формате JSON логин и пароль 
зарегистрированного пользователя: 
```json
{
    "username": "user",
    "password": "bj%w=Sa^0/M*~Lz"
}
```

## Создание записи
Обязательное поле - `text`
Необязательные поля - `image`, `group`
___
**POST** запрос на создание записи `/api/v1/posts/`
```json
{
    "text": "Вечером собрались в редакции «Русской мысли», чтобы поговорить о народном театре. Проект Шехтеля всем нравится.",
    "group": 1
}
```
Пример ответа:
```json
{
    "id": 14,
    "text": "Вечером собрались в редакции «Русской мысли», чтобы поговорить о народном театре. Проект Шехтеля всем нравится.",
    "author": "anton",
    "image": null,
    "group": 1,
    "pub_date": "2021-06-01T08:47:11.084589Z"
}
```

## Создание комментария
Обязательное поле - `text`
___
**POST** запрос на создание комментария к записи `/api/v1/posts/14/comments/`
```json
{
    "text": "Тестовый комментарий."
}
```
Пример ответа:
```json
{
    "id": 4,
    "author": "anton",
    "post": 14,
    "text": "Тестовый комментарий.",
    "created": "2021-06-01T10:14:51.388932Z"
}
```

## Подписки пользователя
Возвращает все подписки пользователя, сделавшего запрос. Анонимные запросы 
запрещены.
Возможен поиск по подпискам по параметру search
___
**GET** запрос авторизованного пользователя 
`/api/v1/follow/`

Пример ответа:
```json
{
    "user": "user",
    "following": "anton"
}
```

## Подписка на автора
Подписка пользователя от имени которого сделан запрос на пользователя 
переданного в теле запроса. Анонимные запросы запрещены.
___
**POST** запрос на создание подписки на автора `/api/v1/follow/`
```json
{
    "following": "anton"
}
```
Пример ответа:
```json
{
    "user": "user",
    "following": "anton"
}
```
