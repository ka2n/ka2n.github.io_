from fabric.api import *
import fabric.contrib.project as project
import os

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path

# Remote server configuration
production = 'root@localhost:22'
dest_path = '/var/www'


def new():
    """Create new post"""
    pass


def clean():
    """remove the generated files"""
    if os.path.isdir(DEPLOY_PATH):
        local('rm -rf {deploy_path}'.format(**env))
        local('mkdir {deploy_path}'.format(**env))


def build():
    """generate the web site"""
    local('pelican -s pelicanconf.py')


def rebuild():
    """clean & build"""
    clean()
    build()


def preview():
    """serve site at http://localhost:8000'"""
    local('pelican -r -s pelicanconf.py')
    local('cd {deploy_path} && python -m SimpleHTTPServer'.format(**env))


def github():
    """upload the web site via gh-pages"""
    rebuild()
    if os.path.isdir(DEPLOY_PATH):
        local('ghp-import -p -b master {deploy_path}'.format(**env))
