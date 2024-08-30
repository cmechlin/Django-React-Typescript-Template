# Django React Typescript Boilerplate

## Manual process to get to this point

(This is just my process. Your welcome to do whatever you want)

### Setup initial git repo

```
git init

create README.md and .gitignore

git add .

git commit -m "initial commit"

git branch dev
```

### Setup python environment

```
python -m venv venv

python -m pip install --upgrade pip

pip install django djangorestframework pylint-django django-debug-toolbar
```

### Setup Django Project

```
django-admin startproject <project name> .

Build sqlite database
python manage.py migrate
```

### Setup Django App

```
python manage.py startapp <app name>
```

## Optional Python Packages

- django-cors-headers
- djangorestframework
- djangorestframework-simplejwt
- pyJWT
- pytz
- sqlparse
- psycopg2-binary # For PostgreSQL
- python-dotenv
