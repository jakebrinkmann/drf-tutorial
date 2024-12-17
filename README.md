<center>source: https://learndjango.com/tutorials/official-django-rest-framework-tutorial-beginners</center>

# 1. Getting Started

```bash
source .venv/bin/activate

python -m pip install django djangorestframework

django-admin startproject tutorial123 .

python manage.py startapp snippets
```

# 2. Create models

```bash
python manage.py makemigrations snippets
python manage.py migrate snippets

python manage.py createsuperuser

python manage.py runserver
```

- open http://localhost:8000
- open http://localhost:8000/admin
