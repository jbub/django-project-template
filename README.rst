django-project-template
=======================

.. image:: https://requires.io/github/jbub/django-project-template/requirements.png?branch=master
   :target: https://requires.io/github/jbub/django-project-template/requirements/?branch=master
   :alt: Requirements Status

Basic template for your Django 1.8 projects.

Installation
------------

Creating new project:

.. code-block:: bash

    django-admin.py startproject --template=https://github.com/jbub/django-project-template/archive/master.zip project_name

Installing initial requirements for local development environment:

.. code-block:: bash

    pip install -r requirements/local.txt


Testing
-------

In order to test the project we need to install testing requirements.

.. code-block:: bash

    pip install -r requirements/test.txt

I use these tools in nearly every project:

- **pytest-django**
- **factory-boy**
- **coverage**
- **py.test**
- **mock**

Database
--------

- **dj_database_url** for configuring database from environment variable
- **djorm-ext-pool** for simple connection pooling

Environment variables
---------------------

There are some environment variables you need to provide in production/staging environment:

- DATABASE_URL
- SECRET_KEY
- DJANGO_SETTINGS_MODULE
- REDIS_CACHE_URL
