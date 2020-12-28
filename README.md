# test app

- The [Django](https://www.djangoproject.com/) application is served by WSGI application.
- [Postgres](https://github.com/postgres/postgres) used as database.

## install requirements:
`pip install -U -r requirements.txt`
Create .env by .env.exmaple and configure it

## Migrate databases
`python manage.py migrate`

## run server
`python manage.py runserver`