# django-project-template

## Installation

Creating new project:

```bash
django-admin.py startproject --template=https://github.com/jbub/django-project-template/archive/master.zip project_name
```

Installing initial requirements for local development environment:

```bash
pip install -r requirements/local.txt
```

## Testing

In order to test the project we need to install testing requirements.

```bash
pip install -r requirements/local.txt
```

I use these tools in nearly every project:

* django-nose
* django-dynamic-fixture
* coverage
* nose
* mock
