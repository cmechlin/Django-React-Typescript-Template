# Django React Typescript Boilerplate

This is my Django 5.1 + React x w/ Typescript boilerplate repo.
This served a few purposes

1. To learn how to put all of this together
2. To have a template I can pull from for future projects
3. To provide something to help others later

## Getting Started

## How to use it

### Adding a Django App

```
python manage.py startapp <app name>

modify settings.py - add new app to INSTALLED_APPS

```

### Adding Views

```
edit app views.py
add function to handle route

# create urls in app urls.py
	from django.urls import path
	from . import views

	urlpatterns = [
		path('<route path>/', views.<function name in views.py>())
	]

# then modify project urls.py
add include import to django.urls
add path to urls pattern to point to other urls.py file

	path('<app path>/', include('<app name>.urls'))
```

## If you want to build this entire thing manually

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

pip install django djangorestframework pylint-django
```

### Setup Django Project

```
django-admin startproject <project name> .

Build sqlite database
python manage.py migrate
```

### (Optional) Install Django Debug Toolbar

```
python -m pip install django-debug-toolbar
add 'debug_toolbar', to INSTALLED_APPS in settings.py
add 'debug_toolbar.middleware.DebugToolbarMiddleware', to top of MIDDLEWARE in settings.py
add to settings.py
	INTERNAL_IPS = [
		'127.0.0.1',
	]

add import debug_toolbar to urls.py
add path('__debug__/', include(debug_toolbar.urls), to urlpatterns in project urls.py
```

### Setup Django App

```
python manage.py startapp <app name>

modify settings.py - add new app to INSTALLED_APPS

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
