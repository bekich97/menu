# Django tree menu

### Requirements
* Internet :)
* Python3
* Django >= 3.1
* Bootstrap 5

### Usage
I use Ubuntu, so my commands are Ubuntu commands.

1. Create virtual environment and activate it

`virtualenv venv`

`source venv/bin/activate`

2. Install requirements.

`pip install -r requirements.txt`

3. Make migrations and migrate

`python manage.py makemigrations`

`python manage.py migrate`

4. Create superuser

`python manage.py createsuperuser`

5. Run DB seed command. Integer arguments after command is count of menus and menu items. You can write how many you want.

`python manage.py dbseed 5 20`

6. Run server

`python manage.py runserver`

Now you can go to http://127.0.0.1:8000
