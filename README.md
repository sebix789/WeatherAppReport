# Weather Report App

Basic weather app which use OpenWeatherAPI to store data in postgres DB, show on graphical UI and generates emails report. Created as studies project 

## Installation

To run this project use:

- build virtual environment
```bash
python -m venv venv
```
- if you don't have `venv` installed use command below
```bash
pip install venv
```
- activate your environment
```bash
venv/Scripts/activate
```
- run python server
```bash
python manage.py runserver
```
## Packages

Packages used in project:

- amqp==5.2.0
- asgiref==3.7.2
- billiard==4.2.0
- celery==5.3.6
- certifi==2023.11.17
- cfgv==3.4.0
- charset-normalizer==3.3.2
- click==8.1.7
- click-didyoumean==0.3.0
- click-plugins==1.1.1
- click-repl==0.3.0
- colorama==0.4.6
- distlib==0.3.8
- Django==4.2.7
- django-environ==0.11.2
- django-extensions==3.2.3
- filelock==3.13.1
- identify==2.5.33
- idna==3.6
- kombu==5.3.4
- nodeenv==1.8.0
- platformdirs==4.1.0
- pre-commit==3.6.0
- prompt-toolkit==3.0.43
- psycopg==3.1.13
- psycopg-binary==3.1.17
- psycopg2==2.9.9
- python-dateutil==2.8.2
- PyYAML==6.0.1
- redis==5.0.1
- requests==2.31.0
- six==1.16.0
- sqlparse==0.4.4
- typing_extensions==4.8.0
- tzdata==2023.3
- urllib3==2.1.0
- vine==5.1.0
- virtualenv==20.25.0
- wcwidth==0.2.13

## License

[MIT](https://choosealicense.com/licenses/mit/)
