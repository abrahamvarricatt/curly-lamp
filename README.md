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


