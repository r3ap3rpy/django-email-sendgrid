### Welcome

This is a demo inventory app.

In order to use it you have to do the following.

Make sure you sign up for [sendgrid](https://app.sendgrid.com/settings/api_keys) and acquire an API key.
That api key has to be saved in the environment variables.

``` bash
export SENDGRID_API_KEY='YOUR_API_KEY'
```

Then follow these steps to use the API.

``` bash
git clone https://github.com/r3ap3rpy/django-email-sendgrid.git
virtualenv djangoinv
djangoinv\Scripts\activate.bat
pip install django sendgrid
cd django-email-sendgrid
python manage.py migrate
python manage.py makemigrations
python manage.py createsuperuser
python manage.py runserver
```