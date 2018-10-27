Python version used for this project,

```shell
$ python --version
Python 3.6.6
```


You can import csv files (in correct format) using the management command,

```shell
$ python manage.py import-houses PATH_TO_CSV
```

The backend database used is sqlite. You can run the application (after
installing python requirements.txt) using the following,

```shell
$ python manage.py migrate
$ python manage.py runserver
```

At this point, you can visit,

http://127.0.0.1:8000/

to see a swagger interface to access the data. The admin page is located at,

http://127.0.0.1:8000/admin/


Things not done:

* rigorous testing
* fix "/" from appearing in swagger
* project linting/code coverage

Interesting things to do:

* some kind of authentication of the data uploaded - to keep track of who
inputted the data
* discussion of how this API might be used by clients
* API authentication - it's an open and exposed interface right now

 