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

- `snippets/models.py`
- `snippets/admin.py`

  - open http://localhost:8000/admin

# 3. Make API endpoints

- `snippets/serializers.py` [ModelSerializer]
- `snippets/views.py` [ListCreateAPIView], [RetrieveUpdateDestroyAPIView]
- `tutorial/urls.py` [include]
- `snippets/urls.py` [format_suffix_pattern]

- open http://localhost:8000/snippets
- open http://localhost:8000/snippets/1
- open http://localhost:8000/snippets/1.json

[ListCreateAPIView]: http://www.django-rest-framework.org/api-guide/generic-views/#listcreateapiview
[RetrieveUpdateDestroyAPIView]: http://www.django-rest-framework.org/api-guide/generic-views/#retrieveupdatedestroyapiview
[include]: https://docs.djangoproject.com/en/5.1/ref/urls/#include
[ModelSerializer]: https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
[format_suffix_pattern]: http://www.django-rest-framework.org/api-guide/format-suffixes/#format_suffix_patterns
