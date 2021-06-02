# Policy Quote Part 1 Application

An simple admin and API application to quote policy for customers

## Setup
The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/abinabraham/policyquote_v1
$ cd policyquote_v1
```


Create a virtual environment to install dependencies in and activate it:


```sh
$ python3 -m venv env

$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv2.

Once pip has finished downloading the dependencies:

```sh
(env)$ cd policyquote_v1
(env)$ python manage.py runserver
```

And navigate to http://127.0.0.1:8000/

There you can see, there are unapplied migrations

Create new env file using command

```sh
(env)$ cp .env.example .env
```

And add db details, Debug status and secret key

Example for DB details if db file name db.sqlite3 and in project root =  sqlite:////db.sqlite3

Run the command to migrate all the tables

```sh
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
```


You can create a superuser by command

```sh
(env)$ python manage.py createsuperuser --username="<>" --email="<>"
```

then need to set password also

And navigate to http://127.0.0.1:8000/

You will get API root urls 

The end of PART 1