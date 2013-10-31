=========================
 django-project-template
=========================

Basic template for your Django projects.

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

- django-nose
- factory-boy
- coverage
- nose
- mock

Database
--------

I assume you want to use PostgreSQL, so **dj_database_url** is used to configure it from environment
variable. To enable simple connection pooling i use lovely **django-postgrespool**.

Environment variables
---------------------

There are some environment variables you need to provide in production:

- DATABASE_URL
- SECRET_KEY
