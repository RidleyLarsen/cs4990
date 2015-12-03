from fabric.api import hosts, run, env

@hosts('root@198.199.109.62')
def deploy():
    env.cwd = '/home/django/cs4990/'
    run('git pull')
