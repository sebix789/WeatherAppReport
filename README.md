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

- asgiref==3.7.2
- certifi==2023.11.17
- charset-normalizer==3.3.2
- Django==5.0.1
- django-environ==0.11.2
- idna==3.6
- psycopg2==2.9.9
- requests==2.31.0
- sqlparse==0.4.4
- tzdata==2023.4
- urllib3==2.1.0

## License

[MIT](https://choosealicense.com/licenses/mit/)
