# Contacts management application

This is the test project for service_fusion.

## Requirements Specification

Write and deploy a simple web application to manage contacts preferably using
Vue, javascript &/ python. It should store a list of persons, containing the
following fields:

* firstname
* lastname
* date of birth
* zero or more addresses
* one or more phone numbers
* one or more emails

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).
Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/) and
[Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone git@github.com:haohong/sf-customers-api.git
$ cd sf-customers-api

$ pipenv install

$ createdb service_fusion

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```

or

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Built With

* [Django-rest-framework](http://www.django-rest-framework.org/) - The web
  framework used for building RESTful api
* [Vue.js](https://vuejs.org/) - The SPA framework used for building frontend
  web app
