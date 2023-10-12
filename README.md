# service_disbursement

This is an disbursement app that disburse loan amount.

**This is written with Django 3.0.2.**

You can view a working version of this app

Setting up disbursement is very easy. You need to
make changes to requirements.txt, settings.py, and any app code that
you want cached. These changes are covered in detail below.

## Building

It is best to use the python `virtualenv` tool to build locally:

```sh
$ python -m virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ DEVELOPMENT=1 python manage.py runserver
```

Then visit `http://localhost:5032` to view the app. Alternatively you
can use foreman and gunicorn to run the server locally (after copying
`dev.env` to `.env`):

```sh
$ foreman start
```

## requirements.txt

Service disbursement has been tested with postgres. You have to install postgres v12.x

Don't forget to update your requirements.txt file with these new pips.
requirements.txt should have the following two lines:


## Configuring ENV (.env)

Create a env at the root folder of the project file with following parameters

```
DB_MASTER_HOST=
DB_MASTER_PORT=
DB_MASTER_USER=
DB_MASTER_PASSWORD=
DB_MASTER_NAME=

DB_SLAVE_HOST=
DB_SLAVE_PORT=
DB_SLAVE_USER=
DB_SLAVE_PASSWORD=
DB_SLAVE_NAME=

BUGSNAG_API_KEY=
```

## Get involved!

We are happy to receive bug reports, fixes, documentation enhancements,
and other improvements.

Please report bugs via the email.

Master [git repository](http://github.com/memcachier/examples-django):

* `git clone git@code.b2cdev.com/vedic/service/service_disbursement.git`
## Licensing

This library is Biz2Credit Licensed.


