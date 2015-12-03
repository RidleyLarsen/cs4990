from fabric.api import hosts, run, env


@hosts('root@198.199.109.62')
def restart():
    env.cwd = '/home/django/cs4990/project9/'
    run('kill -9 $(cat /home/django/cs4990/project9/supervisord.pid)')
    run('supervisord -c supervisord.conf')


@hosts('root@198.199.109.62')
def staticfiles():
    env.cwd = '/home/django/cs4990/project9'
    run('/home/django/cs4990/venv-django/bin/python manage.py collectstatic -l')


@hosts('root@198.199.109.62')
def deploy():
    env.cwd = '/home/django/cs4990/'
    run('git pull')
    restart()
