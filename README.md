# My Notes
Look into postman to send http requests to local app

## install requirements
pip install django
pip install djangorestgramework

## create project 
```
python .\env\Scripts\django-admin.exe startproject <project_name>
```


# Create DB
## Make project files
cd into project folder
```
python manage.py makemigrations <app_name>
```
This will create db file, and it will be empty until the migration files are 
used to make the tables for the DB
```
python manage.py migrate
```


# run server
## Update INSTALLED_APPS
Go to project_name.settings.py and add app_name.apps.app_nameConfig
also include rest_framework
## run server
```
python manage.py runserver
```