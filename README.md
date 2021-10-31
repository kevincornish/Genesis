# Genesis
### Genesis is a BitTorrent tracker web framework. Genesis is written in Python using the Django framework. 

# Installation
Install Python

Install Postgres

```
git clone https://github.com/kevincornish/Genesis
```

Create Virtual Environment 
```
py -m venv env
```
Activate Environment
Mac/Unix
```
source env/bin/activate
```
Windows
```
.\env\Scripts\activate
```

Install requirements for local development
```
pip install -r requirements/local.txt
```

Fill in ```genesis/sample.env``` and rename to ```.env```

Make migrations and then run migrations
```
python manage.py makemigrations
python manage.py migrate
```

Create a superuser
```
python manage.py createsuperuser
```