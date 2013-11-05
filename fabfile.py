# coding=utf-8

import os

from contextlib import contextmanager
from fabric.api import cd, env, prefix, run, local
from fabric.decorators import task

env.user = ''
env.hosts = ['']
env.root = ''
env.project = {
    'name': '{{ project_name }}',
    'repository': '',
    'settings': 'conf.staging.settings',
    'virtualenv': os.path.join(env.root, env.user, 'venv'),
    'root': os.path.join(env.root, env.user, 'app'),
}


@contextmanager
def activate_virtualenv():
    with prefix('source {0}'.format(os.path.join(env.project['virtualenv'], 'bin', 'activate'))):
        yield


@task
def pip(cmd):
    with activate_virtualenv(), cd(env.project['root']):
        run('pip {0}'.format(cmd))


@task
def freeze():
    pip('freeze')


@task
def install():
    with cd(env.project['root']):
        pip('install -r requirements.txt')


@task
def manage(cmd, settings=env.project['settings']):
    with activate_virtualenv(), cd(env.project['root']):
        run('python manage.py {0} --settings={1} --traceback'.format(cmd, settings))


@task
def collectstatic():
    manage('collectstatic --noinput')


@task
def migrate():
    manage('migrate')


@task
def syncdb():
    manage('syncdb')


@task
def git(cmd):
    with cd(env.project['root']):
        run('git {0}'.format(cmd))


@task
def pull():
    git('pull origin master')
    git('submodule init')
    git('submodule update')


@task
def clone():
    git('clone {0} .'.format(env.project['repository']))
    git('submodule init')
    git('submodule update')


@task
def djangoadmin(cmd):
    local('django-admin.py {0}'.format(cmd))


@task(alias='mm')
def makemessages():
    djangoadmin('makemessages --all --ignore=apps/*')


@task(alias='cc')
def compilemessages():
    djangoadmin('compilemessages')


@task
def clean():
    with cd(env.project['root']):
        run('find . -name "*.pyc" -exec rm {} \;')


@task
def localclean():
    local('find . -name "*.pyc" -exec rm {} \;')


@task
def deploy():
    clone()
    install()
    syncdb()
    migrate()
    collectstatic()


@task
def update():
    pull()
    syncdb()
    migrate()
    collectstatic()
